"""
CS3A, Assignment05, Functions and lists
Mingming Gu
This program is aimed to use a few functions to extract some statistical information from a list of integers or
manipulate the list in some fashion.

Included Extra Credit 1
"""

def get_integers():
    """
    This function asks user to type a list of integers separated by space, and returns the list
    :return: a list of integers
    """
    while True:
        try:
            integers = input("Please type a list of integers, separated by space: ")
            integers = integers.split()
            integers = [ int(i) for i in integers ]
            return integers
        except ValueError as e:
            print("Bad input:", e)


def get_key():
    """
    This function asks user to type in a single key integer, and returns the number
    :return: an integer
    """
    while True:
        try:
            key = int(input("Please enter the key number: "))
            return key
        except ValueError as e:
            print("Bad input:", e)


def add_all(integers):
    """
    This function returns the sum of all the integers, and returns 0 if the list is empty.
    :return: an integer
    """
    sum = 0
    if integers == []:
        return 0
    else:
        for num in integers:
            sum += num
        return sum


def average(integers):
    """
    This function returns the average of the integers in the list, which should be a float and the no rounding.
    :return: a float number
    """
    if integers == []:
        return None
    else:
        return add_all(integers) / len(integers)


def minmax(integers):
    """
    This function returns a tuple containing the smallest and the largest integer (in this order) in the list.
    If integers is an empty list, it returns a tuple of (None, None).
    :return: a tuple with two numbers
    """

    if integers == []:
        return (None, None)
    else:
        minimum = integers[0]
        maximum = integers[0]
        for i in integers[1:]:
            if i < minimum:
                minimum = i
            else:
                if i > maximum:
                    maximum = i
        return (minimum, maximum)


def count_key(integers, key):
    """
    This function counts and returns the number of times key appears in the given list of integers.
    :return: an integer representing the counts of appearance
    """
    count = 0
    for i in integers:
        if i == key:
            count += 1
    return count


def is_in(integers, key):
    """
    This function returns True if the key is in the integers list, False otherwise.
    :return: a boolean representing whether the key is in the list
    """
    i = 0
    while i < len(integers):
        if integers[i] == key:
            return True
            break
        else:
            i += 1
    return False


def double(integers):
    """
    This function returns a new list that contains doubles of all the integers in the given list.
    :return: a list with doubles of all original elements
    """
    new_list = []
    new_list = [element * 2 for element in integers]
    return new_list


def mask(integers, key):
    """
    This function replaces every occurrence of key in integers with "None" in-place
    :return: a list after modification
    """
    i = 0
    while i < len(integers):
        if integers[i] == key:
            integers[i] = None
            i += 1
        i += 1
    return integers

def main():
    """
    This is the main driver of this program, which call the first two functions and obtain a list of integers and key
    for the following implementation.
    :return: all the required outputs
    """
    integers = get_integers()
    key = get_key()
    print(f"Integers is {integers}; key is {key}")

    sum_list = add_all(integers)
    print(f"Sum is {sum_list}")

    avg_list = average(integers)
    print(f"Average is {avg_list}")

    minmax_list = minmax(integers)
    print(f"Smallest is {minmax_list[0]}; largest is {minmax_list[1]}")

    countkey = count_key(integers, key)
    print(f"{key} occurs {countkey} times")

    is_check = is_in(integers, key)
    if is_check == True:
        print(f"{key} is in the list")
    else:
        print(f"{key} is not in the list")

    double_list = double(integers)
    print(f"Result of doubling integers is {double_list}")

    masked_list = mask(integers, key)
    print(f"Result of masking {key} in integers is {masked_list}")


if __name__ == '__main__':
    main()


'''
EXTRA CREDIT PORTION
'''
def get_nonint():
    """
    This function asks user to type a list of non-integers separated by space, and returns the list
    :return: a list of non-integers
    """
    while True:
        try:
            lst = input("Please type a list of non-integers, separated by space: ")
            lst = lst.split()
            return lst
        except ValueError as e:
            print("Bad input:", e)


def get_value():
    """
    This function asks user to type in a single key value, and returns the value
    :return: a value/object
    """
    while True:
        try:
            key = input("Please enter the key object: ")
            return key
        except ValueError as e:
            print("Bad input:", e)


def extra_credit1():
    """
    The above functions may work for list of non-int. This function is to show the "count_key" function can also work
    for non-int, but ONLY IF the get_integers() and get_key() are modified.
    After changing them, this function would work for non-int or non-float because it can also count number of occurrence of such objects.
    :return: an integer representing the counts of appearance
    """
    count = 0
    for i in list:
        if i == key:
            count += 1
    return count

list = get_nonint()
key = get_value()
result1 = extra_credit1()
print(f"{key} occurs {result1} times")


"""
Test Cases and Results

### Case 1: empty list
### Case Run 1 Output

"/Users/tjgumingming/Documents/De Anza/Foothill 2021/CS3A/venv/bin/python" "/Users/tjgumingming/Documents/De Anza/Foothill 2021/CS3A/assignment05.py"
Please type a list of integers, separated by space: 
Please enter the key number: 0
Integers is []; key is 0
Sum is 0
Average is None
Smallest is None; largest is None
0 occurs 0 times
0 is not in the list
Result of doubling integers is []
Result of masking 0 in integers is []

Process finished with exit code 0


### Case 2: list with one integer
### Case Run 2 Output

"/Users/tjgumingming/Documents/De Anza/Foothill 2021/CS3A/venv/bin/python" "/Users/tjgumingming/Documents/De Anza/Foothill 2021/CS3A/assignment05.py"
Please type a list of integers, separated by space: 99
Please enter the key number: 9
Integers is [99]; key is 9
Sum is 99
Average is 99.0
Smallest is 99; largest is 99
9 occurs 0 times
9 is not in the list
Result of doubling integers is [198]
Result of masking 9 in integers is [99]

Process finished with exit code 0


### Case 3: list with multiple integers, both positive and negative
### Case Run 3 Output

"/Users/tjgumingming/Documents/De Anza/Foothill 2021/CS3A/venv/bin/python" "/Users/tjgumingming/Documents/De Anza/Foothill 2021/CS3A/assignment05.py"
Please type a list of integers, separated by space: 8 13 2 0 -6 -37 0 13
Please enter the key number: 13
Integers is [8, 13, 2, 0, -6, -37, 0, 13]; key is 13
Sum is -7
Average is -0.875
Smallest is -37; largest is 13
13 occurs 2 times
13 is in the list
Result of doubling integers is [16, 26, 4, 0, -12, -74, 0, 26]
Result of masking 13 in integers is [8, None, 2, 0, -6, -37, 0, None]

Process finished with exit code 0


### Case 4: error input for integers and key
### Case Run 4 Output

"/Users/tjgumingming/Documents/De Anza/Foothill 2021/CS3A/venv/bin/python" "/Users/tjgumingming/Documents/De Anza/Foothill 2021/CS3A/assignment05.py"
Please type a list of integers, separated by space: 9 -11 23 87 -60 10.0 11
Bad input: invalid literal for int() with base 10: '10.0'
Please type a list of integers, separated by space: 9 -11 23 87 -60 10 11
Please enter the key number: -11.0
Bad input: invalid literal for int() with base 10: '-11.0'
Please enter the key number: -11
Integers is [9, -11, 23, 87, -60, 10, 11]; key is -11
Sum is 69
Average is 9.857142857142858
Smallest is -60; largest is 87
-11 occurs 1 times
-11 is in the list
Result of doubling integers is [18, -22, 46, 174, -120, 20, 22]
Result of masking -11 in integers is [9, None, 23, 87, -60, 10, 11]

Process finished with exit code 0

### Case 5: EXTRA CREDIT 1
### Case Run 5 Output

"/Users/tjgumingming/Documents/De Anza/Foothill 2021/CS3A/venv/bin/python" "/Users/tjgumingming/Documents/De Anza/Foothill 2021/CS3A/assignment05.py"
Please type a list of non-integers, separated by space: Hello test "1" False "yes" yes "1"
Please enter the key object: "1"
"1" occurs 2 times

Process finished with exit code 0


###### All test cases pass!!

"""