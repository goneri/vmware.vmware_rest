#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: content_locallibrary_info
short_description: Returns a given local library.
description: Returns a given local library.
options:
  library_id:
    description:
    - Identifier of the local library to return. Required with I(state=['get'])
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
- Ansible Cloud Team (@ansible-collections)
version_added: 1.0.0
requirements:
- python >= 3.6
- aiohttp
"""

EXAMPLES = r"""
- name: Retrieve the local content library information
  vmware.vmware_rest.content_locallibrary_info:
  register: result

- name: Set test local library id for further testing
  set_fact:
    test_library_id: '{{ result.value[0] }}'

- name: Retrieve the local content library information based upon id check mode
  vmware.vmware_rest.content_locallibrary_info:
    library_id: '{{ test_library_id }}'
  register: result
  check_mode: true

- name: Retrieve the local content library information based upon id
  vmware.vmware_rest.content_locallibrary_info:
    library_id: '{{ test_library_id }}'
  register: result
"""

RETURN = r"""
# content generated by the update_return_section callback# task: Retrieve the local content library information based upon id check mode
id:
  description: moid of the resource
  returned: On success
  sample: 2c80c874-2914-49c5-b38f-325edc65d116
  type: str
value:
  description: Retrieve the local content library information based upon id check
    mode
  returned: On success
  sample:
    creation_time: '2021-05-05T14:35:42.786Z'
    description: automated
    id: 2c80c874-2914-49c5-b38f-325edc65d116
    last_modified_time: '2021-05-05T14:35:42.786Z'
    name: local_library_001
    publish_info:
      authentication_method: NONE
      persist_json_enabled: 0
      publish_url: https://vcenter.test:443/cls/vcsp/lib/2c80c874-2914-49c5-b38f-325edc65d116/lib.json
      published: 1
      user_name: vcsp
    server_guid: 059dd233-dedf-4960-bba8-ab6710e6aeb4
    storage_backings:
    - datastore_id: datastore-1089
      type: DATASTORE
    type: LOCAL
    version: '2'
  type: dict
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "create": {
        "query": {"client_token": "client_token"},
        "body": {
            "creation_time": "creation_time",
            "description": "description",
            "id": "id",
            "last_modified_time": "last_modified_time",
            "last_sync_time": "last_sync_time",
            "name": "name",
            "optimization_info": "optimization_info",
            "publish_info": "publish_info",
            "server_guid": "server_guid",
            "storage_backings": "storage_backings",
            "subscription_info": "subscription_info",
            "type": "type",
            "version": "version",
        },
        "path": {},
    },
    "list": {"query": {}, "body": {}, "path": {}},
    "get": {"query": {}, "body": {}, "path": {"library_id": "library_id"}},
    "update": {
        "query": {},
        "body": {
            "creation_time": "creation_time",
            "description": "description",
            "id": "id",
            "last_modified_time": "last_modified_time",
            "last_sync_time": "last_sync_time",
            "name": "name",
            "optimization_info": "optimization_info",
            "publish_info": "publish_info",
            "server_guid": "server_guid",
            "storage_backings": "storage_backings",
            "subscription_info": "subscription_info",
            "type": "type",
            "version": "version",
        },
        "path": {"library_id": "library_id"},
    },
    "delete": {"query": {}, "body": {}, "path": {"library_id": "library_id"}},
    "publish": {
        "query": {},
        "body": {"subscriptions": "subscriptions"},
        "path": {"library_id": "library_id"},
    },
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

    AnsibleModule.collection_name = "vmware.vmware_rest"
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
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

    argument_spec["library_id"] = {"type": "str"}

    return argument_spec


async def main():
    required_if = list([])

    module_args = prepare_argument_spec()
    module = AnsibleModule(
        argument_spec=module_args, required_if=required_if, supports_check_mode=True
    )
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


# template: info_list_and_get_module.j2
def build_url(params):
    if params.get("library_id"):
        _in_query_parameters = PAYLOAD_FORMAT["get"]["query"].keys()
        return (
            ("https://{vcenter_hostname}" "/api/content/local-library/").format(
                **params
            )
            + params["library_id"]
            + gen_args(params, _in_query_parameters)
        )
    _in_query_parameters = PAYLOAD_FORMAT["list"]["query"].keys()
    return ("https://{vcenter_hostname}" "/api/content/local-library").format(
        **params
    ) + gen_args(params, _in_query_parameters)


async def entry_point(module, session):
    url = build_url(module.params)
    async with session.get(url) as resp:
        _json = await resp.json()

        if "value" not in _json:  # 7.0.2+
            _json = {"value": _json}

        if module.params.get("library_id"):
            _json["id"] = module.params.get("library_id")
        elif module.params.get("label"):  # TODO extend the list of filter
            _json = await exists(module.params, session, url)
        else:  # list context, retrieve the details of each entry
            try:
                if (
                    isinstance(_json["value"][0]["library_id"], str)
                    and len(list(_json["value"][0].values())) == 1
                ):
                    # this is a list of id, we fetch the details
                    full_device_list = await build_full_device_list(session, url, _json)
                    _json = {"value": [i["value"] for i in full_device_list]}
            except (TypeError, KeyError, IndexError):
                pass

        return await update_changed_flag(_json, resp.status, "get")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
