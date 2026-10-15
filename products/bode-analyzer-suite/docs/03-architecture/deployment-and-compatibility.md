# Deployment and Compatibility

## Evidence-bounded baseline

The supplied Bode 500 technical-data sheet identifies BAS 3.52 and Windows 11 as PC requirements. The supplied quick-start guide states Microsoft Windows 10 / 11 and BAS 3.50 or newer. This difference must be reconciled against current vendor release documentation and the actual target hardware before deployment.

For Bode 500, the supplied user manual lists these minimum PC conditions: Intel Core-i Dual-Core (or similar), 2 GB RAM (4 GB recommended), Super VGA (1024 x 768; higher recommended), DirectX 11 with Direct2D support, and USB 2.0 or higher. It also lists incoming UDP 5353 for device detection and outgoing TCP 8080–8090 for device connection.

## Required package validation

- Obtain installer from the approved vendor channel; record version, publication date, hash, signer, and source in controlled evidence.
- Validate installation, elevation requirements, drivers, services, tasks, logs, detection, repair, uninstall, and rollback.
- Validate standard-user operation and actual network activity during install, first run, help, update, activation, and support workflows.
- Test the target Windows baseline, BAS version, hardware firmware, accessories, calibration, representative measurement files, and any automation.
- Define managed distribution method and update ownership.
