from __future__ import absolute_import, division, print_function

__metaclass__ = type

import logging

import pytest
import six

if six.PY3:
    from unittest import mock
else:
    import mock

from ansible.module_utils.connection import Connection
import ansible_collections.ansible.vmware_rest.plugins.module_utils.vmware_httpapi as vmware_httpapi
import ansible.module_utils.basic
from ansible_collections.ansible.vmware_rest.plugins.httpapi.vmware import (
    HttpApi,
)


class ConnectionLite(Connection):

    _url = "https://vcenter.test"
    _messages = []
    _auth = False

    def __init__(self, socket):
        pass


def test_get_url_with_filter(monkeypatch):
    argument_spec = vmware_httpapi.VmwareRestModule.create_argument_spec(
        use_filters=True
    )
    argument_spec.update(object_type=dict(type="str", default="datacenter"))

    def fake_load_params():
        return {"object_type": "vm", "filters": [{"names": "a"}]}

    monkeypatch.setattr(
        ansible.module_utils.basic, "_load_params", fake_load_params
    )
    monkeypatch.setattr(vmware_httpapi, "Connection", ConnectionLite)
    module = vmware_httpapi.VmwareRestModule(
        argument_spec=argument_spec,
        supports_check_mode=True,
        use_object_handler=True,
    )
    object_type = module.params["object_type"]

    url = module.get_url_with_filter(object_type)
    assert url == "/rest/vcenter/vm?filter.names=a"


def test_handle_default_generic(monkeypatch):
    monkeypatch.setattr(
        vmware_httpapi.VmwareRestModule,
        "__init__",
        mock.Mock(return_value=None),
    )
    monkeypatch.setattr(vmware_httpapi.VmwareRestModule, "fail", mock.Mock())
    m = vmware_httpapi.VmwareRestModule()
    m.response = {
        "data": {
            "localizableMessages": [
                {
                    "defaultMessage": "Not found.",
                    "id": "com.vmware.vapi.rest.httpNotFound",
                }
            ],
            "majorErrorCode": 404,
            "name": "com.vmware.vapi.rest.httpNotFound",
        },
        "status": 404,
    }
    m.handle_default_generic()
    m.fail.assert_called_once_with(msg="Not found.")
