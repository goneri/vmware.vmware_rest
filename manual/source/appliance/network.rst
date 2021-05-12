.. _vmware_rest_appliance_network:

*****************
Network managment
*****************

IP configuration
================

You can also use Ansible to get and configure the network stack of the VCSA.

Global network information
--------------------------

The appliance_networking_info exposes the state of the global network configuration:

.. ansible-task::

  - name: Get network information
    vmware.vmware_rest.appliance_networking_info:

And you can adjust the parameters with the appliance_networking module.
    
.. ansible-task::

  - name: Set network information
    vmware.vmware_rest.appliance_networking:
      ipv6_enabled: False

Network Interface configuration
-------------------------------

The appliance_networking_interfaces_info returns a list of the Network Interface of the system:

.. ansible-task::

  - name: Get a list of the network interfaces
    vmware.vmware_rest.appliance_networking_interfaces_info:

You can also use the ``interface_name`` parameter to just focus on one single entry:
    
.. ansible-task::

  - name: Get details about one network interfaces
    vmware.vmware_rest.appliance_networking_interfaces_info:
      interface_name: nic0

DNS configuration
=================

The VCSA search domain configuration
------------------------------------


The search domain configuration can be done with appliance_networking_dns_domains and appliance_networking_dns_domains_info. The second module returns a list of domains:

.. ansible-task::

  - name: Get DNS domains configuration
    vmware.vmware_rest.appliance_networking_dns_domains_info:

There is two way to set the search domain. By default the value you pass in ``domains`` will overwrite the existing domain: 
  
.. ansible-task::

  - name: Update the domain configuration
    vmware.vmware_rest.appliance_networking_dns_domains:
      domains:
        - foobar

If you instead use the ``state=add`` parameter, the ``domain`` value will complet the existing list of domains.
        
.. ansible-task::

  - name: Add another domain configuration
    vmware.vmware_rest.appliance_networking_dns_domains:
      domain: barfoo
      state: add
