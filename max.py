def find_max(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    max_value = numbers[0]
    for num in numbers:
        if num > max_value:
            max_value = num
    return max_value

# Example usage:
numbers = [3, 5, 1, 8, 2]
max_number = find_max(numbers)
print("The maximum number is:", max_number)
