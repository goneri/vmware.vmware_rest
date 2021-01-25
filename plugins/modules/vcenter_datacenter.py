#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright: Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: DEFAULT_MODULE

DOCUMENTATION = """
module: vcenter_datacenter
short_description: Manage the datacenter of a vCenter
description: Manage the datacenter of a vCenter
options:
  datacenter:
    description:
    - Identifier of the datacenter to be deleted.
    - The parameter must be the id of a resource returned by M(vcenter_datacenter_info).
      Required with I(state=['absent'])
    type: str
  folder:
    description:
    - Datacenter folder in which the new datacenter should be created.
    - This field is currently required. In the future, if this field is unset, the
      system will attempt to choose a suitable folder for the datacenter; if a folder
      cannot be chosen, the datacenter creation operation will fail.
    - 'When clients pass a value of this structure as a parameter, the field must
      be the id of a resource returned by M(vcenter_folder_info). '
    type: str
  force:
    description:
    - If true, delete the datacenter even if it is not empty.
    - If unset a ResourceInUse error will be reported if the datacenter is not empty.
      This is the equivalent of passing the value false.
    type: bool
  name:
    description:
    - The name of the datacenter to be created. Required with I(state=['present'])
    type: str
  state:
    choices:
    - absent
    - present
    default: present
    description: []
    type: str
  vcenter_hostname:
    description:
    - The hostname or IP address of the vSphere vCenter
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_HOST) will be used instead.
    required: true
    type: str
  vcenter_password:
    description:
    - The vSphere vCenter username
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_PASSWORD) will be used instead.
    required: true
    type: str
  vcenter_rest_log_file:
    description:
    - 'You can use this optional parameter to set the location of a log file. '
    - 'This file will be used to record the HTTP REST interaction. '
    - 'The file will be stored on the host that run the module. '
    - 'If the value is not specified in the task, the value of '
    - environment variable C(VMWARE_REST_LOG_FILE) will be used instead.
    type: str
  vcenter_username:
    description:
    - The vSphere vCenter username
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_USER) will be used instead.
    required: true
    type: str
  vcenter_validate_certs:
    default: true
    description:
    - Allows connection when SSL certificates are not valid. Set to C(false) when
      certificates are not trusted.
    - If the value is not specified in the task, the value of environment variable
      C(VMWARE_VALIDATE_CERTS) will be used instead.
    type: bool
author:
- Goneri Le Bouder (@goneri) <goneri@lebouder.net>
version_added: 1.0.0
requirements:
- python >= 3.6
- aiohttp
"""

EXAMPLES = """
- name: Get a list of all the datacenters
  register: existing_datacenters
  vmware.vmware_rest.vcenter_datacenter_info:
- name: Set my_datacenter_folder
  set_fact:
    my_datacenter_folder: '{{ my_folders.value|selectattr("type", "equalto", "DATACENTER")|first
      }}'
- name: Create datacenter my_dc
  vmware.vmware_rest.vcenter_datacenter:
    name: my_dc
    folder: '{{ my_datacenter_folder.folder }}'
- name: Force delete the existing DC
  vmware.vmware_rest.vcenter_datacenter:
    state: absent
    datacenter: '{{ item.datacenter }}'
    force: true
  with_items: '{{ existing_datacenters.value }}'
"""

RETURN = """
# content generated by the update_return_section callback# task: Force delete the existing DC
msg:
  description: Force delete the existing DC
  returned: On success
  sample: All items completed
  type: str
results:
  description: Force delete the existing DC
  returned: On success
  sample:
  - _ansible_item_label:
      datacenter: datacenter-1286
      name: my_dc
    _ansible_no_log: 0
    _debug_info:
      operation: delete
      status: 200
    ansible_loop_var: item
    changed: 1
    failed: 0
    invocation:
      module_args:
        datacenter: datacenter-1286
        folder: null
        force: 1
        name: null
        state: absent
        vcenter_hostname: vcenter.test
        vcenter_password: VALUE_SPECIFIED_IN_NO_LOG_PARAMETER
        vcenter_rest_log_file: null
        vcenter_username: administrator@vsphere.local
        vcenter_validate_certs: 0
    item:
      datacenter: datacenter-1286
      name: my_dc
  type: list
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "list": {
        "query": {
            "filter.datacenters": "filter.datacenters",
            "filter.folders": "filter.folders",
            "filter.names": "filter.names",
        },
        "body": {},
        "path": {},
    },
    "create": {
        "query": {},
        "body": {"folder": "spec/folder", "name": "spec/name"},
        "path": {},
    },
    "delete": {
        "query": {"force": "force"},
        "body": {},
        "path": {"datacenter": "datacenter"},
    },
    "get": {"query": {}, "body": {}, "path": {"datacenter": "datacenter"}},
}  # pylint: disable=line-too-long

import json
import socket
from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.exceptions import (
        EmbeddedModuleFailure,
    )
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )
except ImportError:
    from ansible.module_utils.basic import AnsibleModule

AnsibleModule.collection_name = "vmware.vmware_rest"

from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    build_full_device_list,
    exists,
    gen_args,
    get_device_info,
    get_subdevice_type,
    list_devices,
    open_session,
    prepare_payload,
    update_changed_flag,
)


def prepare_argument_spec():
    argument_spec = {
        "vcenter_hostname": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_HOST"]),
        ),
        "vcenter_username": dict(
            type="str", required=True, fallback=(env_fallback, ["VMWARE_USER"]),
        ),
        "vcenter_password": dict(
            type="str",
            required=True,
            no_log=True,
            fallback=(env_fallback, ["VMWARE_PASSWORD"]),
        ),
        "vcenter_validate_certs": dict(
            type="bool",
            required=False,
            default=True,
            fallback=(env_fallback, ["VMWARE_VALIDATE_CERTS"]),
        ),
        "vcenter_rest_log_file": dict(
            type="str",
            required=False,
            fallback=(env_fallback, ["VMWARE_REST_LOG_FILE"]),
        ),
    }

    argument_spec["datacenter"] = {"type": "str"}
    argument_spec["folder"] = {"type": "str"}
    argument_spec["force"] = {"type": "bool"}
    argument_spec["name"] = {"type": "str"}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["absent", "present"],
        "default": "present",
    }

    return argument_spec


async def main():
    module_args = prepare_argument_spec()
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    if not module.params["vcenter_hostname"]:
        module.fail_json("vcenter_hostname cannot be empty")
    if not module.params["vcenter_username"]:
        module.fail_json("vcenter_username cannot be empty")
    if not module.params["vcenter_password"]:
        module.fail_json("vcenter_password cannot be empty")
    try:
        session = await open_session(
            vcenter_hostname=module.params["vcenter_hostname"],
            vcenter_username=module.params["vcenter_username"],
            vcenter_password=module.params["vcenter_password"],
            validate_certs=module.params["vcenter_validate_certs"],
            log_file=module.params["vcenter_rest_log_file"],
        )
    except EmbeddedModuleFailure as err:
        module.fail_json(err.get_message())
    result = await entry_point(module, session)
    module.exit_json(**result)


# template: URL
def build_url(params):
    return ("https://{vcenter_hostname}" "/rest/vcenter/datacenter").format(**params)


# template: main_content
async def entry_point(module, session):
    if module.params["state"] == "present":
        if "_create" in globals():
            operation = "create"
        else:
            operation = "update"
    elif module.params["state"] == "absent":
        operation = "delete"
    else:
        operation = module.params["state"]

    func = globals()["_" + operation]
    return await func(module.params, session)


# FUNC_WITH_DATA_CREATE_TPL
async def _create(params, session):
    if params["datacenter"]:
        _json = await get_device_info(session, build_url(params), params["datacenter"])
    else:
        _json = await exists(params, session, build_url(params), ["datacenter"])
    if _json:
        if "_update" in globals():
            params["datacenter"] = _json["id"]
            return await globals()["_update"](params, session)
        return await update_changed_flag(_json, 200, "get")

    payload = prepare_payload(params, PAYLOAD_FORMAT["create"])
    _url = ("https://{vcenter_hostname}" "/rest/vcenter/datacenter").format(**params)
    async with session.post(_url, json=payload) as resp:
        if resp.status == 500:
            text = await resp.text()
            raise EmbeddedModuleFailure(
                f"Request has failed: status={resp.status}, {text}"
            )
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        # Update the value field with all the details
        if (resp.status in [200, 201]) and "value" in _json:
            if isinstance(_json["value"], dict):
                _id = list(_json["value"].values())[0]
            else:
                _id = _json["value"]
            _json = await get_device_info(session, _url, _id)

        return await update_changed_flag(_json, resp.status, "create")


# template: FUNC_WITH_DATA_DELETE_TPL
async def _delete(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["delete"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["delete"])
    subdevice_type = get_subdevice_type("/rest/vcenter/datacenter/{datacenter}")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}" "/rest/vcenter/datacenter/{datacenter}"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.delete(_url, json=payload) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        return await update_changed_flag(_json, resp.status, "delete")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
