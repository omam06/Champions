def move_zero(numbers):
    zero_numbers = 0
    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[zero_numbers] = numbers[i]
            zero_numbers += 1
   
    for i in range(zero_numbers, len(numbers)):
        numbers[i] = 0
    return numbers
print(move_zero([0, 1, 0, 3, 12]))
print(move_zero([4, 0, 5, 0, 2]))
print(move_zero([1, 2, 3]))


FUNCTION balanced_brackets(text):
    CREATE an empty stack

    FOR each character in text:

        IF character is "(" OR "[" OR "{":
            ADD character to the stack

        ELSE IF character is ")" OR "]" OR "}":

            IF the stack is empty:
                RETURN False

            LOOK at the last opening bracket in the stack

            IF the opening bracket does not match the closing bracket:
                RETURN False

            REMOVE the last opening bracket from the stack

    IF the stack is empty:
        RETURN True
    OTHERWISE:
        RETURN False