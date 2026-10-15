# Architecture Overview

## Documented logical boundary

```text
Engineering / quality / production operator
  -> Windows PC running DPG10 Main or Production application
  -> USB or RS232 connection (documented)
  -> DPG10 B-Series or DPG20 tester (exact local model TBD)
  -> DUT / inductive component

Optional, if present locally:
  PC/application -> API/DLL or LabVIEW automation -> TBD consumer/system
  Tester/application -> InterfaceBox INT1 inputs/outputs -> TBD production-line equipment
  Measurement records -> SQLite/XML or configured ODBC/database target -> TBD storage owner
```

## Verified from supplied manuals

- The solution combines Windows PC software with dedicated DPG10/DPG20 measurement hardware.
- USB and RS232 connections are documented.
- Optional hardware includes a 3-Phase Extension Unit and InterfaceBox INT1.
- The manuals document API/DLL, .NET/C++, and LabVIEW integration possibilities and database/storage options.

## Not verified for the local service

Exact deployed tester model, PC, software version, database, production line, external system endpoints, network/security boundary, data location, and implemented APIs are TBD. The diagram shows documented product options, not confirmation that Weidmüller has deployed them.
