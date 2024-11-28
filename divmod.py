def custom_divmod(a, b):
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    quotient = a // b
    remainder = a % b
    return quotient, remainder

# Example usage:
a = 10
b = 3
result = custom_divmod(a, b)
print(f"The quotient and remainder of {a} divided by {b} are: {result}")
