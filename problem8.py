def has_duplicates(numbers):
    seen_numbers = set()
    for number in numbers:
        if number in seen_numbers:
            return True
        seen_numbers.add(number)
    return False
print(has_duplicates([1, 2, 3, 2]))
print(has_duplicates([1, 2, 3, 4]))
print(has_duplicates([]))