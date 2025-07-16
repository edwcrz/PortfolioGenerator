from datetime import datetime
from generate_portfolio import data

ahora = datetime.now(tz=None)
print (ahora)
año = ahora.year
mes = ahora.month
dia = ahora.day
hora = ahora.hour
minutos = ahora.minute
segundos = ahora.second
print (f"{dia}/{mes}/{año} {hora}:{minutos}:{segundos}")

CantidadEperience = 8
QuantityExperience = [5, 4, 3, 7, 8, 1, 9, 4]
QuantityExperience[0]= data.work_experience