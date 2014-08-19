#!/usr/bin/python

from UcsSdk import OrgOrg
from UcsSdk import FirmwareComputeHostPack


def create_bios_policy(
        handle,
        obj,
        desc,
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

    mo = handle.AddManagedObject(
        obj,
        BiosVProfile.ClassId(),
        {BiosVProfile.DN:"org-root/bios-prof-bios_pol_1",
         BiosVProfile.REBOOT_ON_UPDATE:"no",
         BiosVProfile.POLICY_OWNER:"local",
         BiosVProfile.NAME:"bios_pol_1",
         BiosVProfile.DESCR:""})

    handle.AddManagedObject(
        mo,
        BiosVfAssertNMIOnPERR.ClassId(),
        {BiosVfAssertNMIOnPERR.VP_ASSERT_NMION_PERR:"platform-default",
         BiosVfAssertNMIOnPERR.DN:"org-root/bios-prof-bios_pol_1/Assert-NMI-on-PERR"}, True)

    handle.AddManagedObject(
        mo,
        BiosVfAssertNMIOnSERR.ClassId(),
        {BiosVfAssertNMIOnSERR.VP_ASSERT_NMION_SERR:"platform-default",
         BiosVfAssertNMIOnSERR.DN:"org-root/bios-prof-bios_pol_1/Assert-NMI-on-SERR"}, True)

    handle.AddManagedObject(
        mo,
        BiosVfBootOptionRetry.ClassId(),
        {BiosVfBootOptionRetry.VP_BOOT_OPTION_RETRY:"platform-default",
         BiosVfBootOptionRetry.DN:"org-root/bios-prof-bios_pol_1/Boot-option-retry"}, True)

    mo_4 = handle.AddManagedObject(mo, BiosVfCPUPerformance.ClassId(), {BiosVfCPUPerformance.DN:"org-root/bios-prof-bios_pol_1/CPU-Performance", BiosVfCPUPerformance.VP_CPUPERFORMANCE:"platform-default"}, True)
mo_5 = handle.AddManagedObject(mo, BiosVfConsoleRedirection.ClassId(), {BiosVfConsoleRedirection.VP_CONSOLE_REDIRECTION:"platform-default", BiosVfConsoleRedirection.VP_TERMINAL_TYPE:"platform-default", BiosVfConsoleRedirection.VP_FLOW_CONTROL:"platform-default", BiosVfConsoleRedirection.DN:"org-root/bios-prof-bios_pol_1/Console-redirection", BiosVfConsoleRedirection.VP_LEGACY_OSREDIRECTION:"platform-default", BiosVfConsoleRedirection.VP_BAUD_RATE:"platform-default"}, True)
mo_6 = handle.AddManagedObject(mo, BiosVfCoreMultiProcessing.ClassId(), {BiosVfCoreMultiProcessing.VP_CORE_MULTI_PROCESSING:"platform-default", BiosVfCoreMultiProcessing.DN:"org-root/bios-prof-bios_pol_1/Core-MultiProcessing"}, True)
mo_7 = handle.AddManagedObject(mo, BiosVfDirectCacheAccess.ClassId(), {BiosVfDirectCacheAccess.DN:"org-root/bios-prof-bios_pol_1/Direct-Cache-Access", BiosVfDirectCacheAccess.VP_DIRECT_CACHE_ACCESS:"platform-default"}, True)
mo_8 = handle.AddManagedObject(mo, BiosVfDramRefreshRate.ClassId(), {BiosVfDramRefreshRate.DN:"org-root/bios-prof-bios_pol_1/Dram-Refresh-Rate", BiosVfDramRefreshRate.VP_DRAM_REFRESH_RATE:"platform-default"}, True)
mo_9 = handle.AddManagedObject(mo, BiosVfEnhancedIntelSpeedStepTech.ClassId(), {BiosVfEnhancedIntelSpeedStepTech.VP_ENHANCED_INTEL_SPEED_STEP_TECH:"platform-default", BiosVfEnhancedIntelSpeedStepTech.DN:"org-root/bios-prof-bios_pol_1/Enhanced-Intel-SpeedStep-Tech"}, True)
mo_10 = handle.AddManagedObject(mo, BiosVfExecuteDisableBit.ClassId(), {BiosVfExecuteDisableBit.VP_EXECUTE_DISABLE_BIT:"platform-default", BiosVfExecuteDisableBit.DN:"org-root/bios-prof-bios_pol_1/Execute-Disable-Bit"}, True)
mo_11 = handle.AddManagedObject(mo, BiosVfFrontPanelLockout.ClassId(), {BiosVfFrontPanelLockout.DN:"org-root/bios-prof-bios_pol_1/Front-panel-lockout", BiosVfFrontPanelLockout.VP_FRONT_PANEL_LOCKOUT:"platform-default"}, True)
mo_12 = handle.AddManagedObject(mo, BiosVfIntelHyperThreadingTech.ClassId(), {BiosVfIntelHyperThreadingTech.VP_INTEL_HYPER_THREADING_TECH:"platform-default", BiosVfIntelHyperThreadingTech.DN:"org-root/bios-prof-bios_pol_1/Intel-HyperThreading-Tech"}, True)
mo_13 = handle.AddManagedObject(mo, BiosVfIntelTurboBoostTech.ClassId(), {BiosVfIntelTurboBoostTech.DN:"org-root/bios-prof-bios_pol_1/Intel-Turbo-Boost-Tech", BiosVfIntelTurboBoostTech.VP_INTEL_TURBO_BOOST_TECH:"enabled"}, True)
mo_14 = handle.AddManagedObject(mo, BiosVfIntelVTForDirectedIO.ClassId(), {BiosVfIntelVTForDirectedIO.VP_INTEL_VTFOR_DIRECTED_IO:"enabled", BiosVfIntelVTForDirectedIO.VP_INTEL_VTDINTERRUPT_REMAPPING:"platform-default", BiosVfIntelVTForDirectedIO.VP_INTEL_VTDPASS_THROUGH_DMASUPPORT:"platform-default", BiosVfIntelVTForDirectedIO.VP_INTEL_VTDCOHERENCY_SUPPORT:"platform-default", BiosVfIntelVTForDirectedIO.VP_INTEL_VTDATSSUPPORT:"platform-default", BiosVfIntelVTForDirectedIO.DN:"org-root/bios-prof-bios_pol_1/Intel-VT-for-directed-IO"}, True)
mo_15 = handle.AddManagedObject(mo, BiosVfIntelVirtualizationTechnology.ClassId(), {BiosVfIntelVirtualizationTechnology.VP_INTEL_VIRTUALIZATION_TECHNOLOGY:"enabled", BiosVfIntelVirtualizationTechnology.DN:"org-root/bios-prof-bios_pol_1/Intel-Virtualization-Technology"}, True)
mo_16 = handle.AddManagedObject(mo, BiosVfIntelEntrySASRAIDModule.ClassId(), {BiosVfIntelEntrySASRAIDModule.DN:"org-root/bios-prof-bios_pol_1/Intel-entry-SAS-RAID-module", BiosVfIntelEntrySASRAIDModule.VP_SASRAIDMODULE:"platform-default", BiosVfIntelEntrySASRAIDModule.VP_SASRAID:"platform-default"}, True)
mo_17 = handle.AddManagedObject(mo, BiosVfLocalX2Apic.ClassId(), {BiosVfLocalX2Apic.VP_LOCAL_X2_APIC:"platform-default", BiosVfLocalX2Apic.DN:"org-root/bios-prof-bios_pol_1/Local-X2-Apic"}, True)
mo_18 = handle.AddManagedObject(mo, BiosVfLvDIMMSupport.ClassId(), {BiosVfLvDIMMSupport.DN:"org-root/bios-prof-bios_pol_1/LvDIMM-Support", BiosVfLvDIMMSupport.VP_LV_DDRMODE:"platform-default"}, True)
mo_19 = handle.AddManagedObject(mo, BiosVfMaxVariableMTRRSetting.ClassId(), {BiosVfMaxVariableMTRRSetting.DN:"org-root/bios-prof-bios_pol_1/Max-Variable-MTRR-Setting", BiosVfMaxVariableMTRRSetting.VP_PROCESSOR_MTRR:"platform-default"}, True)
mo_20 = handle.AddManagedObject(mo, BiosVfMaximumMemoryBelow4GB.ClassId(), {BiosVfMaximumMemoryBelow4GB.VP_MAXIMUM_MEMORY_BELOW4_GB:"platform-default", BiosVfMaximumMemoryBelow4GB.DN:"org-root/bios-prof-bios_pol_1/Maximum-memory-below-4GB"}, True)
mo_21 = handle.AddManagedObject(mo, BiosVfMemoryMappedIOAbove4GB.ClassId(), {BiosVfMemoryMappedIOAbove4GB.DN:"org-root/bios-prof-bios_pol_1/Memory-mapped-IO-above-4GB", BiosVfMemoryMappedIOAbove4GB.VP_MEMORY_MAPPED_IOABOVE4_GB:"platform-default"}, True)
mo_22 = handle.AddManagedObject(mo, BiosVfMirroringMode.ClassId(), {BiosVfMirroringMode.VP_MIRRORING_MODE:"platform-default", BiosVfMirroringMode.DN:"org-root/bios-prof-bios_pol_1/Mirroring-Mode"}, True)
mo_23 = handle.AddManagedObject(mo, BiosVfNUMAOptimized.ClassId(), {BiosVfNUMAOptimized.VP_NUMAOPTIMIZED:"platform-default", BiosVfNUMAOptimized.DN:"org-root/bios-prof-bios_pol_1/NUMA-optimized"}, True)
mo_24 = handle.AddManagedObject(mo, BiosVfOSBootWatchdogTimer.ClassId(), {BiosVfOSBootWatchdogTimer.VP_OSBOOT_WATCHDOG_TIMER:"platform-default", BiosVfOSBootWatchdogTimer.DN:"org-root/bios-prof-bios_pol_1/OS-Boot-Watchdog-Timer"}, True)
mo_25 = handle.AddManagedObject(mo, BiosVfOSBootWatchdogTimerPolicy.ClassId(), {BiosVfOSBootWatchdogTimerPolicy.VP_OSBOOT_WATCHDOG_TIMER_POLICY:"platform-default", BiosVfOSBootWatchdogTimerPolicy.DN:"org-root/bios-prof-bios_pol_1/OS-Boot-Watchdog-Timer-Policy"}, True)
mo_26 = handle.AddManagedObject(mo, BiosVfOSBootWatchdogTimerTimeout.ClassId(), {BiosVfOSBootWatchdogTimerTimeout.VP_OSBOOT_WATCHDOG_TIMER_TIMEOUT:"platform-default", BiosVfOSBootWatchdogTimerTimeout.DN:"org-root/bios-prof-bios_pol_1/OS-Boot-Watchdog-Timer-Timeout"}, True)
mo_27 = handle.AddManagedObject(mo, BiosVfOnboardStorage.ClassId(), {BiosVfOnboardStorage.VP_ONBOARD_SCUSTORAGE_SUPPORT:"platform-default", BiosVfOnboardStorage.DN:"org-root/bios-prof-bios_pol_1/Onboard-Storage"}, True)
mo_28 = handle.AddManagedObject(mo, BiosVfPOSTErrorPause.ClassId(), {BiosVfPOSTErrorPause.VP_POSTERROR_PAUSE:"platform-default", BiosVfPOSTErrorPause.DN:"org-root/bios-prof-bios_pol_1/POST-error-pause"}, True)
mo_29 = handle.AddManagedObject(mo, BiosVfProcessorCState.ClassId(), {BiosVfProcessorCState.VP_PROCESSOR_CSTATE:"platform-default", BiosVfProcessorCState.DN:"org-root/bios-prof-bios_pol_1/Processor-C-State"}, True)
mo_30 = handle.AddManagedObject(mo, BiosVfProcessorC1E.ClassId(), {BiosVfProcessorC1E.VP_PROCESSOR_C1_E:"platform-default", BiosVfProcessorC1E.DN:"org-root/bios-prof-bios_pol_1/Processor-C1E"}, True)
mo_31 = handle.AddManagedObject(mo, BiosVfProcessorC3Report.ClassId(), {BiosVfProcessorC3Report.VP_PROCESSOR_C3_REPORT:"platform-default", BiosVfProcessorC3Report.DN:"org-root/bios-prof-bios_pol_1/Processor-C3-Report"}, True)
mo_32 = handle.AddManagedObject(mo, BiosVfProcessorC6Report.ClassId(), {BiosVfProcessorC6Report.VP_PROCESSOR_C6_REPORT:"platform-default", BiosVfProcessorC6Report.DN:"org-root/bios-prof-bios_pol_1/Processor-C6-Report"}, True)
mo_33 = handle.AddManagedObject(mo, BiosVfProcessorC7Report.ClassId(), {BiosVfProcessorC7Report.DN:"org-root/bios-prof-bios_pol_1/Processor-C7-Report", BiosVfProcessorC7Report.VP_PROCESSOR_C7_REPORT:"platform-default"}, True)
mo_34 = handle.AddManagedObject(mo, BiosVfQuietBoot.ClassId(), {BiosVfQuietBoot.VP_QUIET_BOOT:"platform-default", BiosVfQuietBoot.DN:"org-root/bios-prof-bios_pol_1/Quiet-Boot"}, True)
mo_35 = handle.AddManagedObject(mo, BiosVfResumeOnACPowerLoss.ClassId(), {BiosVfResumeOnACPowerLoss.DN:"org-root/bios-prof-bios_pol_1/Resume-on-AC-power-loss", BiosVfResumeOnACPowerLoss.VP_RESUME_ON_ACPOWER_LOSS:"platform-default"}, True)
mo_36 = handle.AddManagedObject(mo, BiosVfSelectMemoryRASConfiguration.ClassId(), {BiosVfSelectMemoryRASConfiguration.DN:"org-root/bios-prof-bios_pol_1/SelectMemory-RAS-configuration", BiosVfSelectMemoryRASConfiguration.VP_SELECT_MEMORY_RASCONFIGURATION:"platform-default"}, True)
mo_37 = handle.AddManagedObject(mo, BiosVfSerialPortAEnable.ClassId(), {BiosVfSerialPortAEnable.VP_SERIAL_PORT_AENABLE:"platform-default", BiosVfSerialPortAEnable.DN:"org-root/bios-prof-bios_pol_1/Serial-port-A-enable"}, True)
mo_38 = handle.AddManagedObject(mo, BiosVfSparingMode.ClassId(), {BiosVfSparingMode.DN:"org-root/bios-prof-bios_pol_1/Sparing-Mode", BiosVfSparingMode.VP_SPARING_MODE:"platform-default"}, True)
mo_39 = handle.AddManagedObject(mo, BiosVfUSBBootConfig.ClassId(), {BiosVfUSBBootConfig.DN:"org-root/bios-prof-bios_pol_1/USB-Boot-Config", BiosVfUSBBootConfig.VP_MAKE_DEVICE_NON_BOOTABLE:"platform-default", BiosVfUSBBootConfig.VP_LEGACY_USBSUPPORT:"platform-default"}, True)
mo_40 = handle.AddManagedObject(mo, BiosVfUSBFrontPanelAccessLock.ClassId(), {BiosVfUSBFrontPanelAccessLock.VP_USBFRONT_PANEL_LOCK:"platform-default", BiosVfUSBFrontPanelAccessLock.DN:"org-root/bios-prof-bios_pol_1/USB-Front-Panel-Access-Lock"}, True)
mo_41 = handle.AddManagedObject(mo, BiosVfUSBSystemIdlePowerOptimizingSetting.ClassId(), {BiosVfUSBSystemIdlePowerOptimizingSetting.DN:"org-root/bios-prof-bios_pol_1/USB-System-Idle-Power-Optimizing-Setting", BiosVfUSBSystemIdlePowerOptimizingSetting.VP_USBIDLE_POWER_OPTIMIZING:"platform-default"}, True)

    # handle.CompleteTransaction()

    print "Created Firmware Policy " + policy_name
