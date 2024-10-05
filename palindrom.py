from collections import deque

def is_palindrome(s):
    # Приводимо рядок до нижнього регістру та видаляємо пробіли
    cleaned_string = ''.join(char.lower() for char in s if char.isalnum())

    # Додаємо всі символи до двосторонньої черги
    char_deque = deque(cleaned_string)

    # Порівнюємо символи з обох кінців черги
    while len(char_deque) > 1:
        if char_deque.popleft() != char_deque.pop():
            return False  # Якщо символи не збігаються, це не паліндром
    return True  # Якщо всі символи збігаються, це паліндром

# Приклади використання
print(is_palindrome("A man a plan a canal Panama"))  # True
print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False
