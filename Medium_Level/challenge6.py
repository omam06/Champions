def closest_number(numbers, target):
    if numbers == []:
        return None

    closest = numbers[0]

    for number in numbers:
        distance1 = abs(number - target)
        distance2 = abs(closest - target)

        if distance1 < distance2:
            closest = number

        elif (distance1 == distance2) and number < closest:
            closest = number

    return closest

print(closest_number([10, 8, 15, 20], 21))
print(closest_number([8, 12], 10))
