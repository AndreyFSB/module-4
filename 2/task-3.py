def chain_sum(value: int = None):
    result = getattr(chain_sum, "result", 0)
    if value is None:
        chain_sum.result = 0
        return result
    chain_sum.result = value + result
    return chain_sum


assert chain_sum() == 0
assert chain_sum(5)() == 5
assert chain_sum(5)(10)() == 15
assert chain_sum(5)(10)(72)() == 87
print("SUCCESS!")
