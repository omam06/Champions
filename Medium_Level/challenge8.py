def insertion_sort_count(numbers):
    Make a copy of numbers
    Set shifts to 0

    for each index i from 1 to the last index:
        Save the current number as key
        Set j to i - 1

        while j >= 0 and the number at j > key:
            Move the number at j one position right
            Increase shifts by 1
            Decrease j by 1

        Put key into its correct position

    return the sorted list and shifts