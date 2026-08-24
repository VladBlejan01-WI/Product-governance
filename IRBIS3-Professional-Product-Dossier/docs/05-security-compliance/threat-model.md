# Threat Model

**Document status:** Draft baseline  
**Owner:** TBD  
**Review frequency:** Quarterly or on material change  
**Last reviewed:** 2026-08-24

> Capture credible security threats.

## Assets

Installer, license material, measurement files, analysis settings, reports, workstations, support packages, integration credentials.

## Threats and mitigations

| Threat | Proposed mitigation |
|---|---|
| Untrusted installer | Approved source and integrity check |
| Unauthorized use | Request/approval and entitlement reconciliation |
| Sensitive file leakage | Approved storage and controlled transfer |
| Malicious file or plugin | Endpoint protection and controlled sources |
| Unsupported component | Version/OS governance |
| SDK credential exposure | Secrets management and review |

