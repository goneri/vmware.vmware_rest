#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2

from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: vcenter_vm_hardware_ethernet
short_description: Manage the ethernet of a VM
description: Manage the ethernet of a VM
options:
  allow_guest_control:
    description:
    - Flag indicating whether the guest can connect and disconnect the device.
    - If unset, the value is unchanged.
    type: bool
  backing:
    description:
    - Physical resource backing for the virtual Ethernet adapter.
    - If unset, the system may try to find an appropriate backing. If one is not found,
      the request will fail.
    - 'Valid attributes are:'
    - ' - C(distributed_port) (str): Key of the distributed virtual port that backs
      the virtual Ethernet adapter. Depending on the type of the Portgroup, the port
      may be specified using this field. If the portgroup type is early-binding (also
      known as static), a port is assigned when the Ethernet adapter is configured
      to use the port. The port may be either automatically or specifically assigned
      based on the value of this field. If the portgroup type is ephemeral, the port
      is created and assigned to a virtual machine when it is powered on and the Ethernet
      adapter is connected. This field cannot be specified as no free ports exist
      before use.'
    - May be used to specify a port when the network specified on the I(network) field
      is a static or early binding distributed portgroup. If unset, the port will
      be automatically assigned to the Ethernet adapter based on the policy embodied
      by the portgroup type.
    - ' - C(network) (str): Identifier of the network that backs the virtual Ethernet
      adapter.'
    - This field is optional and it is only relevant when the value of I(type) is
      one of STANDARD_PORTGROUP, DISTRIBUTED_PORTGROUP, or OPAQUE_NETWORK.
    - 'When clients pass a value of this structure as a parameter, the field must
      be the id of a resource returned by M(vcenter_network_info). '
    - ' - C(type) (str): This option defines the valid backing types for a virtual
      Ethernet adapter.'
    - '   - Accepted values:'
    - '     - STANDARD_PORTGROUP'
    - '     - HOST_DEVICE'
    - '     - DISTRIBUTED_PORTGROUP'
    - '     - OPAQUE_NETWORK'
    type: dict
  label:
    description: []
    type: str
  mac_address:
    description:
    - 'MAC address. '
    - ' This field may be modified at any time, and changes will be applied the next
      time the virtual machine is powered on.'
    - ''
    - If unset, the value is unchanged. Must be specified if I(mac_type) is MANUAL.
      Must be unset if the MAC address type is not MANUAL.
    type: str
  mac_type:
    choices:
    - ASSIGNED
    - GENERATED
    - MANUAL
    description:
    - The I(mac_address_type) enumerated type defines the valid MAC address origins
      for a virtual Ethernet adapter.
    type: str
  nic:
    description:
    - Virtual Ethernet adapter identifier.
    - The parameter must be the id of a resource returned by M(vcenter_vm_hardware_ethernet).
      Required with I(state=['absent', 'connect', 'disconnect', 'present'])
    type: str
  pci_slot_number:
    description:
    - Address of the virtual Ethernet adapter on the PCI bus. If the PCI address is
      invalid, the server will change when it the VM is started or as the device is
      hot added.
    - If unset, the server will choose an available address when the virtual machine
      is powered on.
    type: int
  start_connected:
    description:
    - Flag indicating whether the virtual device should be connected whenever the
      virtual machine is powered on.
    - If unset, the value is unchanged.
    type: bool
  state:
    choices:
    - absent
    - connect
    - disconnect
    - present
    default: present
    description: []
    type: str
  type:
    choices:
    - E1000
    - E1000E
    - PCNET32
    - VMXNET
    - VMXNET2
    - VMXNET3
    description:
    - The I(emulation_type) enumerated type defines the valid emulation types for
      a virtual Ethernet adapter.
    type: str
  upt_compatibility_enabled:
    description:
    - 'Flag indicating whether Universal Pass-Through (UPT) compatibility should be
      enabled on this virtual Ethernet adapter. '
    - ' This field may be modified at any time, and changes will be applied the next
      time the virtual machine is powered on.'
    - ''
    - If unset, the value is unchanged. Must be unset if the emulation type of the
      virtual Ethernet adapter is not VMXNET3.
    type: bool
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
  vm:
    description:
    - Virtual machine identifier.
    - The parameter must be the id of a resource returned by M(vcenter_vm_info). This
      parameter is mandatory.
    required: true
    type: str
  wake_on_lan_enabled:
    description:
    - 'Flag indicating whether wake-on-LAN shoud be enabled on this virtual Ethernet
      adapter. '
    - ' This field may be modified at any time, and changes will be applied the next
      time the virtual machine is powered on.'
    - ''
    - If unset, the value is unchanged.
    type: bool
author:
- Goneri Le Bouder (@goneri) <goneri@lebouder.net>
version_added: 1.0.0
requirements:
- python >= 3.6
- aiohttp
"""

EXAMPLES = r"""
"""

RETURN = r"""
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "list": {"query": {}, "body": {}, "path": {"vm": "vm"}},
    "create": {
        "query": {},
        "body": {
            "allow_guest_control": "spec/allow_guest_control",
            "backing": "spec/backing",
            "mac_address": "spec/mac_address",
            "mac_type": "spec/mac_type",
            "pci_slot_number": "spec/pci_slot_number",
            "start_connected": "spec/start_connected",
            "type": "spec/type",
            "upt_compatibility_enabled": "spec/upt_compatibility_enabled",
            "wake_on_lan_enabled": "spec/wake_on_lan_enabled",
        },
        "path": {"vm": "vm"},
    },
    "delete": {"query": {}, "body": {}, "path": {"nic": "nic", "vm": "vm"}},
    "get": {"query": {}, "body": {}, "path": {"nic": "nic", "vm": "vm"}},
    "update": {
        "query": {},
        "body": {
            "allow_guest_control": "spec/allow_guest_control",
            "backing": "spec/backing",
            "mac_address": "spec/mac_address",
            "mac_type": "spec/mac_type",
            "start_connected": "spec/start_connected",
            "upt_compatibility_enabled": "spec/upt_compatibility_enabled",
            "wake_on_lan_enabled": "spec/wake_on_lan_enabled",
        },
        "path": {"nic": "nic", "vm": "vm"},
    },
    "connect": {"query": {}, "body": {}, "path": {"nic": "nic", "vm": "vm"}},
    "disconnect": {"query": {}, "body": {}, "path": {"nic": "nic", "vm": "vm"}},
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

    argument_spec["allow_guest_control"] = {"type": "bool"}
    argument_spec["backing"] = {"type": "dict"}
    argument_spec["label"] = {"type": "str"}
    argument_spec["mac_address"] = {"type": "str"}
    argument_spec["mac_type"] = {
        "type": "str",
        "choices": ["ASSIGNED", "GENERATED", "MANUAL"],
    }
    argument_spec["nic"] = {"type": "str"}
    argument_spec["pci_slot_number"] = {"type": "int"}
    argument_spec["start_connected"] = {"type": "bool"}
    argument_spec["state"] = {
        "type": "str",
        "choices": ["absent", "connect", "disconnect", "present"],
        "default": "present",
    }
    argument_spec["type"] = {
        "type": "str",
        "choices": ["E1000", "E1000E", "PCNET32", "VMXNET", "VMXNET2", "VMXNET3"],
    }
    argument_spec["upt_compatibility_enabled"] = {"type": "bool"}
    argument_spec["vm"] = {"required": True, "type": "str"}
    argument_spec["wake_on_lan_enabled"] = {"type": "bool"}

    return argument_spec


async def main():
    required_if = list(
        [
            ["state", "connect", ["nic", "vm"], True],
            ["state", "absent", ["nic", "vm"], True],
            ["state", "disconnect", ["nic", "vm"], True],
            ["state", "present", ["nic", "vm"], True],
        ]
    )

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


# template: default_module.j2
def build_url(params):
    return (
        "https://{vcenter_hostname}" "/rest/vcenter/vm/{vm}/hardware/ethernet"
    ).format(**params)


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


async def _connect(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["connect"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["connect"])
    subdevice_type = get_subdevice_type(
        "/rest/vcenter/vm/{vm}/hardware/ethernet/{nic}/connect"
    )
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        "/rest/vcenter/vm/{vm}/hardware/ethernet/{nic}/connect"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        return await update_changed_flag(_json, resp.status, "connect")


async def _create(params, session):

    if params["nic"]:
        _json = await get_device_info(session, build_url(params), params["nic"])
    else:
        _json = await exists(params, session, build_url(params), ["nic"])
    if _json:
        if "_update" in globals():
            params["nic"] = _json["id"]
            return await globals()["_update"](params, session)
        return await update_changed_flag(_json, 200, "get")

    payload = prepare_payload(params, PAYLOAD_FORMAT["create"])
    _url = (
        "https://{vcenter_hostname}" "/rest/vcenter/vm/{vm}/hardware/ethernet"
    ).format(**params)
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


async def _delete(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["delete"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["delete"])
    subdevice_type = get_subdevice_type("/rest/vcenter/vm/{vm}/hardware/ethernet/{nic}")
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}" "/rest/vcenter/vm/{vm}/hardware/ethernet/{nic}"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.delete(_url, json=payload) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        return await update_changed_flag(_json, resp.status, "delete")


async def _disconnect(params, session):
    _in_query_parameters = PAYLOAD_FORMAT["disconnect"]["query"].keys()
    payload = prepare_payload(params, PAYLOAD_FORMAT["disconnect"])
    subdevice_type = get_subdevice_type(
        "/rest/vcenter/vm/{vm}/hardware/ethernet/{nic}/disconnect"
    )
    if subdevice_type and not params[subdevice_type]:
        _json = await exists(params, session, build_url(params))
        if _json:
            params[subdevice_type] = _json["id"]
    _url = (
        "https://{vcenter_hostname}"
        "/rest/vcenter/vm/{vm}/hardware/ethernet/{nic}/disconnect"
    ).format(**params) + gen_args(params, _in_query_parameters)
    async with session.post(_url, json=payload) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        return await update_changed_flag(_json, resp.status, "disconnect")


async def _update(params, session):
    payload = prepare_payload(params, PAYLOAD_FORMAT["update"])
    _url = (
        "https://{vcenter_hostname}" "/rest/vcenter/vm/{vm}/hardware/ethernet/{nic}"
    ).format(**params)
    async with session.get(_url) as resp:
        _json = await resp.json()
        for k, v in _json["value"].items():
            if k in payload and payload[k] == v:
                del payload[k]
            elif "spec" in payload:
                if k in payload["spec"] and payload["spec"][k] == v:
                    del payload["spec"][k]

        if payload == {} or payload == {"spec": {}}:
            # Nothing has changed
            _json["id"] = params.get("nic")
            return await update_changed_flag(_json, resp.status, "get")
    async with session.patch(_url, json=payload) as resp:
        try:
            if resp.headers["Content-Type"] == "application/json":
                _json = await resp.json()
        except KeyError:
            _json = {}
        _json["id"] = params.get("nic")
        return await update_changed_flag(_json, resp.status, "update")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
