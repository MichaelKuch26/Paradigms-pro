# Предположим, у нас есть список измерений температуры в разных масштабах (Фаренгейт, Кельвин, и Цельсий), и нам нужно сконвертировать и стандартизировать все измерения в градусы Цельсия.

# Исходные данные
temperature_data = [("Фаренгейт", 98.6), ("Кельвин", 310.15), ("Цельсий", 37.0)]

temperature_data_new = []

def standartization(temperature, shkala):
  if (shkala == "Фаренгейт"):
    return (temperature - 32) * 5/9
  elif (shkala == "Кельвин"):
    return (temperature - 273.15)
  elif (shkala == "Цельсий"):
    return temperature
  else:
    return ValueError("Ошибка: Не удалось стандартизировать")
  
result = [(standartization(temperature, shkala), "Цельсий") for shkala, temperature in  temperature_data]

for temperature, shkala in result:
  print(f"{temperature: .2f} градусов {shkala}")

