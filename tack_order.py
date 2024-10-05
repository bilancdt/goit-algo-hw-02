import queue
import random
import time

# Створення черги для заявок
request_queue = queue.Queue()

# Лічильник для унікальних номерів заявок
request_counter = 1

# Функція для генерації нових заявок
def generate_request():
    global request_counter
    # Генерація нової заявки
    request = f"Request #{request_counter}"
    request_counter += 1
    # Додавання заявки до черги
    request_queue.put(request)
    print(f"Generated: {request}")

# Функція для обробки заявок
def process_request():
    if not request_queue.empty():
        # Видалення заявки з черги
        request = request_queue.get()
        # Імітація обробки заявки
        print(f"Processed: {request}")
    else:
        # Якщо черга порожня
        print("Queue is empty, no requests to process.")

# Головний цикл програми
def main():
    while True:
        # Генерація нових заявок
        if random.random() < 0.7:  # 70% ймовірності на створення нової заявки
            generate_request()

        # Обробка заявок
        if random.random() < 0.5:  # 50% ймовірності на обробку заявки
            process_request()

        # Затримка для імітації реального часу
        time.sleep(1)

# Запуск програми
if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\nProgram stopped manually.")
