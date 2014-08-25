#!/usr/bin/python

from UcsSdk import OrgOrg
from UcsSdk import FcpoolInitiators
from UcsSdk import FcpoolBlock

def create_wwpn_pool(handle, obj, pool_desc, pool_name, pool_range):
    try:
        start_range = pool_range.split("-")[0]
        end_range = pool_range.split("-")[1]

        mo = handle.AddManagedObject(
            obj,
            FcpoolInitiators.ClassId(),
            {FcpoolInitiators.NAME: pool_name,
             FcpoolInitiators.POLICY_OWNER: "local",
             FcpoolInitiators.DESCR: pool_desc,
             FcpoolInitiators.DN: "org-root/wwn-pool-" + pool_name,
             FcpoolInitiators.PURPOSE: "port-wwn-assignment",
             FcpoolInitiators.ASSIGNMENT_ORDER: "sequential"})

        mo_1 = handle.AddManagedObject(
            mo,
            FcpoolBlock.ClassId(),
            {FcpoolBlock.FROM: start_range,
             FcpoolBlock.TO: end_range,
             FcpoolBlock.DN: "org-root/wwn-pool-" + pool_name +
                             "/block-" + pool_range})

        print "Created WWPN pool " + pool_name + \
              " with range " + start_range + " to " + end_range

    except CreateWwpnPoolError:
        print("Error: Unable to create WWPN pool " + pool_name)
