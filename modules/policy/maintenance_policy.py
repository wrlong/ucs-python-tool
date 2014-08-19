#!/usr/bin/python

from UcsSdk import OrgOrg
from UcsSdk import LsmaintMaintPolicy


def create_maintenance_policy(
        handle,
        policy_desc,
        policy_name,
        blade_bundle_version="",
        rack_bundle_version=""):

    # handle.StartTransaction()

    obj = handle.GetManagedObject(
        None,
        OrgOrg.ClassId(),
        {OrgOrg.DN: "org-root"})

    handle.AddManagedObject(
        obj,
        LsmaintMaintPolicy.ClassId(),
        {LsmaintMaintPolicy.UPTIME_DISR: "user-ack",
         LsmaintMaintPolicy.SCHED_NAME: "",
         LsmaintMaintPolicy.DN: "org-root/maint-"+policy_name,
         LsmaintMaintPolicy.DESCR: policy_desc,
         LsmaintMaintPolicy.POLICY_OWNER: "local",
         LsmaintMaintPolicy.NAME: policy_name})

    # handle.CompleteTransaction()

    print "Created Maintenance Policy " + policy_name
