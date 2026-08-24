# Architecture Overview

**Document status:** Draft baseline  
**Owner:** TBD  
**Review frequency:** Quarterly or on material change  
**Last reviewed:** 2026-08-24

> Describe logical boundaries without claiming undiscovered implementation facts.

## Context

IRBIS 3 Professional is a commercial member of InfraTec's IRBIS 3 thermography software family. Public product material describes thermal-image analysis, measurement-data visualization, thermography reporting, image-sequence analysis, advanced emissivity correction, geometric measurement, 3D thermographic display, parallel thermogram analysis, editors, and SDK-related integration. Exact purchased modules, version, entitlement, support terms, installation scope, and enterprise controls require internal verification.

## Logical components

User workstation; IRBIS application/UI; analysis functions; local or approved measurement storage; report/export outputs; optional camera/control or SDK integration.

## Architecture principles

Least privilege; supported workstation baseline; traceable installation; approved storage; recoverable user data; controlled integration; reproducible reports where required.

