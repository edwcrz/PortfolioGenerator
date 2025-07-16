# impotaciones
import json as js
from pathlib import Path
from datetime import UTC, datetime

# cargo json
Directorio = Path("PortfolioEAC.json")
print (type(Directorio))

with open("PortfolioEAC.json",'r',encoding="utf-8") as archivo:
    diccionario = js.load(archivo)

print (type(diccionario))
print (diccionario['name'])

datetimecomplete = datetime.now(UTC)
print(type(datetimecomplete))
print(datetimecomplete.year)
print(type(datetimecomplete.year))

diccionario["current_year"]=datetimecomplete.year
print(type(diccionario["current_year"]))
print(diccionario["current_year"])

if "social_links" in diccionario:
    print ("social_links")
    print (type(diccionario["social_links"]))
    print (diccionario["social_links"])
    print (type(diccionario["social_links"]))