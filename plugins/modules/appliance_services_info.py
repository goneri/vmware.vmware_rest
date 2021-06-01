#!/usr/bin/python
# -*- coding: utf-8 -*-
# Copyright: (c) 2021, Ansible Project
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
# template: header.j2
# This module is autogenerated by vmware_rest_code_generator.
# See: https://github.com/ansible-collections/vmware_rest_code_generator
from __future__ import absolute_import, division, print_function

__metaclass__ = type


DOCUMENTATION = r"""
module: appliance_services_info
short_description: Returns the state of a service.
description: Returns the state of a service.
options:
  service:
    description:
    - identifier of the service whose state is being queried. Required with I(state=['get'])
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
version_added: 2.0.0
requirements:
- vSphere 7.0.2 or greater
- python >= 3.6
- aiohttp
"""

EXAMPLES = r"""
- name: List all the services
  vmware.vmware_rest.appliance_services_info:
  register: result

- name: Get information about ntpd
  vmware.vmware_rest.appliance_services_info:
    service: ntpd
  register: result
"""

RETURN = r"""
# content generated by the update_return_section callback# task: List all the services
value:
  description: List all the services
  returned: On success
  sample:
    appliance-shutdown:
      description: /etc/rc.local.shutdown Compatibility
      state: STOPPED
    atftpd:
      description: The tftp server serves files using the trivial file transfer protocol.
      state: STOPPED
    auditd:
      description: Security Auditing Service
      state: STOPPED
    cloud-config:
      description: Apply the settings specified in cloud-config
      state: STARTED
    cloud-init:
      description: Initial cloud-init job (metadata service crawler)
      state: STARTED
    cloud-init-local:
      description: Initial cloud-init job (pre-networking)
      state: STARTED
    crond:
      description: Command Scheduler
      state: STARTED
    dbus:
      description: D-Bus System Message Bus
      state: STARTED
    dm-event:
      description: Device-mapper event daemon
      state: STOPPED
    dnsmasq:
      description: A lightweight, caching DNS proxy
      state: STARTED
    dracut-cmdline:
      description: dracut cmdline hook
      state: STOPPED
    dracut-initqueue:
      description: dracut initqueue hook
      state: STOPPED
    dracut-mount:
      description: dracut mount hook
      state: STOPPED
    dracut-pre-mount:
      description: dracut pre-mount hook
      state: STOPPED
    dracut-pre-pivot:
      description: dracut pre-pivot and cleanup hook
      state: STOPPED
    dracut-pre-trigger:
      description: dracut pre-trigger hook
      state: STOPPED
    dracut-pre-udev:
      description: dracut pre-udev hook
      state: STOPPED
    dracut-shutdown:
      description: Restore /run/initramfs on shutdown
      state: STARTED
    emergency:
      description: Emergency Shell
      state: STOPPED
    getty@tty2:
      description: DCUI
      state: STARTED
    haveged:
      description: Entropy Daemon based on the HAVEGE algorithm
      state: STARTED
    initrd-cleanup:
      description: Cleaning Up and Shutting Down Daemons
      state: STOPPED
    initrd-parse-etc:
      description: Reload Configuration from the Real Root
      state: STOPPED
    initrd-switch-root:
      description: Switch Root
      state: STOPPED
    initrd-udevadm-cleanup-db:
      description: Cleanup udevd DB
      state: STOPPED
    irqbalance:
      description: irqbalance daemon
      state: STARTED
    kmod-static-nodes:
      description: Create list of required static device nodes for the current kernel
      state: STARTED
    lsassd:
      description: Likewise Security and Authentication Subsystem
      state: STARTED
    lvm2-activate:
      description: LVM2 activate volume groups
      state: STARTED
    lvm2-lvmetad:
      description: LVM2 metadata daemon
      state: STARTED
    lvm2-pvscan@253:2:
      description: LVM2 PV scan on device 253:2
      state: STARTED
    lvm2-pvscan@253:4:
      description: LVM2 PV scan on device 253:4
      state: STARTED
    lwsmd:
      description: Likewise Service Control Manager Service
      state: STARTED
    ntpd:
      description: Network Time Service
      state: STARTED
    observability:
      description: VMware Observability Service
      state: STARTED
    rc-local:
      description: /etc/rc.d/rc.local Compatibility
      state: STARTED
    rescue:
      description: Rescue Shell
      state: STOPPED
    rsyslog:
      description: System Logging Service
      state: STARTED
    sendmail:
      description: Sendmail Mail Transport Agent
      state: STARTED
    sshd:
      description: OpenSSH Daemon
      state: STARTED
    sshd-keygen:
      description: Generate sshd host keys
      state: STOPPED
    syslog-ng:
      description: System Logger Daemon
      state: STOPPED
    sysstat:
      description: Resets System Activity Logs
      state: STARTED
    sysstat-collect:
      description: system activity accounting tool
      state: STOPPED
    sysstat-summary:
      description: Generate a daily summary of process accounting
      state: STOPPED
    systemd-ask-password-console:
      description: Dispatch Password Requests to Console
      state: STOPPED
    systemd-ask-password-wall:
      description: Forward Password Requests to Wall
      state: STOPPED
    systemd-binfmt:
      description: Set Up Additional Binary Formats
      state: STOPPED
    systemd-fsck-root:
      description: File System Check on Root Device
      state: STARTED
    systemd-hwdb-update:
      description: Rebuild Hardware Database
      state: STARTED
    systemd-initctl:
      description: initctl Compatibility Daemon
      state: STOPPED
    systemd-journal-catalog-update:
      description: Rebuild Journal Catalog
      state: STARTED
    systemd-journal-flush:
      description: Flush Journal to Persistent Storage
      state: STARTED
    systemd-journald:
      description: Journal Service
      state: STARTED
    systemd-logind:
      description: Login Service
      state: STARTED
    systemd-machine-id-commit:
      description: Commit a transient machine-id on disk
      state: STOPPED
    systemd-modules-load:
      description: Load Kernel Modules
      state: STARTED
    systemd-networkd:
      description: Network Service
      state: STARTED
    systemd-networkd-wait-online:
      description: Wait for Network to be Configured
      state: STARTED
    systemd-quotacheck:
      description: File System Quota Check
      state: STOPPED
    systemd-random-seed:
      description: Load/Save Random Seed
      state: STARTED
    systemd-remount-fs:
      description: Remount Root and Kernel File Systems
      state: STARTED
    systemd-resolved:
      description: Network Name Resolution
      state: STARTED
    systemd-sysctl:
      description: Apply Kernel Variables
      state: STARTED
    systemd-tmpfiles-clean:
      description: Cleanup of Temporary Directories
      state: STOPPED
    systemd-tmpfiles-setup:
      description: Create Volatile Files and Directories
      state: STARTED
    systemd-tmpfiles-setup-dev:
      description: Create Static Device Nodes in /dev
      state: STARTED
    systemd-udev-trigger:
      description: udev Coldplug all Devices
      state: STARTED
    systemd-udevd:
      description: udev Kernel Device Manager
      state: STARTED
    systemd-update-done:
      description: Update is Completed
      state: STARTED
    systemd-update-utmp:
      description: Update UTMP about System Boot/Shutdown
      state: STARTED
    systemd-update-utmp-runlevel:
      description: Update UTMP about System Runlevel Changes
      state: STOPPED
    systemd-user-sessions:
      description: Permit User Sessions
      state: STARTED
    systemd-vconsole-setup:
      description: Setup Virtual Console
      state: STOPPED
    vami-lighttp:
      description: vami-lighttp.service
      state: STARTED
    vgauthd:
      description: VGAuth Service for open-vm-tools
      state: STOPPED
    vmafdd:
      description: 'LSB: Authentication Framework Daemon'
      state: STARTED
    vmcad:
      description: 'LSB: Start and Stop vmca'
      state: STARTED
    vmdird:
      description: 'LSB: Start and Stop vmdir'
      state: STARTED
    vmtoolsd:
      description: Service for virtual machines hosted on VMware
      state: STOPPED
    vmware-firewall:
      description: VMware Firewall service
      state: STARTED
    vmware-pod:
      description: VMware Pod Service.
      state: STARTED
    vmware-vdtc:
      description: VMware vSphere Distrubuted Tracing Collector
      state: STARTED
    vmware-vmon:
      description: VMware Service Lifecycle Manager
      state: STARTED
  type: dict
"""

# This structure describes the format of the data expected by the end-points
PAYLOAD_FORMAT = {
    "get": {"query": {}, "body": {}, "path": {"service": "service"}},
    "list": {"query": {}, "body": {}, "path": {}},
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

    argument_spec["service"] = {"type": "str"}

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
    if params.get("service"):
        _in_query_parameters = PAYLOAD_FORMAT["get"]["query"].keys()
        return (
            ("https://{vcenter_hostname}" "/api/appliance/services/").format(**params)
            + params["service"]
            + gen_args(params, _in_query_parameters)
        )
    _in_query_parameters = PAYLOAD_FORMAT["list"]["query"].keys()
    return ("https://{vcenter_hostname}" "/api/appliance/services").format(
        **params
    ) + gen_args(params, _in_query_parameters)


async def entry_point(module, session):
    url = build_url(module.params)
    async with session.get(url) as resp:
        _json = await resp.json()

        if "value" not in _json:  # 7.0.2+
            _json = {"value": _json}

        if module.params.get("service"):
            _json["id"] = module.params.get("service")
        elif module.params.get("label"):  # TODO extend the list of filter
            _json = await exists(module.params, session, url)
        else:  # list context, retrieve the details of each entry
            try:
                if (
                    isinstance(_json["value"][0]["service"], str)
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
