def reverse_first(queue, k):
    if k < 0 or k > len(queue):
        return queue

    stack = []
    for index in range(k):
        first_item = queue.pop(0)
        stack.append(first_item)

    while stack != []:
        popped_item = stack.pop()
        queue.append(popped_item)
        
    for index in range(len(queue) - k):
        rmv_item = queue.pop(0)
        queue.append(rmv_item)
    
    return queue

print(reverse_first([10, 20, 30, 40, 50], 3))
print(reverse_first([1, 2, 3, 4], 2))
print(reverse_first([2, 21, 22, 3], 4))