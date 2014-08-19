#!/usr/bin/python
from UcsSdk import FabricLanCloud
from UcsSdk import FabricVlan


def create_vlan(handle, vlan, vlan_name):
    fab_vlan_dn = "fabric/lan/net-"+vlan_name

    obj = handle.GetManagedObject(
        None,
        FabricLanCloud.ClassId(),
        {FabricLanCloud.DN: "fabric/lan"})

    handle.AddManagedObject(
        obj,
        FabricVlan.ClassId(),
        {FabricVlan.COMPRESSION_TYPE: "included",
         FabricVlan.DN: fab_vlan_dn,
         FabricVlan.SHARING: "none",
         FabricVlan.PUB_NW_NAME: "",
         "policyOwner": "local",
         FabricVlan.ID: vlan,
         FabricVlan.MCAST_POLICY_NAME: "",
         FabricVlan.NAME: vlan_name,
         FabricVlan.DEFAULT_NET: "no"})

    print "Created VLAN " + vlan_name + " with id " + vlan
