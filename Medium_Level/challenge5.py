def most_frequent(numbers):
    if numbers == []:
        return None

    frequency = {}

    for number in numbers:
        if number in frequency:
            frequency[number] += 1
        else:
            frequency[number] = 1

    most_common_number = numbers[0]
    highest_count = frequency[most_common_number]

    for number in numbers:
        if frequency[number] > highest_count:
            most_common_number = frequency[number]
            highest_count = frequency[most_common_number]

    return most_common_number

print(most_frequent([2, 5, 2, 8, 2, 5]))
print(most_frequent([4, 7, 7, 4]))
print(most_frequent([1, 2, 3, 4, 32]))