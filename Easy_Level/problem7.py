def reverse_list(items):
    new_list = []
    new_position = len(items) - 1
    while new_position >= 0:
        new_list.append(items[new_position])
        new_position -= 1
        
    return new_list
print(reverse_list([1, 2, 3, 4]))
    
