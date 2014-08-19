#!/usr/bin/python

from UcsSdk import OrgOrg
from UcsSdk import VnicLanConnTempl
from UcsSdk import VnicEtherIf


def create_vnic_template(
        handle,
        obj,
        vnic_templ_desc,
        vnic_templ_name,
        mac_pool_name,
        vnic_vlan_list,
        templ_type="updating-template",
        vnic_mtu="9000",
        vnic_qos_pol="qos-1",
        vnic_switch_id="A",
        vnic_nw_ctrl_pol="default"):

    vnic_templ_name_mod = "org-root/lan-conn-templ-" + vnic_templ_name

    # handle.StartTransaction()
    '''
    obj = handle.GetManagedObject(
        None,
        OrgOrg.ClassId(),
        {OrgOrg.DN: "org-root"})
    '''
    mo = handle.AddManagedObject(
        obj,
        VnicLanConnTempl.ClassId(),
        {VnicLanConnTempl.QOS_POLICY_NAME: vnic_qos_pol,
         VnicLanConnTempl.MTU: vnic_mtu,
         VnicLanConnTempl.DESCR: vnic_templ_desc,
         VnicLanConnTempl.IDENT_POOL_NAME: mac_pool_name,
         VnicLanConnTempl.NAME: vnic_templ_name,
         VnicLanConnTempl.TEMPL_TYPE: templ_type,
         VnicLanConnTempl.DN: vnic_templ_name_mod,
         VnicLanConnTempl.SWITCH_ID: vnic_switch_id,
         VnicLanConnTempl.POLICY_OWNER: "local",
         VnicLanConnTempl.NW_CTRL_POLICY_NAME: vnic_nw_ctrl_pol,
         VnicLanConnTempl.PIN_TO_GROUP_NAME: "",
         VnicLanConnTempl.STATS_POLICY_NAME: "default"})

    for vnic_vlan_name in vnic_vlan_list:
        eth_if_dn = "org-root/lan-conn-templ-" + vnic_templ_name + \
                    "/if-" + vnic_vlan_name
        mo_1 = handle.AddManagedObject(
            mo,
            VnicEtherIf.ClassId(),
            {VnicEtherIf.DN: eth_if_dn,
             VnicEtherIf.NAME: vnic_vlan_name,
             VnicEtherIf.DEFAULT_NET: "no"},
            True)

    eth_def_dn = "org-root/lan-conn-templ-" + vnic_templ_name + \
                 "/if-default"
    mo_2 = handle.AddManagedObject(
        mo,
        VnicEtherIf.ClassId(),
        {VnicEtherIf.DN: eth_def_dn,
         VnicEtherIf.NAME: "default",
         VnicEtherIf.DEFAULT_NET: "no"},
        True)

    # handle.CompleteTransaction()

    print "Created vNIC template " + vnic_templ_name + \
          " with mac pool " + mac_pool_name
