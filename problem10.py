def move_zeros(numbers):
    zero_numbers = 0
    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[zero_numbers] = numbers[i]
            zero_numbers += 1
   
    for i in range(zero_numbers, len(numbers)):
        numbers[i] = 0
    return numbers
print(move_zeros([0, 1, 0, 3, 12]))
print(move_zeros([1, 2, 3]))
print(move_zeros([0, 0, 5]))