def second__largest(numbers):
    highest_number = None
    second_highest = None
    for number in numbers:
        if highest_number is None or number > highest_number:
            if number != highest_number:
                second_highest = highest_number
            highest_number = number

        elif number != highest_number:
            if second_highest is None or number > second_highest:
                second_highest = number

    return second_highest 
    
print(second__largest([10, 5, 8, 10, 3, 7, 9]))
print(second__largest([4, 4, 4]))
print(second__largest([-5, -2, -8, -3]))

