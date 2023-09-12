# Определяем класс Person
class Person:
# Конструктор класса, инициализирующий атрибуты имя и возраст
  def __init__(self, name, age):
    self.name = name
    self.age = age

# Метод для представления информации о человеке
  def introduce(self):
    print(f"Привет, меня зовут {self.name} и мне {self.age} лет.")

# Создаем объекты класса Person
person1 = Person("Анна", 25)
person2 = Person("Иван", 30)

# Вызываем методы объектов
person1.introduce() # Вывод: Привет, меня зовут Анна и мне 25 лет.
person2.introduce() # Вывод: Привет, меня зовут Иван и мне 30 лет.


# Базовый класс обработчика, содержащий ссылку на следующий обработчик в цепочке (если есть)
class Handler:
  def __init__(self, successor=None):
    self.successor = successor # преемник (следующий обработчик в цепочке)

  def handle_request(self, currency):
    pass


# Конкретный обработчик для долларов США
class USDHandler(Handler):
  def handle_request(self, currency):
# Если валюта - USD, обработаем ее
    if currency == "USD":
      print("Обработка долларов США")
# Если это не USD и у нас есть преемник, передаем запрос дальше
    elif self.successor:
      self.successor.handle_request(currency)


# Конкретный обработчик для евро
class EURHandler(Handler):
  def handle_request(self, currency):
# Если валюта - EUR, обработаем ее
    if currency == "EUR":
      print("Обработка евро")
# Если это не EUR и у нас есть преемник, передаем запрос дальше
    elif self.successor:
      self.successor.handle_request(currency)


# Конкретный обработчик для британских фунтов
class GBPHandler(Handler):
  def handle_request(self, currency):
# Если валюта - GBP, обработаем ее
    if currency == "GBP":
      print("Обработка британских фунтов")
# Если это не GBP и у нас есть преемник, передаем запрос дальше
    elif self.successor:
      self.successor.handle_request(currency)


# Создаем обработчики
usd_handler = USDHandler()
eur_handler = EURHandler(usd_handler) # передаем usd_handler как преемника для eur_handler
gbp_handler = GBPHandler(eur_handler) # передаем eur_handler как преемника для gbp_handler

# Посылаем запрос на обработку GBP
# Запрос будет передан от gbp_handler к eur_handler, затем к usd_handler, пока он не будет обработан
gbp_handler.handle_request("GBP")