#!/usr/bin/python

from UcsSdk import OrgOrg
from UcsSdk import ComputePool
from UcsSdk import ComputePooledSlot
from UcsSdk import UuidpoolBlock

def create_server_pool(
        handle,
        obj,
        pool_desc,
        pool_name,
        pool_range):

    try:
        chassis_range = pool_range['chassis']
        slot_range = pool_range['slots']

        mo = handle.AddManagedObject(
            obj,
            ComputePool.ClassId(),
            {ComputePool.NAME: pool_name,
             ComputePool.POLICY_OWNER: "local",
             ComputePool.DESCR: pool_desc,
             ComputePool.DN: "org-root/compute-pool-" + pool_name})

        for cur_chassis in chassis_range.split(","):
            for cur_slot in slot_range.split(","):
                mo_x = handle.AddManagedObject(
                    mo,
                    ComputePooledSlot.ClassId(),
                    {ComputePooledSlot.SLOT_ID: cur_slot,
                     ComputePooledSlot.DN: "org-root/compute-pool-" + \
                                           pool_name + "/blade-" + \
                                           cur_chassis + "-" + cur_slot,
                     ComputePooledSlot.CHASSIS_ID: cur_chassis},
                    True)


        print "Created Server Pool " + pool_name

    except CreateServerPoolError:
        print("Error: Unable to create server pool " + pool_name)
