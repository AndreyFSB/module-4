import types


def my_range(stop: float, start=0.0, step=1.0):
    while start <= stop:
        yield start
        start += step


# tests
assert isinstance(my_range(1), types.GeneratorType)

res = list(my_range(0.6, step=0.2))
assert res, f"Actual = {res}"

res = [round(x, 1) for x in my_range(0.7, start=0.2, step=0.2)]
assert res == [0.2, 0.4, 0.6], f"Actual = {res}"

print("SUCCESS!")
