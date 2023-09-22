# Реализовать секундомер на любом языке программирования в любой парадигме. Секундомер должен поддерживать следующий функционал:
# ○ Запуск
# ○ Пауза
# ○ Выход из паузы
# ○ Остановка

import time

class Stopwatch:
    def __init__(self):
        self.start_time = None
        self.pause_time = None
        self.paused = False

    def start(self):
        if not self.paused:
            self.start_time = time.time()
        else:
            self.start_time += time.time() - self.pause_time
        self.paused = False

    def pause(self):
        if not self.paused:
            self.pause_time = time.time()
            self.paused = True

    def resume(self):
        if self.paused:
            self.start_time += time.time() - self.pause_time
            self.paused = False

    def stop(self):
        self.start_time = None
        self.paused = False

    def elapsed_time(self):
        if self.start_time is None:
            return 0
        elif self.paused:
            return self.pause_time - self.start_time
        else:
            return time.time() - self.start_time

    def display_time(self):
        seconds = int(self.elapsed_time())
        minutes, seconds = divmod(seconds, 60)
        hours, minutes = divmod(minutes, 60)
        return f"{hours:02}:{minutes:02}:{seconds:02}"

if __name__ == "__main__":
    stopwatch = Stopwatch()
    while True:
        print("Секундомер (введите команду):")
        print("1. Запуск")
        print("2. Пауза")
        print("3. Выход из паузы")
        print("4. Остановка")
        print("5. Время")
        print("6. Выход")
        choice = input("Введите номер команды: ")

        if choice == "1":
            stopwatch.start()
        elif choice == "2":
            stopwatch.pause()
        elif choice == "3":
            stopwatch.resume()
        elif choice == "4":
            stopwatch.stop()
        elif choice == "5":
            print(f"Прошло времени: {stopwatch.display_time()}")
        elif choice == "6":
            break
        else:
            print("Неправильная команда. Попробуйте ещё раз.")