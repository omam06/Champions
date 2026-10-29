def two_sum(numbers, target):
    seen = {}

    for i in range(0, len(numbers)):
        current_number = numbers[i]
        needed_number = target - current_number


        if needed_number in seen:
            return [seen[needed_number], i]

        seen[current_number] = i

    return None

print(two_sum([2, 7, 11, 15, 7], 9))
print(two_sum([], 3))