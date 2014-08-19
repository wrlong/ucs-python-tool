#!/usr/bin/python

from UcsSdk import OrgOrg
from UcsSdk import FirmwareComputeHostPack


def create_fw_policy(
        handle,
        obj,
        policy_desc,
        policy_name,
        blade_bundle_version="",
        rack_bundle_version=""):

    # handle.StartTransaction()
    '''
    obj = handle.GetManagedObject(
        None,
        OrgOrg.ClassId(),
        {OrgOrg.DN: "org-root"})
    '''
    handle.AddManagedObject(
        obj,
        FirmwareComputeHostPack.ClassId(),
        {FirmwareComputeHostPack.BLADE_BUNDLE_VERSION: blade_bundle_version,
         FirmwareComputeHostPack.DN: "org-root/fw-host-pack-" + policy_name,
         FirmwareComputeHostPack.MODE: "staged",
         FirmwareComputeHostPack.UPDATE_TRIGGER: "immediate",
         FirmwareComputeHostPack.NAME: policy_name,
         FirmwareComputeHostPack.STAGE_SIZE: "0",
         FirmwareComputeHostPack.IGNORE_COMP_CHECK: "yes",
         FirmwareComputeHostPack.POLICY_OWNER: "local",
         FirmwareComputeHostPack.DESCR: policy_desc,
         FirmwareComputeHostPack.RACK_BUNDLE_VERSION: rack_bundle_version})

    # handle.CompleteTransaction()

    print "Created Firmware Policy " + policy_name
