"""
CS3A, Assignment08, String reversal, etc
Mingming Gu
This assignment will use three techniques -- iteration, stack, and recursion -- to solve a problem, reversing a string.
"""


class Reverser:

    @staticmethod
    def reverse_str_iter(string):
        """
        This method uses iteration with a for/while loop to reverse the string. If must iterate the string starting at
        the first character forward.

        :param string: a string
        :return: a reversed string
        """
        new_string = ""
        for i in range(len(string)):
            new_string += string[len(string) - i - 1]
        return new_string

    @staticmethod
    def reverse_str_stack(string):
        """
        This method uses a stack to reverse the string. Will use list as a stack, list.append() and list.pop().

        :param string: a string
        :return: a reversed string
        """
        stack = []
        new_stack = []
        new_string = ""
        for i in range(len(string)):
            stack.append(string[i])
        for i in range(len(stack)):
            new_stack.append(stack.pop())
        for i in range(len(new_stack)):
            new_string += new_stack[i]
        return new_string

    @staticmethod
    def reverse_str_rec(string):
        """
        This method uses recursion to reverse the string.
        It must have a base case. It must call itself. It must utilize the result returned by the recursive call.
        :param string: a string
        :return: a reversed string

        ###  Comment: By testing around, the length of thg longest string it can handle is 997. ###
        """
        if len(string) == 0:
            return string
        return Reverser.reverse_str_rec(string[1:]) + string[0]

    @staticmethod
    def reverse_str_builtin(string):
        """
        This method uses Python's builtin way to reverse the string, with one line function.
        :param string: a string
        :return: a reversed string
        """
        return "".join(reversed(string))


def remove_char(string, char):
    """
    This function should return a new str that's the same as the parameter string with all occurrences of char removed.
    :param string: a string
    :param char: a character as a string
    :return: a new string after removal
    """
    if len(string) == 0:
        return string
    if string[0] == char:
        return remove_char(string[1:], char)
    else:
        return string[0] + remove_char(string[1:], char)


"""
Reverser tests
"""


def test():
    """
    A global function that tests all 4 methods above.
    :return: a list with 4 reverted strings

    Comment: By running performance tests, reverse_str_builtin() is the fastest method, reverse_str_rec() is the
    slowest method. Intuitively, the built-in function can finish reversion in one step by running the function,
    whereas recursion implements the function n times, where n is the length of the string, so the latter takes longer.
    """
    long_string = "l" + "o" * 993 + "ng"
    test_lst = ["", "x", "Reverse the string in four methods.", long_string]
    reverse_ten = Reverser.reverse_str_iter("Reverse the string in four methods.")
    reverse_long = Reverser.reverse_str_rec(long_string)
    expect_result = ["", "x", reverse_ten, reverse_long]

    result_iter = []
    result_stack = []
    result_rec = []
    result_builtin = []

    for ts in test_lst:
        result_iter.append(Reverser.reverse_str_iter(ts))
        result_stack.append(Reverser.reverse_str_stack(ts))
        result_rec.append(Reverser.reverse_str_rec(ts))
        result_builtin.append(Reverser.reverse_str_builtin(ts))
    print(
        "Print out four lists by using four different methods, stating if each result is correct(True) or not(False).")
    print(
        f"The result of iteration method is {result_iter}, and it is {result_iter[0] == expect_result[0]} as expected.")
    print(f"The result of stack method is {result_stack}, and it is {result_stack[1] == expect_result[1]} as expected.")
    print(f"The result of recursion method is {result_rec}, and it is {result_rec[2] == expect_result[2]} as expected.")
    print(f"The result of builtin method is {result_builtin}, and it is {result_builtin[3] == expect_result[3]} as "
          f"expected.")

    """
    Reverser performance testing
    """
    import time

    start = time.perf_counter()
    for ts in test_lst:
        result_iter.append(Reverser.reverse_str_iter(ts))
    duration_iter = time.perf_counter() - start
    print(f"Using iteration method takes {duration_iter:.5f}")

    start = time.perf_counter()
    for ts in test_lst:
        result_stack.append(Reverser.reverse_str_stack(ts))
    duration_stack = time.perf_counter() - start
    print(f"Using stack method takes {duration_stack:.5f}")

    start = time.perf_counter()
    for ts in test_lst:
        result_rec.append(Reverser.reverse_str_rec(ts))
    duration_rec = time.perf_counter() - start
    print(f"Using recursion method takes {duration_rec:.5f}")

    start = time.perf_counter()
    for ts in test_lst:
        result_builtin.append(Reverser.reverse_str_builtin(ts))
    duration_builtin = time.perf_counter() - start
    print(f"Using builtin method takes {duration_builtin:.5f}")


"""
remove_char() testing
"""


def remove_char_test(string, char):
    """
    This function tests remove_char() function.
    :return: Pass or Not Pass
    """
    result = remove_char(string, char)
    if not string:
        if result == string:
            print("Pass")
        else:
            print("Not Pass")
    else:
        if (s != char for s in result):
            print("Pass")
        else:
            print("Not Pass")


if __name__ == '__main__':
    test()
    remove_char_test("good", "o")
    remove_char_test("!Hello!", "!")  # when char is a symbol.
    remove_char_test("", "a")  # when string is empty.
    remove_char_test("Here I am.", " ")  # when char is a space.
    remove_char_test("I buy a china in China", "C")  # when there are both small case and large case of a same char.
