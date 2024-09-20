def is_substring(string: str, sub_string: str) -> bool:
    return sub_string in string


assert is_substring("Hello", "ell")
assert is_substring("123456789", "2345678")
assert not is_substring("Python", "ruby")
print("SUCCESS!")
