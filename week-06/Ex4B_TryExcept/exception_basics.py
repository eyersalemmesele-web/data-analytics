# Exercise 4.B Working with exceptions
# Lab 1 - Exception Basics

# in this lab i practiced using try and except blocks
# to handle different python errors without crashing the program
# ValueError

try:
    number = int("hello")

except ValueError:
    print("ValueError: cannot convert text into a number")

else:
    print(number)

finally:
    print("Let's try another one...\n")

# note:
# i created an example of a value error by trying to convert text into an integer



# NameError

try:
    fruit = banana

except NameError:
    print("NameError: variable is not defined")

else:
    print(fruit)

finally:
    print("Let's try another one...\n")

# note:
# i created a name error by using a variable that was not defined



# TypeError

try:
    total = "10" + 5

except TypeError:
    print("TypeError: cannot combine string and integer")

else:
    print(total)

finally:
    print("Let's try another one...\n")

# note:
# i created a type error by trying to add text and a number together



# SyntaxError

try:
    eval("if True print('hello')")

except SyntaxError:
    print("SyntaxError: invalid syntax in the code")

else:
    print("No syntax error")

finally:
    print("Let's try another one...\n")

# note:
# i created a syntax error using incorrect python syntax


# challenge question

# raise SystemExit(0) is used to stop the whole program completely
# it is different from break because break only stops a loop
# it may cause unexpected results if the program exits too early