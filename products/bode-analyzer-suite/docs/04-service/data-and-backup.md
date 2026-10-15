# Data, Backup, and Recovery

BAS documentation describes saving measurement configurations, calibration data, measurement data, and graphical display settings in `.bode3` files. It also documents exports to CSV, Excel-compatible formats, Touchstone files, and chart images.

## Baseline controls

- Store business-relevant results, templates, scripts, and approved exports on corporate storage rather than relying solely on endpoint-local files.
- Confirm default locations, native/export formats, file ownership, data classification, retention, encryption, and backup scope before operational use.
- Treat device-specific behaviour carefully: supplied documentation says a `.bode3` file generated for Bode 100 cannot be opened and used with Bode 500, and vice versa, although it can be opened without a connected device to review and export measured data.
- Keep only non-sensitive references in Git; detailed test data, product information, or calibration evidence belongs in approved controlled storage.
