def balanced_brackets(text):
    stack = []
    for character in text:
        if character == "(" or character == "[" or character == "{":
            stack.append(character)

        elif character == ")" or character == "]" or character == "}":
            if stack == []:
                return False
            
            stack[-1]

            if stack[0] != character[-1]:
                return False

            stack.pop()

    if stack == []:
        return True
    else:
        return False

print(balanced_brackets("(hello)"))
print(balanced_brackets("{[()]}"))


