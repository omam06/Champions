Set low to 0
Set high to the last index
Set result to -1

While low <= high:
    Find the middle index

    If the middle value equals target:
        Save the middle index in result
        Continue searching the left half
    Else if the middle value is smaller than target:
        Search the right half
    Else:
        Search the left half

Return result