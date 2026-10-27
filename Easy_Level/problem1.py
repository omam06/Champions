def find_largest(numbers):
    if numbers == []:
        return None
    highest_number = numbers[0]
    for number in numbers:
        if number > highest_number:
            highest_number = number
    return highest_number
print(find_largest([3, 41, 56, 21, 76, 9]))
print(find_largest([-10, -5, -2, -18]))
print(find_largest([]))