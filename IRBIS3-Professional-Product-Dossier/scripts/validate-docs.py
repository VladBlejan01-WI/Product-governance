from pathlib import Path
import sys
r=Path(__file__).resolve().parents[1]
required=['product.yaml','README.md','docs/01-product/product-brief.md','docs/03-architecture/architecture-overview.md','docs/04-service/support-model.md','docs/05-security-compliance/security-classification.md','docs/06-commercial/licensing.md','docs/07-delivery/backlog-model.md']
missing=[x for x in required if not (r/x).exists()]
print('Missing:', missing)
sys.exit(1 if missing else 0)
