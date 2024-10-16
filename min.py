def find_min(numbers):
    if not numbers:
        return None  # Return None if the list is empty
    min_value = numbers[0]
    for num in numbers:
        if num < min_value:
            min_value = num
    return min_value

# Example usage:
numbers = [3, 5, 1, 8, 2]
min_number = find_min(numbers)
print("The minimum number is:", min_number)
