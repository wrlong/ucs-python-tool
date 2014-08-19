#!/usr/bin/python

from UcsSdk import OrgOrg
from UcsSdk import LsbootPolicy
from UcsSdk import LsbootLan
from UcsSdk import LsbootLanImagePath


def create_lan_boot_policy(handle, policy_name, vnic_name):
    policy_desc = "Created by Python"

    # handle.StartTransaction()

    obj = handle.GetManagedObject(
        None,
        OrgOrg.ClassId(),
        {OrgOrg.DN: "org-root"})

    mo = handle.AddManagedObject(
        obj,
        LsbootPolicy.ClassId(),
        {LsbootPolicy.POLICY_OWNER: "local",
         LsbootPolicy.REBOOT_ON_UPDATE: "yes",
         LsbootPolicy.NAME: policy_name,
         LsbootPolicy.ENFORCE_VNIC_NAME: "yes",
         LsbootPolicy.DN: "org-root/boot-policy-" + policy_name,
         LsbootPolicy.DESCR: policy_desc})

    mo_1 = handle.AddManagedObject(
        mo,
        LsbootLan.ClassId(),
        {LsbootLan.ORDER: "1"})

    mo_1_1 = handle.AddManagedObject(
        mo_1,
        LsbootLanImagePath.ClassId(),
        {LsbootLanImagePath.TYPE: "primary",
         LsbootLanImagePath.VNIC_NAME: vnic_name})

    # handle.CompleteTransaction()

    print "Created Boot from LAN Policy " + policy_name + \
          " with primary vNIC " + vnic_name
