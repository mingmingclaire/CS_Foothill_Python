"""
CS3A, Assignment04, Free Frozen Yogurt
Mingming Gu
This program is aimed to run a purchase-and-award system on yogurts buying for customers.
"""
# Define a constant for the number of stamps that qualifies for a free yogurt, initialized to be 7
stamps_for_free = 7

# Define a variable to represent the balance of customer's stamp, initialized to be 0
stamp_balance = 0

while True:
    action = input("Menu: \n"
                   + "P (process Purchase) \n"
                   + "S (Shut down) \n"
                   + "Your Choice: ")
    if action[0] not in ("p", "P", "s", "S"):
        print("*** Use P or S, please ***.")
        continue

    if action[0] in ("s", "S"):
        break

    if stamp_balance < 7: # Normal transaction
        while True:
            num_purchase = int(input("How many yogurts would you like to buy? "))
            if num_purchase <= 0:
                print("*** Invalid # yogurts. ***")
                continue
            else:
                stamp_balance += num_purchase
                print("You have just earned " + str(num_purchase) + " stamps and have a total of " + str(stamp_balance) + " to use.")
                break
    else: # Execute an award transaction
        while True:
            boolean_answer = input("You qualify for a free yogurt. Would you like to use your stamps? (Y or N) ")
            if boolean_answer[0] not in ("Y", "y", "N", "n"):
                print("*** Invalid answer, please enter 'Y' or 'N' ***")
                continue
            if boolean_answer[0] in ("Y", "y"):
                stamp_balance -= 7
                print("You have just used 7 stamps and have " + str(stamp_balance) + " left. \n"
                    + "Enjoy your free yogurt.")
                break
            else: # Normal transaction
                while True:
                    num_purchase = int(input("How many yogurts would you like to buy? "))
                    if num_purchase <= 0:
                        print("*** Invalid # yogurts. ***")
                        continue
                    else:
                        stamp_balance += num_purchase
                        print("You have just earned " + str(num_purchase) + " stamps and have a total of " + str(stamp_balance) + " to use.")
                        break


"""
Test Cases and Results

### Case Run 1 Output

"/Users/tjgumingming/Documents/De Anza/Foothill 2021/pythonProject4/venv/bin/python" "/Users/tjgumingming/Documents/De Anza/Foothill 2021/CS3A/assignment04.py"
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: p
How many yogurts would you like to buy? 4
You have just earned 4 stamps and have a total of 4 to use.
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: no
*** Use P or S, please ***.
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: P
How many yogurts would you like to buy? 11
You have just earned 11 stamps and have a total of 15 to use.
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: P
You qualify for a free yogurt. Would you like to use your stamps? (Y or N) don't know
*** Invalid answer, please enter 'Y' or 'N' ***
You qualify for a free yogurt. Would you like to use your stamps? (Y or N) y
You have just used 7 stamps and have 8 left. 
Enjoy your free yogurt.
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: Purchase
You qualify for a free yogurt. Would you like to use your stamps? (Y or N) n
How many yogurts would you like to buy? 2
You have just earned 2 stamps and have a total of 10 to use.
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: p
You qualify for a free yogurt. Would you like to use your stamps? (Y or N) y
You have just used 7 stamps and have 3 left. 
Enjoy your free yogurt.
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: s

Process finished with exit code 0

### Conclusion: Case 1 PASSES

### Case Run 2 Output

"/Users/tjgumingming/Documents/De Anza/Foothill 2021/pythonProject4/venv/bin/python" "/Users/tjgumingming/Documents/De Anza/Foothill 2021/CS3A/assignment04.py"
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: yes
*** Use P or S, please ***.
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: p
How many yogurts would you like to buy? 20
You have just earned 20 stamps and have a total of 20 to use.
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: p
You qualify for a free yogurt. Would you like to use your stamps? (Y or N) yes
You have just used 7 stamps and have 13 left. 
Enjoy your free yogurt.
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: process Purchase
You qualify for a free yogurt. Would you like to use your stamps? (Y or N) y
You have just used 7 stamps and have 6 left. 
Enjoy your free yogurt.
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: purchase
How many yogurts would you like to buy? -6
*** Invalid # yogurts. ***
How many yogurts would you like to buy? 0
*** Invalid # yogurts. ***
How many yogurts would you like to buy? 3
You have just earned 3 stamps and have a total of 9 to use.
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: p
You qualify for a free yogurt. Would you like to use your stamps? (Y or N) nope
How many yogurts would you like to buy? 1
You have just earned 1 stamps and have a total of 10 to use.
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: s

Process finished with exit code 0

### Conclusion: Case 2 PASSES

### Case Run 3 Output

"/Users/tjgumingming/Documents/De Anza/Foothill 2021/pythonProject4/venv/bin/python" "/Users/tjgumingming/Documents/De Anza/Foothill 2021/CS3A/assignment04.py"
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: p
How many yogurts would you like to buy? 2
You have just earned 2 stamps and have a total of 2 to use.
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: first
*** Use P or S, please ***.
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: p
How many yogurts would you like to buy? 01
You have just earned 1 stamps and have a total of 3 to use.
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: pur
How many yogurts would you like to buy? 06
You have just earned 6 stamps and have a total of 9 to use.
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: p
You qualify for a free yogurt. Would you like to use your stamps? (Y or N) no
How many yogurts would you like to buy? -2
*** Invalid # yogurts. ***
How many yogurts would you like to buy? 0
*** Invalid # yogurts. ***
How many yogurts would you like to buy? 3
You have just earned 3 stamps and have a total of 12 to use.
You qualify for a free yogurt. Would you like to use your stamps? (Y or N) y
You have just used 7 stamps and have 5 left. 
Enjoy your free yogurt.
Menu: 
P (process Purchase) 
S (Shut down) 
Your Choice: s

Process finished with exit code 0

### Conclusion: Case 3 PASSES
###### All test cases pass!!

"""











