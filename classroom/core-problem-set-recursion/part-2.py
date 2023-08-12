# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# search
def search(array, query):
    if len(array) == 0:
        return False
    elif array[0] == query:
        return True
    return search(array[1:], query)


# is_palindrome
def is_palindrome(text):
    if len(text) == 1:
        return True
    elif text[0] != text[-1]:
        return False
    return is_palindrome(text[1:-1])


# digit_match
def digit_match(digit1, digit2):
    count = 0
    str_digit1 = str(digit1)
    str_digit2 = str(digit2)
    def check(digit1, digit2, count):
        if digit1 == "" or digit2 == "":
            return count
        elif digit1[-1] == digit2[-1]:
            count += 1
        return check(digit1[:-1], digit2[:-1], count)
    
    return check(str_digit1, str_digit2, count)
