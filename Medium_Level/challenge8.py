def insertion_sort_count(numbers):
    sorted_numbers = numbers.copy()
    number_of_shifts = 0

    for index in range(1, len(sorted_numbers)):
        current_number = sorted_numbers[index]

        left = index - 1

        while left >= 0 and sorted_numbers[left] > current_number:
            sorted_numbers[left + 1] = sorted_numbers[left]
            number_of_shifts += 1
            left -= 1
        sorted_numbers[left + 1] = current_number

    return sorted_numbers, number_of_shifts

print(insertion_sort_count([5, 3, 4]))
print(insertion_sort_count([-12, 21, 0, -1]))
print(insertion_sort_count([]))