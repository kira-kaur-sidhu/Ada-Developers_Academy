def max_value(numbers):
    """ This function returns the largest number
        in the list.
    """

    largest_num = 0
    for num in numbers:
        if num > largest_num:
            largest_num = num
    return largest_num


if __name__ == "__main__":
    print(max_value([1, 12, 2, 42, 8, 3]))
