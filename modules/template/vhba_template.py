#!/usr/bin/python

from UcsSdk import OrgOrg
from UcsSdk import VnicSanConnTempl
from UcsSdk import VnicFcIf


def create_vhba_template(
        handle,
        obj,
        vhba_templ_desc,
        vhba_templ_name,
        wwpn_pool_name,
        vhba_vsan_list,
        templ_type="updating-template",
        vhba_switch_id="A"):

    vhba_templ_name_mod = "org-root/san-conn-templ-" + vhba_templ_name

    # handle.StartTransaction()
    '''
    obj = handle.GetManagedObject(
        None,
        OrgOrg.ClassId(),
        {OrgOrg.DN: "org-root"})
    '''
    mo = handle.AddManagedObject(
        obj,
        VnicSanConnTempl.ClassId(),
        {VnicSanConnTempl.DESCR: vhba_templ_desc,
         VnicSanConnTempl.IDENT_POOL_NAME: wwpn_pool_name,
         VnicSanConnTempl.NAME: vhba_templ_name,
         VnicSanConnTempl.TEMPL_TYPE: templ_type,
         VnicSanConnTempl.DN: vhba_templ_name_mod,
         VnicSanConnTempl.SWITCH_ID: vhba_switch_id,
         VnicSanConnTempl.POLICY_OWNER: "local",
         VnicSanConnTempl.PIN_TO_GROUP_NAME: "",
         VnicSanConnTempl.STATS_POLICY_NAME: "default"})

    for vhba_vsan_name in vhba_vsan_list:
        fc_if_dn = "org-root/san-conn-templ-" + vhba_templ_name + \
                   "/if-default"
        mo_1 = handle.AddManagedObject(
            mo,
            VnicFcIf.ClassId(),
            {VnicFcIf.NAME: vhba_vsan_name,
             VnicFcIf.DN: fc_if_dn},
            True)

    # handle.CompleteTransaction()

    print "Created vHBA template " + vhba_templ_name + \
          " with wwpn pool " + wwpn_pool_name
