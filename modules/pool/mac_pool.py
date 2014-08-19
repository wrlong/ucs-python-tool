#!/usr/bin/python

from UcsSdk import OrgOrg
from UcsSdk import MacpoolPool
from UcsSdk import MacpoolBlock


def create_mac_pool(handle, obj, pool_desc, pool_name, pool_range):
    start_range = pool_range.split("-")[0]
    end_range = pool_range.split("-")[1]

    # handle.StartTransaction()

    #obj = handle.GetManagedObject(
    #    None,
    #    OrgOrg.ClassId(),
    #    {OrgOrg.DN: "org-root"})

    mo = handle.AddManagedObject(
        obj,
        MacpoolPool.ClassId(),
        {MacpoolPool.NAME: pool_name,
         MacpoolPool.POLICY_OWNER: "local",
         MacpoolPool.DESCR: pool_desc,
         MacpoolPool.DN: "org-root/mac-pool-"+pool_name,
         MacpoolPool.ASSIGNMENT_ORDER: "sequential"})

    mo_1 = handle.AddManagedObject(
        mo,
        MacpoolBlock.ClassId(),
        {MacpoolBlock.FROM: start_range,
         MacpoolBlock.TO: end_range,
         MacpoolBlock.DN: "org-root/mac-pool-"+pool_name+"/block-"+pool_range})

    # handle.CompleteTransaction()

    print "Created MAC pool " + pool_name + \
        " with range " + start_range + " to " + end_range
