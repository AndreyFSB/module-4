def to_string(value, indent=0):
    result = []
    if isinstance(value, dict):
        for key, value in value.items():
            row = f'\n{" " * indent}{key}:{to_string(value, indent + 2)}'
            result.append(row)
    elif isinstance(value, list):
        result.append(f"array={value}")
    else:
        result.append(f"value={value}")
    return "".join(result)


data = {
    "key": [1, 2, 3],
    "key2": {"key1": 56, "key2": [1, 2, 3, 4, 5], "key3": {"key1": 56, "key2": []}},
}


expected_result = """
key:array=[1, 2, 3]
key2:
  key1:value=56
  key2:array=[1, 2, 3, 4, 5]
  key3:
    key1:value=56
    key2:array=[]"""

assert to_string(data) == expected_result
print("SUCCESS!")
