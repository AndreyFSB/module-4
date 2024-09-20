from typing import List


def my_range(stop: float, start=0.0, step=1.0) -> List[float]:
    result = []
    while start <= stop:
        result.append(start)
        start += step
    return result


# tests
assert my_range(0.6, step=0.2) == [0.0, 0.2, 0.4], f"Actual = {my_range(0.6, step=0.2)}"

res = [round(x, 1) for x in my_range(0.7, start=0.2, step=0.2)]
assert res == [0.2, 0.4, 0.6], f"Actual = {res}"

print("SUCCESS!")
