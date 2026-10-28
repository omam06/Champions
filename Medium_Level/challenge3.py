def balanced_brackets(text):
    pairs = {")": "(", "]": "[", "}": "{"}
    stack = []
    for character in text:
        if character == "(" or character == "[" or character == "{":
            stack.append(character)

        elif character == ")" or character == "]" or character == "}":
            if stack == []:
                return False
            
            if stack[-1] != pairs[character]:
                return False

            stack.pop()

    if stack == []:
        return True
    else:
        return False

print(balanced_brackets("(hello)"))
print(balanced_brackets("{[()]}"))
print(balanced_brackets("([)]"))
print(balanced_brackets("((hello)"))