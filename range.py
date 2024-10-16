def calculate_range(numbers):
    if not numbers:  # Check if the list is empty
        return None
    return max(numbers) - min(numbers)

# Example usage:
data = [5, 3, 8, 1, 4]
result = calculate_range(data)
print("The range is:", result)
