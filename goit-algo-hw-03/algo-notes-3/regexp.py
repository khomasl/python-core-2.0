import re

text = "Вивчення Python може бути веселим."
pattern = "Python"
match = re.search(pattern, text)

if match:
    print("Знайдено:", match.group())
else:
    print("Не знайдено.")


pattern = r"в\w*м"
match = re.search(pattern, text, re.IGNORECASE)

if match:
    print("Знайдено:", match.group())


# знаходження електронної адреси в рядку.
text = "Моя електронна адреса: example@example.com"
pattern = r"\w+@\w+\.\w+" #мінімально необхідний патерн для пошуку електронної адреси
match = re.search(pattern, text)

if match:
    print("Електронна адреса:", match.group())


# вилучити ім'я користувача та домен цієї електронної адреси окремо.
email = "username@domain.com"
pattern = r"(\w+)@(\w+\.\w+)" #круглі дужки можуть бути корисними для групування та вилучення специфічних частин тексту в регулярних виразах.
match = re.search(pattern, email)

if match:
    user_name = match.group(1)
    domain_name = match.group(2)
    print("Ім'я користувача:", user_name)
    print("Домен:", domain_name)


# знайти всі числа у рядку (re.findall)
text = "Рік 2023 був складнішим, ніж 2022"
pattern = r"\d+"
matches = re.findall(pattern, text)

print(matches)


# зробити вибірка всіх слів в тексті.
text = "Python - це проста, але потужна мова програмування."
pattern = r"\w+" # пробіли не включаються, тому що \w відповідає лише буквам, цифрам та підкресленням. Якщо ви хочете включити слова з апострофами або дефісами, можна використовувати більш складний патерн, наприклад: r"\b\w[\w'-]*\b"
matches = re.findall(pattern, text)

print(matches)  # Виведе список всіх слів у рядку


# Видалимо всі пунктуаційні знаки з рядка.
text = "Python - потужна, універсальна; мова!"
pattern = r"[;,\-:!\.]"
replacement = ""
modified_text = re.sub(pattern, replacement, text)

print(modified_text)  


# форматування телефонних номерів.
phone = """
        Михайло Куліш: 050-171-1634
        Вікторія Кущ: 063-134-1729
        Оксана Гавриленко: 068-234-5612
        """
pattern = r"(\d{3})-(\d{3})-(\d{4})"
replacement = r"(\1) \2-\3"
formatted_phone = re.sub(pattern, replacement, phone)

print(formatted_phone)