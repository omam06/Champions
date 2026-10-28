FUNCTION reverse_first(queue, k):
    if k is less than 0 OR k is greater than the queue length:
        return queue

    create an empty stack

    repeat k times:
        remove the front item from queue
        push that item onto stack

    while stack is not empty:
        pop an item from stack
        add that item to the back of queue

    repeat (queue length - k) times:
        remove the front item from queue
        add that item to the back of queue

    return queue