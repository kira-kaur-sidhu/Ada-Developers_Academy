# Functions

Each student should select **one** of the following tests, implement the function **in a new branch** and push that branch up to github.  Then create a pull request.

## Function One: `twoSum`

`twoSum` is a function which finds which two numbers in a list of numbers add up to the given target.

```py
def twoSum(n, t):
    for i in range(len(n)):
        for j in range(i + 1, len(n)):
            if n[j] == t - n[i]:
                return [i, j]
```

### Tests

```py
import pytest
from functions.two_sum import twoSum

def test_returns_0_1_for_2_7_11_15_with_target_9():
    # Arrange
    n = [2, 7, 11, 15]
    t = 9

    # Act
    answer = twoSum(n, t)

    # Assert
    assert answer == [0, 1]


def test_returns_1_2_for_3_2_4_with_target_6():
    # Arrange
    n = [3, 2, 4]
    t = 6

    # Act
    answer = twoSum(n, t)

    # Assert
    assert answer == [1, 2]


def test_returns_0_1_for_3_3_with_target_6():
    # Arrange
    n = [3, 3]
    t = 6

    # Act
    answer = twoSum(n, t)

    # Assert
    assert answer == [0, 1]
```

*Taken from [Leetcode: Two Sum](https://leetcode.com/problems/two-sum/)*

## Function Two: `palindrome_number`

`palindrome_number` is a function which finds returns true if the given number's digits can be reversed resulting in the same number.  For example 121 is a palindrome number but 123 is not (321 != 123).


```py
def palindrome_number(x):
  temp = x
  reverse = 0
  while(x>0):
    dig = x%10
    reverse = reverse*10 + dig
    x = x//10

    if temp == reverse:
      return True
    else:
      return False
```

### Tests

```py
import pytest
from functions.palindrome_number import palindrome_number

def test_returns_true_for_99():
    # Arrange
    n = 99

    # Act
    answer = palindrome_number(99)

    # Assert
    assert answer == True


def test_returns_true_for_151():
    # Arrange
    n = 151

    # Act
    answer = palindrome_number(n)

    # Assert
    assert answer == True


def test_returns_false_for_123():
    # Arrange
    n = 123

    # Act
    answer = palindrome_number(123)

    # Assert
    assert answer == False
```

## Function Three: `merge_sorted_arrays`

```py
def merge_sorted_lists(l1, l2):
    merged = l1 + l2

    return sorted(merged)
```

### Tests

```py
import pytest
from functions.merge_sorted_lists import merge_sorted_lists


def test_for_1_and_2():
    # Arrange
    l1 = [1]
    l2 = [2]

    # Act
    answer = merge_sorted_lists(l1, l2)

    # Assert
    assert answer == [1, 2]


def test_for_2_and_1():
    # Arrange
    l1 = [2]
    l2 = [1]

    # Act
    answer = merge_sorted_lists(l1, l2)

    # Assert
    assert answer == [1, 2]


def test_for_1_2_3_and_4_5_6():
    # Arrange
    l1 = [1, 2, 3]
    l2 = [4, 5, 6]

    # Act
    answer = merge_sorted_lists(l1, l2)

    # Assert
    assert answer == [1, 2, 3, 4, 5, 6]
```
