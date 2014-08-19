#!/usr/bin/python

from UcsSdk import OrgOrg
from UcsSdk import UuidpoolPool
from UcsSdk import UuidpoolBlock


def create_uuid_pool(handle, obj, pool_desc, pool_name, pool_range):
    start_range = pool_range.split("=")[0]
    end_range = pool_range.split("=")[1]

    # handle.StartTransaction()
    '''
    obj = handle.GetManagedObject(
        None,
        OrgOrg.ClassId(),
        {OrgOrg.DN: "org-root"})
    '''
    mo = handle.AddManagedObject(
        obj,
        UuidpoolPool.ClassId(),
        {UuidpoolPool.NAME: pool_name,
         UuidpoolPool.DESCR: pool_desc,
         UuidpoolPool.PREFIX: "derived",
         UuidpoolPool.DN: "org-root/uuid-pool-" + pool_name,
         UuidpoolPool.ASSIGNMENT_ORDER: "sequential",
         UuidpoolPool.POLICY_OWNER: "local"})

    mo_1 = handle.AddManagedObject(
        mo,
        UuidpoolBlock.ClassId(),
        {UuidpoolBlock.FROM: start_range,
         UuidpoolBlock.TO: end_range,
         UuidpoolBlock.DN: "org-root/uuid-pool-" + pool_name +
                           "/block-from-" + start_range +
                           "-to-" + end_range})

    # handle.CompleteTransaction()

    print "Created UUID pool " + pool_name + \
          " with range " + start_range + " to " + end_range
