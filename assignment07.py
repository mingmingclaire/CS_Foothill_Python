"""
CS3A, Assignment07, Slot Machine Simulation
Mingming Gu
This program will simulate a slot machine pull which generates from three strings.The user's winning is determined by his
original bet multiplied by the pay multiplier based on the pull result.
"""
import random

# TripleString class definition


class TripleString:
    """
    Encapsulates a triple-string object
    """

    # Class constants
    MIN_LEN = 1  # The inclusive minimum length for attribute string1, string2, and string3
    MAX_LEN = 100  # The inclusive maximum length for attribute string1, string2, and string3
    DEFAULT_STRING = "（undefined)"  # The default value for the string attributes
    NUM_INSTANCES = 0

    # Initializer
    def __init__(self, string1, string2, string3):
        # This is the initializer that initializes all 3 instance attributes according to the parameters.
        # Create a list to store 3 attributes together
        self.string = [self.DEFAULT_STRING] * 3
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
    def set_string_list(self, the_str, i):
        if not self.validate_string(the_str):
            return False
        else:
            self.string[i] = the_str
            return True

    def set_string1(self, the_str):
        # This is the setter for the instance attribute string1.
        return self.set_string_list(the_str, 0)

    def set_string2(self, the_str):
        # This is the setter for the instance attribute string2.
        return self.set_string_list(the_str, 1)

    def set_string3(self, the_str):
        # This is the setter for the instance attribute string3.
        return self.set_string_list(the_str, 2)

    # Getters
    def get_string1(self):
        return self.string[0]

    def get_string2(self):
        return self.string[1]

    def get_string3(self):
        return self.string[2]

    def __str__(self):
        # This method should return a str that contains information about the particular instance of the class.
        return f"The value of strings are {str(self.string)}."

    @classmethod
    def validate_string(cls, the_str):
        # This helper determines if the_str is valid.
        if cls.MIN_LEN <= len(the_str) <= cls.MAX_LEN:
            return True
        return False

    @classmethod
    def get_number_of_instances(cls):
        # This counts the number of instances of TripleString that have been created.
        cls.NUM_INSTANCES += 1
        return cls.NUM_INSTANCES


# Global symbolic constants
STR1 = "BAR"
STR2 = "cherries"
STR3 = "(space)"
STR4 = "7"
P1 = 38
P2 = 40
P3 = 7
P4 = 15
MIN_BET = 0
MAX_BET = 50
INVALID_VALUE = 0
MULTIPLIER = 0
MULTIPLIER_5 = 5
MULTIPLIER_15 = 15
MULTIPLIER_30 = 30
MULTIPLIER_50 = 50
MULTIPLIER_100 = 100


def get_bet():
    # This asks the user for the bet amount and returns it as an int, assume always integers.
    while True:
        bet_amount = int(input("How much would you like to bet (1 - 50) or 0 to quit? "))
        if bet_amount < INVALID_VALUE or bet_amount > 50:
            print("Invalid input.")
            continue
        else:
            return bet_amount


def rand_string():
    # This produces and returns a single random str based on probabilities
    num = random.randrange(100)
    if num < P1:
        return STR1
    elif P1 <= num < P1 + P2:
        return STR2
    elif P1 + P2 <= num < P1 + P2 + P3:
        return STR3
    else:
        return STR4


def pull():
    # This instantiates and returns a TripleString instance that represents a slot machine pull.
    rand_string1 = rand_string()
    rand_string2 = rand_string()
    rand_string3 = rand_string()
    pull_result = TripleString(rand_string1, rand_string2, rand_string3)
    return pull_result


def get_pay_multiplier(the_pull):
    # This determines the pay multiplier based on the pull result.
    if the_pull.string1 == STR2:
        if the_pull.string2 == STR2:
            if the_pull.string3 == STR2:
                return 30
            return 15
        return 5
    elif the_pull.string1 == the_pull.string2 == the_pull.string3 == STR1:
        return 50
    elif the_pull.string1 == the_pull.string2 == the_pull.string3 == STR4:
        return 100
    return MULTIPLIER


def display(the_pull, winnings):
    # This displays a message including the number of TripleString instances, three strings in the_pull, win/lose
    message1 = f"Whirrrrrr .... and your pull {TripleString.get_number_of_instances()} is ... \n"
    message2 = f"{the_pull.string1}, {the_pull.string2}, {the_pull.string3} \n"
    if get_pay_multiplier(the_pull) == 0:
        message3 = f"Sorry, you lose."
    else:
        message3 = f"Congratulations, you win: {winnings}."
    print(message1 + message2 + message3)


def main():
    while True:
        bet = get_bet()
        if bet != INVALID_VALUE:
            the_pull = pull()
            multiplier = get_pay_multiplier(the_pull)
            winnings = bet * multiplier
            display(the_pull, winnings)
            continue
        print("Bye!")
        exit()


if __name__ == '__main__':
    main()


"""
Test for functions
"""


def test_rand_string():
    str1_count = 0
    str2_count = 0
    str3_count = 0
    str4_count = 0
    for i in range(10000):
        str = rand_string()
        if str == STR1:
            str1_count += 1
        elif str == STR2:
            str2_count += 1
        elif str == STR3:
            str3_count += 1
        elif str == STR4:
            str4_count += 1

    print(str1_count, str2_count, str3_count, str4_count)

# test_rand_string()
# result is 3798 3972 699 1531


def test_get_bet():
    if 0 < get_bet() <= 50:
        print("True")
    else:
        print("False")

# test_get_bet()
# Result is True.


def test_pull():
    if pull().string1 in (STR1, STR2, STR3, STR4) and pull().string2 in (STR1, STR2, STR3, STR4) and pull().string3 in (STR1, STR2, STR3, STR4):
        print("True")
    else:
        print("False")

# test_pull()
# Result is True.


def test_get_pay_multiplier(the_pull):
    if get_pay_multiplier(the_pull) == MULTIPLIER_5:
        print(the_pull.string1 == "cherries" and the_pull.string2 != "cherries")
    elif get_pay_multiplier(the_pull) == MULTIPLIER_15:
        print(the_pull.string1 == "cherries" and the_pull.string2 == "cherries" and the_pull.string3 != "cherries")
    elif get_pay_multiplier(the_pull) == MULTIPLIER_30:
        print(the_pull.string1 == "cherries" and the_pull.string2 == "cherries" and the_pull.string3 == "cherries")
    elif get_pay_multiplier(the_pull) == MULTIPLIER_50:
        print(the_pull.string1 == "BAR" and the_pull.string2 == "BAR" and the_pull.string3 == "BAR")
    elif get_pay_multiplier(the_pull) == MULTIPLIER_100:
        print(the_pull.string1 == "7" and the_pull.string2 == "7" and the_pull.string3 == "7")
    elif get_pay_multiplier(the_pull) == MULTIPLIER:
        print("None of the pre-defined multipliers")

# test_get_pay_multiplier(pull())
# Result is True or "None of the pre-defined multipliers.
