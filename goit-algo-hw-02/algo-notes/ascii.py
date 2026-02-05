def get_str_ascii_code_dict(input_str: str) -> dict:
    ascii_dict = {}
    for char in input_str:
        if char not in ascii_dict:
            ascii_dict[char] = ord(char)
    return ascii_dict

string = input("Введіть рядок: ")
ascii_mapping = get_str_ascii_code_dict(string)
print(ascii_mapping)