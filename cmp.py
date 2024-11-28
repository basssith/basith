def custom_cmp(a, b):
    if a < b:
        return -1
    elif a > b:
        return 1
    else:
        return 0

# Example usage:
x = 5
y = 10
result = custom_cmp(x, y)
print(f"Comparison result of {x} and {y}: {result}")
