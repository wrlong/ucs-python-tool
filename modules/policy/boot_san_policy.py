#!/usr/bin/python

from UcsSdk import OrgOrg
from UcsSdk import LsbootPolicy
from UcsSdk import LsbootVirtualMedia
from UcsSdk import LsbootStorage
from UcsSdk import LsbootSanImage
from UcsSdk import LsbootSanImagePath

def create_boot_san_policy(
    handle,
    obj,
    policy_desc,
    policy_name,
    vhba_a_name,
    target_a_vhba_a,
    vhba_b_name,
    target_b_vhba_b):

    try:
        mo = handle.AddManagedObject(
            obj,
            LsbootPolicy.ClassId(),
            {LsbootPolicy.POLICY_OWNER: "local",
             LsbootPolicy.REBOOT_ON_UPDATE: "no",
             LsbootPolicy.NAME: policy_name,
             LsbootPolicy.ENFORCE_VNIC_NAME: "yes",
             LsbootPolicy.DN: "org-root/boot-policy-" + policy_name,
             LsbootPolicy.DESCR: policy_desc})

        mo_1 = handle.AddManagedObject(
            mo,
            LsbootVirtualMedia.ClassId(),
            {LsbootVirtualMedia.DN: "org-root/boot-policy-" + \
                                    policy_name + "/read-only-vm",
             LsbootVirtualMedia.ACCESS: "read-only",
             LsbootVirtualMedia.ORDER: "1"})

        mo_2 = handle.AddManagedObject(
            mo,
            LsbootStorage.ClassId(),
            {LsbootStorage.DN: "org-root/boot-policy-" + \
                               policy_name + "/storage",
             LsbootStorage.ORDER: "2"},
            True)

        mo_2_1 = handle.AddManagedObject(
            mo_2,
            LsbootSanImage.ClassId(),
            {LsbootSanImage.VNIC_NAME: vhba_a_name,
             LsbootSanImage.DN: "org-root/boot-policy-" + \
                                policy_name + "/storage/san-primary",
             LsbootSanImage.TYPE: "primary"})

        mo_2_1_1 = handle.AddManagedObject(
            mo_2_1,
            LsbootSanImagePath.ClassId(),
            {LsbootSanImagePath.TYPE: "primary",
             LsbootSanImagePath.DN: "org-root/boot-policy-" + \
                                    policy_name + \
                                    "/storage/san-primary/path-primary",
             LsbootSanImagePath.LUN: "0",
             LsbootSanImagePath.WWN: target_a_vhba_a})

        mo_2_2 = handle.AddManagedObject(
            mo_2,
            LsbootSanImage.ClassId(),
            {LsbootSanImage.VNIC_NAME: vhba_b_name,
             LsbootSanImage.DN: "org-root/boot-policy-" + \
                                policy_name + "/storage/san-secondary",
             LsbootSanImage.TYPE: "secondary"})

        mo_2_2_1 = handle.AddManagedObject(
            mo_2_2,
            LsbootSanImagePath.ClassId(),
            {LsbootSanImagePath.TYPE: "primary",
             LsbootSanImagePath.DN: "org-root/boot-policy-" + \
                                    policy_name + \
                                    "/storage/san-secondary/path-primary",
             LsbootSanImagePath.LUN: "0",
             LsbootSanImagePath.WWN: target_b_vhba_b})

        print "Created Boot from SAN Policy " + policy_name + \
              " with primary target " + target_a_vhba_a

    except CreateBootFromSanPolicyError:
        print("Error: Unable to create boot from SAN policy " + policy_name)
