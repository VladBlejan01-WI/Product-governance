# Security and Compliance Baseline

**Status:** Open assessment. This dossier does not grant endpoint, production-network, or safety approval.

## Assessment boundary

The manuals describe Windows PC software, dedicated test hardware, USB/RS232, optional API/DLL and LabVIEW integration, an optional InterfaceBox for production-line I/O, and storage/database options. Whether any optional integration is deployed locally is TBD. Assess the actual endpoint and each implemented interface before approval.

## Evidence and decisions required

| Area | Required confirmation |
|---|---|
| Package trust | Approved vendor source, version, signature/hash, component inventory, and malware scan in controlled records |
| Endpoint controls | Supported managed Windows baseline, privileges, drivers, services, ports, update behavior, and uninstall/rollback |
| Interfaces | Actual USB/RS232/API/LabVIEW/INT1/database/production connections, data flows, owners, and required network rules |
| Identity and access | Actual operator authentication, authorization, shared-account and privileged-access arrangements |
| Data protection | Actual data stores, access, encryption, classification, retention, backup, and recovery |
| Vulnerability/support | Vendor advisory route, supported release, patch/update process, and internal review cadence |
| Operational safety | Responsible engineering/safety review of the installed tester, safety-lock configuration, work method, and authorized operators |
| Compliance | Applicable endpoint, production/OT, quality, privacy, and safety policies; applicability and approval TBD |

The supplied documents do not establish the organization's security configuration or demonstrate controls such as encryption, SSO, audit logging, or vulnerability management. Record evidence and detailed findings only in approved controlled storage.
