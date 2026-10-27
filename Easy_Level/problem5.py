def count_occurrences(numbers, target):
    count = 0
    for number in numbers:
        if number == target:
            count +=1
    return count
print(count_occurrences([2, 5, 2, 8, 2], 2))
print(count_occurrences([2, 5, 2, 8, 2], 10))
