def to_snake_case(value: str) -> str:
    return "_".join(value.lower().split())


assert to_snake_case("Some text") == "some_text"
assert to_snake_case("V for Vendetta") == "v_for_vendetta"
assert to_snake_case("Horizon zero dawn") == "horizon_zero_dawn"
print("SUCCESS!")
