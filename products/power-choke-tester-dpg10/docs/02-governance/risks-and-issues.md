# Risks and Issues

**Status:** Candidate governance risks for review, not confirmed incidents or control failures. Ratings and owners are TBD.

| ID | Candidate risk / evidence | Potential effect | Proposed treatment | Owner | Rating / status |
|---|---|---|---|---|---|
| R1 | Installed release and approved package baseline are unverified; SharePoint contains a `3.9.4` package folder | Unsupported or inconsistent software/hardware setup | Confirm installed version, package provenance, supported OS, compatibility tests, updates, and rollback | TBD | TBD / Open |
| R2 | Dedicated tester, interfaces, accessories, and calibration are product dependencies | Test unavailability or invalid results | Inventory exact assets, firmware, calibration, connection method, and validated setup | TBD | TBD / Open |
| R3 | Manuals describe local SQLite and other database/storage/export options; actual deployment and recovery are unknown | Loss or inappropriate exposure of quality/production measurement records | Confirm actual data path, classification, access, retention, backup, and restore testing | TBD | TBD / Open |
| R4 | API/DLL, LabVIEW, INT1, and production integration capabilities are documented; local integrations are unknown | Uncontrolled interface changes or production disruption | Inventory implemented integrations, data flows, interface owners, change controls, and acceptance tests | TBD | TBD / Open |
| R5 | Manuals describe a safety-lock interface and electrically hazardous test equipment | Injury or equipment damage if test setup or safety procedure is unsuitable | Have the responsible engineering/safety owner validate the actual installation and authorized-use procedure; do not treat this software record as a safety approval | TBD | TBD / Open |
| R6 | Product manuals do not establish Weidmüller authentication, access, encryption, audit, vulnerability, or update controls | Security and compliance posture cannot yet be assessed | Obtain vendor/security evidence and perform endpoint/application assessment | TBD | TBD / Open |
| R7 | License, entitlement, support coverage, and renewal terms are not established by the reviewed documents | Compliance or support interruption | Reconcile controlled purchase, EULA, entitlement, and support records | TBD | TBD / Open |
