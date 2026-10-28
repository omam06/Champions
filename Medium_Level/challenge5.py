def most_frequent(numbers):
    if numbers is empty:
        return None

    create an empty dictionary called frequency

    for each number in numbers:
        if number is already in frequency:
            increase its frequency by 1
        otherwise:
            set its frequency to 1

    set most_common to the first number in numbers
    set highest_count to its frequency

    for each number in numbers:
        if its frequency is greater than highest_count:
            update most_common to that number
            update highest_count to its frequency

    return most_common