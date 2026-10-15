# Deployment and Compatibility

## Documented baseline

- The supplied DPG10 manual documents Microsoft Windows 10 and Windows 11.
- It recommends screen resolution of 1400 × 900 or higher.
- The manual states that the Main application is 64-bit-only from software version 3.6.x and the Production application is 64-bit-only.
- The SharePoint folder `DPG10_V3.9.4` contains setup/demo application executable filenames marked `3.9.4`. The installed Weidmüller version and package approval are TBD.
- Documented tester connections include USB and RS232.

These are statements from the supplied manuals/package-folder inventory. They do not confirm current vendor support lifecycle or compatibility with a particular managed Weidmüller endpoint image.

## Required validation before deployment/change

- Confirm exact installed and proposed software release, tester model/serial under controlled asset records, firmware, drivers, optional hardware, and calibration status.
- Obtain/verify approved vendor installer source, signature, hash, package contents, privileges, install/uninstall behavior, services, ports, and update behavior.
- Test on the target managed Windows build and confirm standard-user operation and interface needs.
- Validate representative measurements, safety interlocks, any database/API/production integration, logging, backup, rollback, and recovery.
- Document distribution/update owner and vendor support lifecycle.

Do not run or redistribute the setup/demo executables from this documentation task; binary handling belongs to approved endpoint security and packaging processes.
