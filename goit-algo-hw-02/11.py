def format_string(string, length):
    diff_len = length - len(string)
    if diff_len <= 0:
        return string
    else:
        left_space = diff_len // 2
        right_space = diff_len - left_space
        # return f"{'*' * space_count}{string}{'*' * (diff_len - space_count)}"
        return " " * left_space + string + " " * right_space
    
print(format_string("Hello", 10))  # Output: "  Hello   "
print(format_string("World!", 3))   # Output: "World"
print(format_string("abaa", 15))   # Output: " Python "