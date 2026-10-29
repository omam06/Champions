def longest_consecutive(numbers):
    num_set = set(numbers)
    longest_sequence = 0

    for number in num_set:
        if number - 1 not in num_set:
            current = number
            length = 1

            while current + 1 in num_set:
                current += 1
                length += 1

            if length > longest_sequence:
                longest_sequence = length

    return longest_sequence

print(longest_consecutive([100, 6, 20, 1, 3]))
print(longest_consecutive([7, 12, 21, 17, 8, 13, 14]))