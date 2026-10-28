def closest_number(numbers, target):
    if numbers is empty:
        return None

    set closest to the first number

    for each number in numbers:
        calculate the distance between number and target
        calculate the distance between closest and target

        if number's distance is smaller:
            update closest to number

        else if both distances are equal AND number is smaller than closest:
            update closest to number

    return closest