# global list (must be outside the class so it keeps all customers)
cust_list = []

class RewardsProgram:
    """A class that stores customer information for a rewards program."""

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email

    def profile(self):
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}")

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!")

    def add_to_cust_list(self):
        cust_list.append((self.cust_name, self.phone, self.email))
    
cust1 = RewardsProgram("Eyerusalem", "123-456-7890", "eyerusalem@email.com")
cust2 = RewardsProgram("Daniel", "111-222-3333", "daniel@email.com")
cust3 = RewardsProgram("Sara", "999-888-7777", "sara@email.com")

cust1.profile()
cust1.thank_you()
cust1.add_to_cust_list()

cust2.profile()
cust2.thank_you()
cust2.add_to_cust_list()

cust3.profile()
cust3.thank_you()
cust3.add_to_cust_list()

print("\nCustomer List:")
print(cust_list)