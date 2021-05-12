.. _vmware_rest_appliance_health:

*******************************************
Get the health state of the VCSA components
*******************************************

Introduction
============

The collection provides several modules that you can use to know the state of the different components of the VCSA.

Scenario requirements
=====================

You've got an up and running vCenter Server Appliance.


Health state per component
--------------------------

The database:

.. ansible-task::

  - name: Get the database heath status
    vmware.vmware_rest.appliance_health_database_info:

The database storage:

.. ansible-task::

  - name: Get the database storage heath status
    vmware.vmware_rest.appliance_health_databasestorage_info:

The system load:

.. ansible-task::

  - name: Get the system load status
    vmware.vmware_rest.appliance_health_load_info:

The memory usage:

.. ansible-task::

  - name: Get the system mem status
    vmware.vmware_rest.appliance_health_mem_info:


The system status:

.. ansible-task::

  - name: Get the system health status
    vmware.vmware_rest.appliance_health_system_info:

The package manager:

.. ansible-task::

  - name: Get the health of the software package manager
    vmware.vmware_rest.appliance_health_softwarepackages_info:

The storage system:

.. ansible-task::

  - name: Get the health of the storage system
    vmware.vmware_rest.appliance_health_storage_info:

The swap usage:

.. ansible-task::

  - name: Get the health of the swap
    vmware.vmware_rest.appliance_health_swap_info::
