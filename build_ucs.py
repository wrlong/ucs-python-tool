#!/usr/bin/python

import simplejson as json
import getopt
from UcsSdk import *
from modules.fabric import vlan
from modules.pool import mac_pool
from modules.pool import uuid_pool
from modules.pool import server_pool
from modules.pool import wwnn_pool
from modules.pool import wwpn_pool
from modules.template import vnic_template
from modules.template import vhba_template
from modules.template import sp_template
from modules.policy import qos_policy
from modules.policy import firmware_policy
from modules.policy import maintenance_policy
from modules.policy import boot_lan_policy
from modules.policy import boot_san_policy
from modules.utilities import utilities
from modules.utilities import login

if __name__ == '__main__':

    time_start = utilities.current_time()
    remove_script_file = "remove_script_" + utilities.timestamp_str()
    file_out = open(remove_script_file, 'w')
    desc_string = utilities.unique_description()

    #invoking_user = getpass.getuser()
    #desc_string = utilities.unique_description()
    #print desc_string

    try:
        myopts, args = getopt.getopt(sys.argv[1:], "c:i:u:p:", ["config_file=","ip=","user=","pw="])
    except getopt.GetoptError:
        print("Usage: %s --ip <ip> --user <user_name> --pw <password> --config_file <config_file>" % sys.argv[0])

    for o, a in myopts:
        if o in ("-i", "--ip"):
            ucsm_ip = a
        elif o in ("-u", "--user"):
            ucsm_user = a
        elif o in ("-p", "--pw"):
            ucsm_pass = a
        elif o in ("-c", "--config_file"):
            config_file = a
        else:
            print("Usage: %s --ip <ip> --user <user_name> --pw <password> --config_file <config_file>" % sys.argv[0])

    try:
        json_config_data = open(config_file)
        SPTemplates = json.load(json_config_data)
    except JsonLoadException:
        print("Error: Error loading JSON file for import")

    # Login to UCSM
    handle = login.ucs_login(ucsm_ip, ucsm_user, ucsm_pass)
    obj = handle.GetManagedObject(None,OrgOrg.ClassId(),{OrgOrg.DN:"org-root"})


    for spt in SPTemplates.keys():
        # Collect pools policies and templates

        handle.StartTransaction()

        spt_policies = SPTemplates[spt]['policies']
        spt_pools = SPTemplates[spt]['pools']
        spt_templates = SPTemplates[spt]['templates']
        sp_instances = SPTemplates[spt]['service_profiles']

        # Create vnic templates and mac pools, network policies, etc.
        spt_vnic_templates = spt_templates['vnic']

        for vnic in spt_vnic_templates.keys():
            mac_pool_name = spt_vnic_templates[vnic]['macpool']['name']
            mac_pool_range = spt_vnic_templates[vnic]['macpool']['range']
            mac_pool.create_mac_pool(
                handle,
                obj,
                desc_string,
                mac_pool_name,
                mac_pool_range)
            utilities.add_to_remove_script(
                file_out,
                "org-root/mac-pool-"+mac_pool_name,
                "MacpoolPool")
            qos_policy.create_qos_policy(
                handle,
                obj,
                desc_string,
                spt_vnic_templates[vnic]['qos_policy']['name'],
                "bronze",
                "line-rate",
                "10240",
                "none")
            utilities.add_to_remove_script(
                file_out,
                "org-root/ep-qos-"+spt_vnic_templates[vnic]['qos_policy']['name'],
                "EpqosDefinition")
            vnic_template.create_vnic_template(
                handle,
                obj,
                desc_string,
                vnic,
                spt_vnic_templates[vnic]['macpool']['name'],
                #vnic,
                spt_vnic_templates[vnic]['vlans'],
                spt_vnic_templates[vnic]['template_type'],
                spt_vnic_templates[vnic]['mtu'],
                spt_vnic_templates[vnic]['qos_policy']['name'],
                spt_vnic_templates[vnic]['switch_id'],
                spt_vnic_templates[vnic]['network_policy'])
            utilities.add_to_remove_script(
                file_out,
                "org-root/lan-conn-templ-"+vnic,
                "VnicLanConnTempl")

        # Create vhba templates and wwpn pools
        spt_vhba_templates = spt_templates['vhba']

        for vhba in spt_vhba_templates.keys():
            wwpn_pool.create_wwpn_pool(
                handle,
                obj,
                desc_string,
                spt_vhba_templates[vhba]['wwpnpool']['name'],
                spt_vhba_templates[vhba]['wwpnpool']['range'])
            utilities.add_to_remove_script(
                file_out,
                "org-root/wwn-pool-"+spt_vhba_templates[vhba]['wwpnpool']['name'],
                "FcpoolInitiators")
            vhba_template.create_vhba_template(
                handle,
                obj,
                desc_string,
                vhba,
                spt_vhba_templates[vhba]['wwpnpool']['name'],
                #vhba,
                spt_vhba_templates[vhba]['vsans'],
                spt_vhba_templates[vhba]['template_type'],
                spt_vhba_templates[vhba]['switch_id'])
            utilities.add_to_remove_script(file_out,
                                "org-root/san-conn-templ-"+vhba,
                                "VnicSanConnTempl")

        # handle.CompleteTransaction()

        # Create UUID pool
        uuid_pool.create_uuid_pool(handle,
                                   obj,
                                   desc_string,
                                   spt_pools['uuid']['name'],
                                   spt_pools['uuid']['range'])
        utilities.add_to_remove_script(file_out,
                            "org-root/uuid-pool-" + \
                            spt_pools['uuid']['name'],
                            "UuidpoolPool")

        # Create WWNN pool
        wwnn_pool.create_wwnn_pool(handle,
                                   obj,
                                   desc_string,
                                   spt_pools['wwnn']['name'],
                                   spt_pools['wwnn']['range'])
        utilities.add_to_remove_script(file_out,
                             "org-root/wwn-pool-" + \
                             spt_pools['wwnn']['name'],
                             "FcpoolInitiators")

        # Create server pool
        server_pool.create_server_pool(handle,
                                       obj,
                                       desc_string,
                                       spt_pools['server']['name'],
                                       spt_pools['server']['range'])
        utilities.add_to_remove_script(file_out,
                             "org-root/compute-pool-" + \
                             spt_pools['server']['name'],
                             "ComputePool")

        # Create firmware policy
        firmware_policy.create_fw_policy(handle,
                                         obj,
                                         desc_string,
                                         spt_policies['firmware']['name'])
        utilities.add_to_remove_script(
            file_out,
            "org-root/fw-host-pack-"+spt_policies['firmware']['name'],
            "FirmwareComputeHostPack")

        # Create maintenance policy
        '''
        maintenance_policy.create_maintenance_policy(
            handle,
            spt_policies['maintenance']['name'])
        utilities.add_to_remove_script(
            file_out,
            "org-root/maint-"+spt_policies['maintenance']['name'],
            "LsmaintMaintPolicy")
        '''

        # Create boot policy
        '''
        boot_lan_policy.create_lan_boot_policy(
            handle,
            spt_policies['boot']['name'],
            spt_policies['boot']['vnic'])
        utilities.add_to_remove_script(
            file_out,
            "org-root/boot-policy-"+spt_policies['boot']['name'],
            "LsbootPolicy")
        '''

        # Create boot policy

        boot_san_policy.create_boot_san_policy(
            handle,
            obj,
            desc_string,
            spt_policies['boot']['name'],
            spt_policies['boot']['paths']['vhba_primary']['name'],
            spt_policies['boot']['paths']['vhba_primary']['target_primary'],
            spt_policies['boot']['paths']['vhba_secondary']['name'],
            spt_policies['boot']['paths']['vhba_secondary']['target_primary'])
        utilities.add_to_remove_script(
            file_out,
            "org-root/boot-policy-"+spt_policies['boot']['name'],
            "LsbootPolicy")


        # Create Service Profile template
        sp_template.create_sp_template(
            handle,
            obj,
            desc_string,
            remove_script_file,
            spt,
            spt_policies['boot']['name'],
            spt_pools['uuid']['name'],
            spt_pools['wwnn']['name'],
            spt_vnic_templates,
            spt_vhba_templates,
            spt_pools['server']['name'],
            spt_policies['firmware']['name'],
            spt_policies['maintenance']['name'])
        utilities.add_to_remove_script(
            file_out,
            "org-root/ls-"+spt,
            "LsServer")

        handle.CompleteTransaction()
        handle.StartTransaction()

        # Create Service Profile instances
        #handle.LsInstantiateNTemplate(
        #    "org-root/ls-"+spt,
        #    sp_instances['instances'],
        #    sp_instances['prefix'],
        #    "org-root",
        #    False)

        #obj = handle.GetManagedObject(None,OrgOrg.ClassId(),{OrgOrg.DN:"org-root"})

        cur_instance = 1
        while cur_instance <= int(sp_instances['instances']):
        #    mo = handle.AddManagedObject(
        #        obj,
        #        desc_string,
        #        LsServer.ClassId(),
        #        {LsServer.SRC_TEMPL_NAME: "org-root/ls-" + spt,
        #         LsServer.NAME: sp_instances['prefix'] + str(cur_instance)})
        ##    utilities.add_to_remove_script(
        #        file_out,
        #        "org-root/ls-"+sp_instances['prefix']+str(cur_instance),
        ##        "LsServer")
            cur_instance += 1


        handle.CompleteTransaction()


        # Create boot policy
        '''
        boot_san_policy.create_boot_san_policy(
            handle,
            spt_vhba_templates[vnic]['qos_policy']['name'],
            "bronze",
            "line-rate",
            "10240",
            "none")
        '''

        # spt_uuid_pools = spt_pools['uuid']
        '''
        firmware.create_fw_package(
            handle,
            spt_pools['uuid']['name'],
            spt_pools['uuid']['range'])
        '''

    #handle.CompleteTransaction()

    # Logout to clean up
    handle.Logout()

    time_now = utilities.current_time()

    print ""
    print("Completed in %.2f seconds" % round((time_now-time_start), 2))
    print "Remove script created is", remove_script_file
