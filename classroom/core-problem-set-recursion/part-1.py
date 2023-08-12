# There are comments with the names of
# the required functions to build.
# Please paste your solution underneath
# the appropriate comment.

# factorial
def factorial(n):
    if n >= 0:
        if n == 0:
            return 1
        return n * factorial(n-1)
    else:
        raise ValueError


# reverse
def reverse(s):
    if len(s) <= 1:
        return s
    
    first_letter = s[0]
    rest = s[1:]
    
    return reverse(rest) + first_letter


# bunny
def bunny(count):
    if not count:
        return count
    else:
        return 2 + bunny(count-1)


# is_nested_parens
def is_nested_parens(parens):
    if parens == "":
        return True
    elif "()" in parens:
        new_parens = parens.replace("()", "")
        return is_nested_parens(new_parens)
    else:
        return False
    
