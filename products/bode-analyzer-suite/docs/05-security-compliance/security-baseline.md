# Security and Compliance Baseline

**Status:** Open assessment; no formal approval is asserted.

## Primary policy classification

The proposed architecture is a local endpoint application with external hardware. Endpoint application governance is therefore the primary assessment area. SaaS and server policies are not expected to apply unless cloud licensing, telemetry, online storage, a shared license service, or server-side automation is introduced.

## Required validation

| Area | Required evidence / decision |
|---|---|
| Installer trust | Vendor source, signature, hash, malware scan, and retained approved installer record |
| Privileges | Installation and runtime elevation requirements |
| Network | DNS/HTTP(S) and device traffic during install, use, update, help, activation, and support |
| Ports | Confirm need for Bode 500 incoming UDP 5353 and outgoing TCP 8080–8090 in the actual deployment |
| Telemetry and privacy | Vendor terms, observed behaviour, opt-out/configuration, and policy decision |
| Local components | Drivers, services, scheduled tasks, startup items, browser components, and firewall changes |
| Data protection | Default paths, classification, approved storage, backup, encryption, and retention |
| Vulnerabilities | Vendor advisory/contact channel and internal review cadence |
| Updates | Source, signature validation, user control, managed-update approach, and rollback |

Do not record installer hashes, internal scan results, detailed vulnerabilities, or sensitive security evidence in Git.
