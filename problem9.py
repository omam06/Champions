def first_duplicate(numbers):
    seen_numbers = set()
    for number in numbers:
        if number in seen_numbers:
            return number
        seen_numbers.add(number)
    
print(first_duplicate([4, 7, 2, 7, 5, 4]))
print(first_duplicate([1, 2, 3, 4]))
print(first_duplicate([5, 5, 3]))