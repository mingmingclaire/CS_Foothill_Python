"""
CS3A, Assignment06, A Triple String Class
Mingming Gu
This program is using OOP to implement a class called TripleString, which consists of a few instance attribute and a few
instance methods to support those attributes.

No extra credit part
"""


class TripleString:
    """
    Encapsulates a triple-string object
    """

    # Class constants
    MIN_LEN = 1  # The inclusive minimum length for attribute string1, string2, and string3
    MAX_LEN = 100  # The inclusive maximum length for attribute string1, string2, and string3
    DEFAULT_STRING = "（undefined)"  # The default value for the string attributes

    # Initializer
    def __init__(self, string1, string2, string3):
        # This is the initializer that initializes all 3 instance attributes according to the parameters.
        self.string1 = string1  # could use anything, including None
        self.string2 = string2
        self.string3 = string3

        if not self.set_string1(string1):
            self.string1 = TripleString.DEFAULT_STRING

        if not self.set_string2(string2):
            self.string2 = TripleString.DEFAULT_STRING

        if not self.set_string3(string3):
            self.string3 = TripleString.DEFAULT_STRING

    # Setters
    def set_string1(self, the_str):
        # This is the setter for the instance attribute string1.
        if not self.validate_string(the_str):
            return False
        else:
            self.string1 = the_str
            return True

    def set_string2(self, the_str):
        # This is the setter for the instance attribute string2.
        if not self.validate_string(the_str):
            return False
        else:
            self.string2 = the_str
            return True

    def set_string3(self, the_str):
        # This is the setter for the instance attribute string3.
        if not self.validate_string(the_str):
            return False
        else:
            self.string3 = the_str
            return True

    # Getters
    def get_string1(self):
        return self.string1

    def get_string2(self):
        return self.string2

    def get_string3(self):
        return self.string3

    def __str__(self):
        # This method should return a str that contains information about the particular instance of the class.
        return (f"The value of string1 is {self.get_string1()}, while the value of string2 is {self.get_string2()}, \n" +
        f"and the value of string3 is {self.get_string3()}.")


    # Validate string method
    def validate_string(self, the_str):
        # This helper determines if the_str is valid.
        if TripleString.MIN_LEN <= len(the_str) <= TripleString.MAX_LEN:
            return True
        else:
            return False


def test():
    """ Tests for TripleString class """

    # Test Part 1
    s = "~" * 101
    t = ""
    ts1 = TripleString("a", "b", "c")
    ts2 = TripleString("sun", "moon", "star")
    ts3 = TripleString("@_@", "$$$$", s)
    ts4 = TripleString(t, s + "!", "0")

    # Test Part 2
    print(ts1.__str__())
    print(ts2.__str__())
    print(ts3.__str__())
    print(ts4.__str__())

    # Test Part 3
    # Pick ts4 for testing setter
    # Input a valid argument to string1
    ts4.set_string1("!")
    if ts4.get_string1() == "!":
        print(f"The setter set_string1('!') succeeds, expected. The new value set by the setter is {ts4.get_string1()}")
    else:
        print(f"The set_string1('!') fails, unexpected. The value from the getter is {ts4.get_string1()}")

    # Input an invalid argument to string2, the length is 101 > MAX_LEN
    ts4.set_string2("~" * 101)
    if ts4.get_string2() == "~" * 101:
        print(f"The setter set_string2('~' * 101) succeeds, expected. The new value set by the setter is {ts4.get_string2()}")
    else:
        print(f"The set_string2('~' * 101) fails, unexpected. The value from the getter is {ts4.get_string2()}")

    # Input an invalid argument to string3, the length is 0 < MIN_LEN
    ts4.set_string3("")
    if ts4.get_string3() == "":
        print(f"The setter set_string3('') succeeds, expected. The new value set by the setter is {ts4.get_string3()}")
    else:
        print(f"The set_string3('') fails, unexpected. The value from the getter is {ts4.get_string3()}")


# Test Part 4
    # Pick ts1 for testing setter
    # Input a valid argument to string1
    ts1.set_string1("aaa")
    if ts1.get_string1() == "aaa":
        print(f"The setter set_string1('aaa') succeeds, expected. The new value set by the setter is {ts1.get_string1()}")
    else:
        print(f"The set_string1('aaa') fails, unexpected. The value from the getter is {ts1.get_string1()}")

    # Input an invalid argument to string2, the length is 101 > MAX_LEN
    ts1.set_string2("b" * 120)
    if ts1.get_string2() == "b" * 120:
        print(f"The setter set_string2('b' * 120) succeeds, expected. The new value set by the setter is {ts1.get_string2()}")
    else:
        print(f"The set_string2('b' * 120) fails, unexpected. The value from the getter is {ts1.get_string2()}")

    # Input an invalid argument to string3, the length is 0 < MIN_LEN
    ts1.set_string3("")
    if ts1.get_string3() == "":
        print(f"The setter set_string3('') succeeds, expected. The new value set by the setter is {ts1.get_string3()}")
    else:
        print(f"The set_string3('') fails, unexpected. The value from the getter is {ts1.get_string3()}")


if __name__ == '__main__':
    test()


"""
Test Cases and Results

### Test Part 1 and Part 2 Result
### Instantiate four class instances with different values, valid and invalid, print out all instances by using __str__

"/Users/tjgumingming/Documents/De Anza/Foothill 2021/CS3A/venv/bin/python" "/Users/tjgumingming/Documents/De Anza/Foothill 2021/CS3A/assignment06.py"
The value of string1 is a, while the value of string2 is b, 
and the value of string3 is c.
The value of string1 is sun, while the value of string2 is moon, 
and the value of string3 is star.
The value of string1 is @_@, while the value of string2 is $$$$, 
and the value of string3 is （undefined).
The value of string1 is （undefined), while the value of string2 is （undefined), 
and the value of string3 is 0.


### Test Part 3 Result
### Pick one of the instances, which is ts4, and do three times of setter tests. Results are 

The setter set_string1('!') succeeds, expected. The new value set by the setter is !
The set_string2('~' * 101) fails, unexpected. The value from the getter is （undefined)
The set_string3('') fails, unexpected. The value from the getter is 0


### Test Part 4 Result
### Pick another instance, which is ts1, and do three times of setter tests. Results are 

The setter set_string1('aaa') succeeds, expected. The new value set by the setter is aaa
The set_string2('b' * 120) fails, unexpected. The value from the getter is b
The set_string3('') fails, unexpected. The value from the getter is c

###### All test cases pass!!

"""



