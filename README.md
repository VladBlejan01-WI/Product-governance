# Product Governance

This repository is the Git source of truth for IT product documentation and portfolio governance.

Git stores the approved product record, documentation, metadata, diagrams, templates, and decision records. The work-management platform stores backlog items and delivery tasks. A controlled records platform stores contracts, invoices, entitlement evidence, confidential security evidence, license keys, and personal information.

## Repository sections

- [products/](products/)
- [portfolio/](portfolio/)
- [_templates/](_templates/)
- [docs/](docs/)
- [automation/](automation/)

## Onboarded products

- IRBIS 3 Professional

## Adding a new product

1. Create a new folder under [products/](products/) in lowercase kebab-case.
2. Add a product metadata file in YAML for the new product.
3. Add a product README, evidence index, and any supporting governance notes.
4. Add the product to the portfolio catalog and risk registers.
5. Update ownership and review dates using only authoritative evidence.

## Governance note

TBD values must be completed only from authoritative evidence. Where a fact is not yet validated, the repository keeps the placeholder value and does not infer or assume missing details.

## Scope

This repository is intentionally limited to logical enterprise product governance and support boundaries. It does not replace authoritative operational records or vendor-controlled product repositories.
