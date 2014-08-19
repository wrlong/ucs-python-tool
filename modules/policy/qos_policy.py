#!/usr/bin/python

from UcsSdk import OrgOrg
from UcsSdk import EpqosDefinition
from UcsSdk import EpqosEgress


def create_qos_policy(
        handle,
        obj,
        policy_desc,
        policy_name,
        priority,
        rate,
        burst,
        host_control):

    # handle.StartTransaction()
    '''
    obj = handle.GetManagedObject(
        None,
        OrgOrg.ClassId(),
        {OrgOrg.DN: "org-root"})
    '''
    mo = handle.AddManagedObject(
        obj,
        EpqosDefinition.ClassId(),
        {EpqosDefinition.DN: "org-root/ep-qos-" + policy_name,
         EpqosDefinition.DESCR: policy_desc,
         EpqosDefinition.NAME: policy_name,
         EpqosDefinition.POLICY_OWNER: "local"})

    mo_1 = handle.AddManagedObject(
        mo,
        EpqosEgress.ClassId(),
        {EpqosEgress.PRIO: priority,
         EpqosEgress.HOST_CONTROL: host_control,
         EpqosEgress.RATE: rate,
         EpqosEgress.NAME: "",
         EpqosEgress.DN: "org-root/ep-qos-" + policy_name + "/egress",
         EpqosEgress.BURST: burst},
        True)

    # handle.CompleteTransaction()

    print "Created QoS Policy " + policy_name + " with priority " + priority
