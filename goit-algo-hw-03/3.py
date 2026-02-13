import re

def normalize_phone(phone_number: str) -> str:
    digit_phone = ''
    for char in phone_number:
        if char.isdigit():
            digit_phone += char
    
    last_nine_digit = digit_phone[len(digit_phone)-9::]  
    formatted_phone = "+380" + last_nine_digit
    
    return formatted_phone


def normalize_phone_regexp(phone_number: str) -> str:
    # v1
    pattern = r"[\+.\d*]" 
    matches = re.findall(pattern, phone_number)
    modified_phone = "".join(matches)
    
    # v2
    pattern = r"[^\+\d]"
    replacement = ""
    modified_phone = re.sub(pattern, replacement, phone_number)

    formatted_phone = modified_phone 
    if not modified_phone.startswith("+"):
        if modified_phone.startswith("38"):
            formatted_phone = "+" + modified_phone
        else:    
            formatted_phone = "+38" + modified_phone
    
    return formatted_phone

raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

sanitized_numbers = [normalize_phone_regexp(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)
