def first_position(numbers, target):
    left = 0
    right = len(numbers) - 1
    result = -1

    while left <= right:
        middle = (left + right) // 2

        if numbers[middle] == target:
            result = middle
            right = middle - 1
        elif numbers[middle] < target:
            left = middle + 1
        else:
            right = middle - 1

    return result

print(first_position([2, 4, 4, 4, 8, 10], 4))
print(first_position([1, 3, 5, 7], 6))