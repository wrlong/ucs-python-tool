#!/usr/bin/python

from UcsSdk import OrgOrg
from UcsSdk import VnicLanConnTempl
from UcsSdk import VnicEtherIf
from UcsSdk import LsServer
from UcsSdk import LsVConAssign
from UcsSdk import LsPower
from UcsSdk import LsRequirement
from UcsSdk import VnicEther
from UcsSdk import VnicEtherIf
from UcsSdk import VnicFc
from UcsSdk import VnicFcIf
from UcsSdk import VnicFcNode

def create_sp_template(
        handle,
        obj,
        template_description,
        remove_file,
        sp_templ_name,
        boot_policy_name,
        uuid_pool_name,
        wwnn_pool_name,
        spt_vnic_templates,
        spt_vhba_templates,
        server_pool_name,
        firmware_policy_name="default",
        maintenance_policy_name="default",
        server_pool_qual_name="all-chassis",
        template_type="updating-template",
        power_policy_name="default",
        sp_power_state="admin-up"):

    try:
        mo = handle.AddManagedObject(
            obj,
            LsServer.ClassId(),
            {LsServer.EXT_IPPOOL_NAME:  "ext-mgmt",
             LsServer.BOOT_POLICY_NAME:  boot_policy_name,
             LsServer.TYPE:  template_type,
             LsServer.DYNAMIC_CON_POLICY_NAME:  "",
             LsServer.DESCR: template_description,
             LsServer.BIOS_PROFILE_NAME: "",
             LsServer.SRC_TEMPL_NAME: "",
             LsServer.EXT_IPSTATE: "pooled",
             LsServer.AGENT_POLICY_NAME: "",
             LsServer.LOCAL_DISK_POLICY_NAME: "default",
             LsServer.HOST_FW_POLICY_NAME: firmware_policy_name,
             LsServer.MGMT_FW_POLICY_NAME: "",
             LsServer.MGMT_ACCESS_POLICY_NAME: "",
             LsServer.UUID: "0",
             LsServer.DN: "org-root/ls-"+sp_templ_name,
             LsServer.MAINT_POLICY_NAME: maintenance_policy_name,
             LsServer.SCRUB_POLICY_NAME: "",
             LsServer.USR_LBL: "",
             LsServer.SOL_POLICY_NAME: "",
             LsServer.POWER_POLICY_NAME: power_policy_name,
             LsServer.VCON_PROFILE_NAME: "",
             LsServer.IDENT_POOL_NAME: uuid_pool_name,
             LsServer.POLICY_OWNER: "local",
             LsServer.NAME: sp_templ_name,
             LsServer.STATS_POLICY_NAME: "default"})

        adapter_count = 1

        for vnic in spt_vnic_templates.keys():

            mo_1 = handle.AddManagedObject(
                mo,
                LsVConAssign.ClassId(),
                {LsVConAssign.VNIC_NAME: vnic,
                 LsVConAssign.TRANSPORT: "ethernet",
                 LsVConAssign.ORDER: adapter_count,
                 LsVConAssign.ADMIN_VCON: "1",
                 LsVConAssign.DN: "org-root/ls-" + sp_templ_name +
                                  "/assign-ethernet-vnic-"+vnic},
                True)

            mo_3 = handle.AddManagedObject(
                mo,
                VnicEther.ClassId(),
                {VnicEther.DN: "org-root/ls-"+sp_templ_name+"/ether-"+vnic,
                 VnicEther.ORDER: adapter_count,
                 VnicEther.NAME: vnic,
                 VnicEther.ADMIN_VCON: "1",
                 VnicEther.NW_TEMPL_NAME: vnic})

        adapter_count += 1

        for vhba in spt_vhba_templates.keys():
            mo_2 = handle.AddManagedObject(
                mo,
                LsVConAssign.ClassId(),
                {LsVConAssign.VNIC_NAME: vhba,
                 LsVConAssign.TRANSPORT: "fc",
                 LsVConAssign.ORDER: adapter_count,
                 LsVConAssign.ADMIN_VCON: "2",
                 LsVConAssign.DN: "org-root/ls-" + sp_templ_name + \
                                  "/assign-fc-vnic-" + vhba},
                True)

            mo_4 = handle.AddManagedObject(
                mo,
                VnicFc.ClassId(),
                {VnicFc.ADMIN_VCON: "2",
                 VnicFc.NW_TEMPL_NAME: vhba,
                 VnicFc.ORDER: adapter_count,
                 VnicFc.MAX_DATA_FIELD_SIZE: "2048",
                 VnicFc.NAME: vhba,
                 VnicFc.DN: "org-root/ls-" + sp_templ_name + "/fc-" + vhba})

        adapter_count += 1

        # Add FC WWNN
        mo_wwnn = handle.AddManagedObject(
            mo,
            VnicFcNode.ClassId(),
            {VnicFcNode.ADDR: "pool-derived",
             VnicFcNode.DN: "org-root/ls-" + sp_templ_name + "/fc-node",
             VnicFcNode.IDENT_POOL_NAME: wwnn_pool_name},
            True)

        # Add Server Pool
        mo_svr_pool = handle.AddManagedObject(
            mo,
            LsRequirement.ClassId(),
            {LsRequirement.NAME: server_pool_name,
             LsRequirement.RESTRICT_MIGRATION: "no",
             LsRequirement.DN: "org-root/ls-" + sp_templ_name + "/pn-req",
             LsRequirement.QUALIFIER: server_pool_qual_name},
            True)

        # Add Power State
        mo_power = handle.AddManagedObject(
            mo,
            LsPower.ClassId(),
            {LsPower.DN: "org-root/ls-" + sp_templ_name + "/power",
             LsPower.STATE: sp_power_state},
            True)

        print "Created Service Profile Template " + sp_templ_name

    except CreateSpTemplateError:
        print("Error: Unable to create SP template " + sp_templ_name)
