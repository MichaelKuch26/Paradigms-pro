# Представьте, что у вас есть список измерений топливной эффективности автомобилей в разных масштабах, таких как "миль на галлон" (MPG), "километров на литр" (KPL) и "миль на литр" (MPL). Ваша задача - создать функцию convert_to_L_per_100KM, которая принимает список измерений и конвертирует их в масштаб "литры на 100 километров" (L/100KM).

data = [
{"масштаб": "MPG", "значение": 25.0},
{"масштаб": "KPL", "значение": 10.0},
{"масштаб": "MPL", "значение": 40.0},
{"масштаб": "MPG", "значение": 30.0}
]

# Примечание: Для конвертации MPG в L/100KM используйте формулу: 
# L/100KM = 235.214583 / MPG, для KPL в L/100KM: L/100KM = 100 / KPL, и для MPL в L/100KM: L/100KM = MPL * 2.35214583.

def convert_to_L_per_100KM(mashtab, list_of_izmereny):
  if (list_of_izmereny == "MPG"):
    return 235.214583 / mashtab
  if (list_of_izmereny == "KPL"):
    return 100 / mashtab
  if (list_of_izmereny == "MPL"):
    return mashtab * 2.35214583
  else:
    return ValueError ("Ошибка конвертации")
  
result = [(convert_to_L_per_100KM(entry["значение"], entry["масштаб"]), entry["масштаб"]) for entry in data]

for mashtab, list_of_izmereny in result:
  print(f"{mashtab: .2f} MPL {list_of_izmereny}")