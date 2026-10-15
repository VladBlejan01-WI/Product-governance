# Architecture Overview

## Logical architecture

```text
Engineering user
  -> Windows endpoint running Bode Analyzer Suite
  -> local USB or network connection
  -> Bode 100 or Bode 500 measurement hardware
  -> probes / fixtures / injection accessories
  -> device under test

Measurement configurations, traces, plots, notes, and exports
  -> local working storage or approved corporate storage
```

## Boundary and dependencies

- Deployment class: endpoint application with external hardware dependency.
- No enterprise-system integration is verified.
- User identity is expected to be the signed-in Windows context; product-specific accounts, SSO, Entra ID, and roles are TBD.
- Results may contain confidential product behaviour. Storage, classification, retention, and encryption must be decided before operational use.
- BAS 3.52 documentation describes `.bode3` files and CSV, Excel-compatible, and Touchstone export options. Treat data portability and retention as governance requirements.
