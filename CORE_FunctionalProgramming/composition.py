def square(a: int) -> int:
    return a * a


def multiply_by_ten(a: int) -> int:
    return a * 10


x = square(multiply_by_ten(5))
y = multiply_by_ten(square(5))

print(f"square(multiply_by_ten(5)): {x}")
print(f"multiply_by_ten(square(5)): {y}")