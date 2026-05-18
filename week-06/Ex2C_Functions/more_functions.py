# Exercise 2.C Creating and Calling Functions
# Lab 2 - More Functions

# display_mailing_label function


def display_mailing_label(name, address, city, state, zip_code):
    print(name)
    print(address)
    print(f"{city}, {state} {zip_code}")
    print()

# i created a function to display mailing labels

display_mailing_label(
    "Eyerusalem Debero",
    "123 Main Street",
    "Dallas",
    "TX",
    "75201"
)

# i tested the function with my information

display_mailing_label(
    "Selam Halu",
    "456 Oak Avenue",
    "Houston",
    "TX",
    "77001"
)

# i tested the function with another person


# add_numbers function


def add_numbers(*numbers):
    total = sum(numbers)

    equation = " + ".join(str(num) for num in numbers)

    print(f"{equation} = {total}")

# i created a function that adds numbers together

add_numbers(5)

# i tested the function with one number

add_numbers(5, 10)

# i tested the function with two numbers

add_numbers(1, 2, 3, 4, 5)

# i tested the function with multiple numbers

# display_receipt function


def display_receipt(total_due, amount_paid):

    print(f"Total Due: ${total_due}")
    print(f"Amount Paid: ${amount_paid}")

    if amount_paid > total_due:
        change = amount_paid - total_due
        print(f"Change Due: ${change}")

    elif amount_paid == total_due:
        print("Change Due: $0")

    else:
        balance = total_due - amount_paid
        print(f"Remaining Balance: ${balance}")

    print()

# i created a function that calculates receipt payments

display_receipt(50, 60)

# i tested the function with overpayment

display_receipt(50, 50)

# i tested the function with exact payment

display_receipt(50, 30)

# i tested the function with underpayment