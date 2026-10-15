# Data, Backup, and Recovery

## Documented product options

The supplied DPG10 manual describes measurement storage using XML and SQLite, ODBC-connected database options including SQLite, MariaDB, and MySQL, and PDF/CSV/XML export. It also describes measurement records that can contain curves, parameters, DUT identifiers, tester/operator information, remarks, and resistance/serial-measurement details.

## Governance requirements (local configuration TBD)

- Identify the database and export formats actually used, the data owner, storage location, and connected systems.
- Assess whether measurement and operator records are confidential or personal data; confirm classification and retention with the accountable owners.
- Define approved access, backup, restore, retention, archival, and deletion controls before production use.
- Test recovery of the actual database/configuration and representative records.
- Do not put measurement data, operator/user lists, production identifiers, database copies, or sensitive technical evidence in Git.
