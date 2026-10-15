# Security and Quality Baseline

**Status:** Open assessment. No formal security approval or risk assessment is asserted.

## Reported environment

The product is reported as a local desktop application with ZEISS Quality Suite, licensing mechanisms or hardware dongles, sensor drivers, and VMR functionality. PLM project storage and CAD workflows are reported. Actual components and data flows require site-level validation.

## Required assessment

| Area | Required evidence / decision |
|---|---|
| Endpoint/package | Approved installer source, release, service pack, signature/hash, components, privileges, and controlled distribution |
| Compatibility | Supported OS, Windows update behavior, graphics/sensor drivers, ZEISS Quality Suite, VMR, and rollback |
| Identity/access | License administration, dongle/activation behavior, user access, approved administration roles, and access transfer |
| Data | Inspection project/report classification, PLM permissions, retention, backup, recovery, and any personal-data fields |
| Integrations | Actual PLM/CAD, scanner/CT, PMI/MBD, STEP AP242 interfaces and associated data flows |
| Security | Network behavior, update channels, vulnerabilities, support lifecycle, and endpoint controls based on the deployed configuration |
| Quality | Applicability to accredited/DAkkS-related measurement, GPS-compliant evaluation, measurement uncertainty, validation, and change-control procedures |
| Governance | Identify accountable Quality/Metrology, Product, Security, data, and site owners; record approvals in approved systems |

The intake says no formal security/risk review has been identified. Absence of a supplied assessment does not prove that controls are absent. Detailed findings remain in controlled security records, not Git.
