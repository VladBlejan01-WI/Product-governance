# Architecture Overview

## Reported logical architecture

```text
Metrology / Quality / Product Development / Production user
  -> local Windows workstation
  -> ZEISS INSPECT basic or ZEISS INSPECT Pro
  -> ZEISS Quality Suite, licensing mechanism/dongle, sensor drivers (reported dependencies)
  -> optical measurement system or CT measurement data (specific local devices TBD)
  -> inspection project / report
  -> PLM project storage (integration/workflow reported; system and endpoint TBD)

Optional/locally configured workflow dependencies reported:
  -> CAD inputs: Creo / Siemens NX / CATIA
  -> PMI/MBD and STEP AP242 data
  -> Virtual Measuring Room (VMR)
```

## Reported boundary

Stakeholder intake describes ZEISS INSPECT and Pro primarily as local desktop applications and identifies no dedicated application server or database. It also describes PLM project storage and CAD workflows. Exact sites, versions, scanner/CT configurations, license architecture, deployed integrations, network flows, and data paths have not been verified.

## Architecture controls

- Treat PLM, CAD, measurement sensors, CT/optical hardware, drivers, ZEISS Quality Suite, license dongles/mechanisms, and VMR as candidate dependencies until confirmed locally.
- Obtain system owners and approved data-flow/storage diagrams before recording integrations as deployed facts.
- Do not infer Active Directory, SSO, MES/CAQ, application servers, or database components; local deployment details remain TBD.
