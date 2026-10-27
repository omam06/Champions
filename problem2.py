def find_smallest(numbers):
    if numbers == []:
        return None
    smallest_number = numbers[0]
    for number in numbers:
        if number < smallest_number:
            smallest_number = number
    return smallest_number
print(find_smallest([8, 3, 12, 1, 7]))
print(find_smallest([-3, -10, -1, -6]))