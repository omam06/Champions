def missing_number(numbers):
    n = len(numbers)

    xpected_sum = n * (n + 1) // 2
    actual_sum = sum(numbers)

    return xpected_sum - actual_sum 
 
numbers = [9, 6, 4, 2, 3, 5, 7, 0, 1]
print(missing_number(numbers))
print(sum(numbers))