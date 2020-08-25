#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

DOCUMENTATION = """
module: vcenter_vm_info
short_description: Handle resource of type vcenter_vm
description: Handle resource of type vcenter_vm
options:
  filter_clusters:
    description:
    - Clusters that must contain the virtual machine for the virtual machine to match
      the filter.
    - If unset or empty, virtual machines in any cluster match the filter.
    - 'When clients pass a value of this structure as a parameter, the field must
      contain identifiers for the resource type: ClusterComputeResource. When operations
      return a value of this structure as a result, the field will contain identifiers
      for the resource type: ClusterComputeResource.'
    elements: str
    type: list
  filter_datacenters:
    description:
    - Datacenters that must contain the virtual machine for the virtual machine to
      match the filter.
    - If unset or empty, virtual machines in any datacenter match the filter.
    - 'When clients pass a value of this structure as a parameter, the field must
      contain identifiers for the resource type: Datacenter. When operations return
      a value of this structure as a result, the field will contain identifiers for
      the resource type: Datacenter.'
    elements: str
    type: list
  filter_folders:
    description:
    - Folders that must contain the virtual machine for the virtual machine to match
      the filter.
    - If unset or empty, virtual machines in any folder match the filter.
    - 'When clients pass a value of this structure as a parameter, the field must
      contain identifiers for the resource type: Folder. When operations return a
      value of this structure as a result, the field will contain identifiers for
      the resource type: Folder.'
    elements: str
    type: list
  filter_hosts:
    description:
    - Hosts that must contain the virtual machine for the virtual machine to match
      the filter.
    - If unset or empty, virtual machines on any host match the filter.
    - 'When clients pass a value of this structure as a parameter, the field must
      contain identifiers for the resource type: HostSystem. When operations return
      a value of this structure as a result, the field will contain identifiers for
      the resource type: HostSystem.'
    elements: str
    type: list
  filter_names:
    description:
    - Names that virtual machines must have to match the filter (see VM.Info.name).
    - If unset or empty, virtual machines with any name match the filter.
    elements: str
    type: list
  filter_power_states:
    description:
    - Power states that a virtual machine must be in to match the filter (see Power.Info.state.
    - If unset or empty, virtual machines in any power state match the filter.
    elements: str
    type: list
  filter_resource_pools:
    description:
    - Resource pools that must contain the virtual machine for the virtual machine
      to match the filter.
    - If unset or empty, virtual machines in any resource pool match the filter.
    - 'When clients pass a value of this structure as a parameter, the field must
      contain identifiers for the resource type: ResourcePool. When operations return
      a value of this structure as a result, the field will contain identifiers for
      the resource type: ResourcePool.'
    elements: str
    type: list
  filter_vms:
    description:
    - Identifiers of virtual machines that can match the filter.
    - If unset or empty, virtual machines with any identifier match the filter.
    - 'When clients pass a value of this structure as a parameter, the field must
      contain identifiers for the resource type: VirtualMachine. When operations return
      a value of this structure as a result, the field will contain identifiers for
      the resource type: VirtualMachine.'
    elements: str
    type: list
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
    - 'The parameter must be an identifier for the resource type: VirtualMachine.
      Required with I(state=[''get''])'
    type: str
author:
- Goneri Le Bouder (@goneri) <goneri@lebouder.net>
version_added: 1.0.0
requirements:
- python >= 3.6
- aiohttp
"""

EXAMPLES = """
- register: test_vm1
  vcenter_vm_info:
    filter_names: test_vm1

- name: Search with an invalid filter
  vcenter_vm_info:
    filter_names: test_vm1_does_not_exists
- name: Collect information about a specific VM
  vcenter_vm_info:
    vm: '{{ test_vm1.value[0].vm }}'

- name: Collect the list of the existing VM
  vcenter_vm_info:
  register: existing_vms
  until: existing_vms is not failed

"""

IN_QUERY_PARAMETER = [
    "filter.clusters",
    "filter.datacenters",
    "filter.folders",
    "filter.hosts",
    "filter.names",
    "filter.power_states",
    "filter.resource_pools",
    "filter.vms",
]

import socket
import json
from ansible.module_utils.basic import env_fallback

try:
    from ansible_collections.cloud.common.plugins.module_utils.turbo.module import (
        AnsibleTurboModule as AnsibleModule,
    )
except ImportError:
    from ansible.module_utils.basic import AnsibleModule
from ansible_collections.vmware.vmware_rest.plugins.module_utils.vmware_rest import (
    gen_args,
    open_session,
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
    }

    argument_spec["filter_clusters"] = {"type": "list", "elements": "str"}
    argument_spec["filter_datacenters"] = {"type": "list", "elements": "str"}
    argument_spec["filter_folders"] = {"type": "list", "elements": "str"}
    argument_spec["filter_hosts"] = {"type": "list", "elements": "str"}
    argument_spec["filter_names"] = {"type": "list", "elements": "str"}
    argument_spec["filter_power_states"] = {"type": "list", "elements": "str"}
    argument_spec["filter_resource_pools"] = {"type": "list", "elements": "str"}
    argument_spec["filter_vms"] = {"type": "list", "elements": "str"}
    argument_spec["vm"] = {"type": "str"}

    return argument_spec


async def get_device_info(params, session, _url, _key):
    async with session.get(_url + "/" + _key) as resp:
        _json = await resp.json()
        entry = _json["value"]
        entry["_key"] = _key
        return entry


async def list_devices(params, session):
    existing_entries = []
    _url = url(params)
    async with session.get(_url) as resp:
        _json = await resp.json()
        devices = _json["value"]
    for device in devices:
        _id = list(device.values())[0]
        existing_entries.append((await get_device_info(params, session, _url, _id)))
    return existing_entries


async def exists(params, session):
    unicity_keys = ["bus", "pci_slot_number"]
    devices = await list_devices(params, session)
    for device in devices:
        for k in unicity_keys:
            if params.get(k) is not None and device.get(k) != params.get(k):
                break
        else:
            return device


async def main():
    module_args = prepare_argument_spec()
    module = AnsibleModule(argument_spec=module_args, supports_check_mode=True)
    session = await open_session(
        vcenter_hostname=module.params["vcenter_hostname"],
        vcenter_username=module.params["vcenter_username"],
        vcenter_password=module.params["vcenter_password"],
    )
    result = await entry_point(module, session)
    module.exit_json(**result)


def url(params):

    if params["vm"]:
        return ("https://{vcenter_hostname}" "/rest/vcenter/vm/{vm}").format(
            **params
        ) + gen_args(params, IN_QUERY_PARAMETER)
    else:
        return ("https://{vcenter_hostname}" "/rest/vcenter/vm").format(
            **params
        ) + gen_args(params, IN_QUERY_PARAMETER)


async def entry_point(module, session):
    async with session.get(url(module.params)) as resp:
        _json = await resp.json()
        return await update_changed_flag(_json, resp.status, "get")


if __name__ == "__main__":
    import asyncio

    loop = asyncio.get_event_loop()
    loop.run_until_complete(main())
