# impotaciones
import json as js
from pathlib import Path
from datetime import UTC, datetime

# cargo json
Directorio = Path("PortfolioEAC.json")
with Directorio.open(encoding="utf-8") as f:
contenido = f.read()
print(contenido)