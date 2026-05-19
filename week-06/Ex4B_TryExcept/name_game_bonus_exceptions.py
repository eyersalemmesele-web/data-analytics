# Exercise 4.B Working with exceptions
# Lab 2 - name_game_bonus_exceptions.py

# in this lab i practiced adding try and except blocks
# to handle invalid user inputs in my name game program


try:

    name = input("Enter your name: ")

    # checks if the user entered nothing
    if name == "":
        raise ValueError("No text entered")

    # checks if the input is only one letter
    if len(name) == 1:
        raise ValueError("Name is too short")

    # checks if the user entered numbers only
    if name.isdigit():
        raise ValueError("Numbers are not allowed")

    print(f"Hello, {name}!")
    print(f"Your name has {len(name)} letters.")

except ValueError as e:
    print("ValueError:", e)

except TypeError:
    print("TypeError: invalid data type")

except Exception as e:
    print("Unknown error:", e)

else:
    print("Program ran successfully")

finally:
    print("Thanks for trying the name game!")


# notes:
# i noticed that some inputs like numbers do not automatically
# create an error because python still accepts them as strings
# i used if statements and raise ValueError to handle those cases


# exception notes:
# ValueError happens when the user enters blank text,
# a single character, or only numbers


# challenge question:
# raise SystemExit(0) stops the entire program completely
# it can be used instead of break when ending the full program
# instead of just stopping a loop
# unexpected results may happen if the program exits too early
