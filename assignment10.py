"""
CS 3A  - Assignment 10, Contact List, part 2
Mingming Gu
This is part 2 of a 2-part project, in which we'll finish the features:
1. Search for a specific contact either by first name or last name
2. Print all contacts, sorted by either the first name or last name
Extra Credit:
3. find() multiple contacts: Search contacts by first name and last name together
4. Create main() function with a dictionary
"""


class Sorter:
    """
    This is the bubble sort presented in lectures, the only difference is
    that the two functions are now static methods of a class.
    """

    # TODO part 2: change whatever's necessary to sort by first/last name

    @staticmethod
    def float_largest_to_top(lst, size, by):
        swapped = False
        if by == ContactList.BY_FIRST_NAME:
            for i in range(size - 1):
                if lst[i].first_name > lst[i + 1].first_name:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = True
            return swapped
        elif by == ContactList.BY_LAST_NAME:
            for i in range(size - 1):
                if lst[i].last_name > lst[i + 1].last_name:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    swapped = True
            return swapped
        else:
            raise ValueError("Invalid value for by parameter, should be either BY_FIRST_NAME or BY_LAST_NAME")

    @staticmethod
    def sort(lst, by):
        size = len(lst)
        while Sorter.float_largest_to_top(lst, size, by):
            size -= 1
            Sorter.float_largest_to_top(lst, size, by)


class Contact:
    """
    This class represents a single contact (one person)
    """

    # TODO part 1: make email and phone optional parameters that default to None
    def __init__(self, first_name, last_name, email=None, phone=None):
        """
        This is the initializer for Contact class.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone

    def __str__(self):
        """
        Return a str that that shows all contact info
        """
        # TODO part 1: return a str that contains all 4 attributes
        # String preceded by f is called f-string, and is a more readable
        # way of incorporating information into a string than str.format()
        return (f"Name: {self._first_name} {self._last_name}\n"
                f"Email: {self._email}\n"
                f"Phone: {self._phone}\n")

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if type(first_name) != str:
            raise TypeError("Invalid first name, should be str")
        if len(first_name) == 0:
            raise ValueError("First name cannot be empty")
        self._first_name = first_name

    # TODO part 1: turn other attributes into properties with "Pythonic"
    # setter and getter
    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if type(last_name) != str:
            raise TypeError("Invalid last name, should be str")
        if len(last_name) == 0:
            raise ValueError("Last name cannot be empty")
        self._last_name = last_name

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, email):
        if type(email) != str and email is not None:
            raise TypeError("Invalid email address, should be str or None ")
        if type(email) == str and "@" not in email:
            raise ValueError("Email address should contain @")
        self._email = email

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, phone):
        if type(phone) != str and phone is not None:
            raise TypeError("Invalid phone number, should be str or None")
        if type(phone) == str and int(phone) <= 0:
            raise ValueError("Phone number should be a positive integer")
        self._phone = phone


class ContactList:
    """
    This class stores multiple contacts.
    """
    BY_FIRST_NAME = 1  # sort/find by first name
    BY_LAST_NAME = 2  # sort/find by last name
    By_FIRST_AND_LAST_NAME = 3  # sort/find by both first name and last name, for extra credit

    def __init__(self):
        """
        Creates a list of contacts, and also dict's that associated contacts with
        first names and last names
        """
        self._contacts = []

        # TODO part 2: add any necessary code to help search by first/last name
        self._contact_dict_first_name = {}
        self._contact_dict_last_name = {}
        # self._contact_dict_first_last_name = {}

    def clear(self):
        """
        Clear/remove all contacts
        :return:
        """
        self._contacts.clear()

        # TODO part 2: add any necessary code to clear all contacts
        self._contact_dict_first_name.clear()
        self._contact_dict_last_name.clear()

    @property
    def contacts(self):
        return self._contacts

    def add(self, contact):
        """
        Add a single contact (one person) to the internal data structures
        raise TypeError if contact is not an instance of class Contact
        """
        # TODO part 1: check type of contact, add contact to list of contacts
        if type(contact) != Contact:
            raise TypeError(f"Type of contact is not an instance of class Contact.")
        else:
            self._contacts.append(contact)
            # TODO part 2: add any necessary code to enable search by first/last name
            # Expected structure: contact_dict = {contact.first_name: [contact_1, contact_2]
            # if two contacts share one first_name}
            if contact.first_name not in self._contact_dict_first_name.keys():
                self._contact_dict_first_name[contact.first_name] = []
                self._contact_dict_first_name[contact.first_name].append(contact)
            # If duplicate first_name, only add new contact to value to the same key
            else:
                self._contact_dict_first_name[contact.first_name].append(contact)

            if contact.last_name not in self._contact_dict_last_name.keys():
                self._contact_dict_last_name[contact.last_name] = []
                self._contact_dict_last_name[contact.last_name].append(contact)
            else:
                self._contact_dict_last_name[contact.last_name].append(contact)

    def find(self, name, by):
        """
        Find a contact by the given name
        :param name: the first/last name, or first name & last name, of the contact to lookup, depend on by
        :param by: if BY_FIRST_NAME, name should be interpreted as the first name
                   if BY_LAST_NAME, name should be interpreted as the last name
        :return: an instance of Contact, the first_name/last_name attribute of which
                 matches name; if no match, returns None; if multiple, returns the first one

        With extra credit part
        :param by: if BY_FIRST_AND_LAST_NAME
        Approach: added BY_FIRST_AND_LAST_NAME option, find first_name in the self._contact_dict_first_name dictionary.
        If there are multiple results, use linear search to find by last_name in the result. Return the first found.
        """
        # TODO part 2: add any necessary code to enable search by first/last name

        try:
            if by == self.BY_FIRST_NAME:
                ary = self._contact_dict_first_name[name]
                if len(ary) == 1:
                    return ary[0]
                return ary[0]
            elif by == self.BY_LAST_NAME:
                ary = self._contact_dict_last_name[name]
                if len(ary) == 1:
                    return ary[0]
                return ary[0]
            elif by == self.By_FIRST_AND_LAST_NAME:
                # if len(name) != 2:
                #     raise ValueError("Invalid input, please enter both first and last name as two words.")
                # get the first/last name from user's input string
                get_first_name = name.split()[0]
                get_last_name = name.split()[1]
                ary = self._contact_dict_first_name[get_first_name]
                if len(ary) == 1:
                    if ary[0].last_name == get_last_name:
                        return ary[0]
                    return None
                else:
                    # Linear search
                    for i in range(len(ary)):
                        if ary[i].last_name != get_last_name:
                            i += 1
                        else:
                            return ary[i]
                    return None
            else:
                raise ValueError("Invalid, please find the contact either BY_FIRST_NAME or BY_LAST_NAME or both")
        except KeyError:
            return None

    def __str__(self, by=BY_FIRST_NAME):
        """
        Return a str that contains all contact, sorted by first names or
        last name, depending on the "by" parameter.
        It raises a ValueError if the "by" parameter contains invalid value.
        """
        # TODO part 1, return a string that contains all contacts in the list

        # TODO part 2: add any necessary code to handle sorting by first/last name
        Sorter.sort(self._contacts, by)
        return "\n".join(str(c) for c in self._contacts)


def get_choice():
    """
    Repeatedly prompts the user for an integer until they do so.
    :return: An integer choice.
    """
    while True:
        try:
            choice = int(input(
                "\n"
                "****** Contact List ******\n"
                "Please choose from the following actions:\n"
                "  1. Load contacts from file\n"
                "  2. Print all contacts, sorted by first name\n"
                "  3. Print all contacts, sorted by last name\n"
                "  4. Search all contacts by first name\n"
                "  5. Search all contacts by last name\n"
                "  6. Search all contacts by first name and last name\n"  # new choice for extra credit
                "  7. Quit\n"
                "Please enter your choice: "))
            return choice
        except:
            print("Invalid input")


def line_to_contact(line):
    """
    Convert a line of str of the form
        first_name,last_name[,email][,phone]
    to an instance of Contact
    :param line: the line to convert from
    :return: An instance of Contact
    :raise exception if the line doesn't have at least two comma-separated
           fields, or if any of the fields are invalid.
    """
    # TODO part 1: convert a line of str to an instance of Contact
    line_lst = [l.strip() for l in line.split(",")]
    contact = Contact(line_lst[0], line_lst[1])
    if len(line_lst) > 2:
        contact.email = line_lst[2]
    if len(line_lst) > 3:
        contact.phone = line_lst[3]

    return contact


def load_contacts_from_file(contact_list, filename):
    """
    Add all contacts contained in the file specified by filename to contact_list
    :param contact_list: instance of ContactList; new contacts should be added to it
    :param filename: name of file to read contacts from
    :return: None
    """
    # TODO part 1: add all contacts from file to contact list
    with open(filename) as read_csv:
        for row in read_csv:
            try:
                contact = line_to_contact(row)
                contact_list.add(contact)
            except ValueError:
                pass


def load_contacts(contact_list):
    """
    Prompts the user for the name of a file, and load contact from that file.
    """
    filename = input("Enter the name of the file to load: ")
    contact_list.clear()

    # TODO part 1: handle any exception raised by load_contacts_from_file() and
    # print it out.
    try:
        load_contacts_from_file(contact_list, filename)
        print("Loaded {} contacts from {}".format(len(contact_list.contacts), filename))
    except ValueError:
        print(f"Problem loading contacts: [Error 2] No such file or directory: '{filename}'")


def print_by_first_name(contact_list):
    print("\n" + contact_list.__str__(ContactList.BY_FIRST_NAME))


def print_by_last_name(contact_list):
    print("\n" + contact_list.__str__(ContactList.BY_LAST_NAME))


def find_contact(contact_list, by):
    name = input("Please enter the name to search: ")
    contact = contact_list.find(name, by)
    print("\n" + str(contact))


def find_by_first_name(contact_list):
    find_contact(contact_list, ContactList.BY_FIRST_NAME)


def find_by_last_name(contact_list):
    find_contact(contact_list, ContactList.BY_LAST_NAME)


def find_by_first_last_name(contact_list):  # new find function for extra credit
    find_contact(contact_list, ContactList.By_FIRST_AND_LAST_NAME)


def quit(contact_list):
    """
    Do cleanup and exit program; ok to use exit() in this function in this assignment.
    :param contact_list:
    :return: (Never, because it exits the program)
    """
    print("Bye!")
    exit(0)


def main():
    contact_list = ContactList()
    choice_dict = {1: load_contacts, 2: print_by_first_name,
                   3: print_by_last_name,
                   4: find_by_first_name, 5: find_by_last_name, 6: find_by_first_last_name,
                   7: quit}
    while True:
        choice = get_choice()

        if choice in range(1, 8):
            choice_dict[choice](contact_list)
        else:
            print("Invalid choice")

    #
    #     if choice == 1:
    #         load_contacts(contact_list)
    #     elif choice == 2:
    #         print_by_first_name(contact_list)
    #     elif choice == 3:
    #         print_by_last_name(contact_list)
    #     elif choice == 4:
    #         find_by_first_name(contact_list)
    #     elif choice == 5:
    #         find_by_last_name(contact_list)
    #     elif choice == 6:
    #         quit(contact_list)
    #     else:
    #         print("Invalid choice")


if __name__ == '__main__':
    main()



