class RewardsProgram:
    """Tracks customer visits and rewards points."""

    def __init__(self, cust_name, phone, email):
        self.cust_name = cust_name
        self.phone = phone
        self.email = email
        self.restaurants_visited = []
        self.rewards_points = 0

    def profile(self):
        print("\nCustomer Profile")
        print(f"Name: {self.cust_name}")
        print(f"Phone: {self.phone}")
        print(f"Email: {self.email}\n")

    def thank_you(self):
        print(f"Thank you, {self.cust_name}, for visiting our restaurant!\n")

    def calculate_rewards(self, bill_amount):
        return int(float(bill_amount))

    def visit_rest(self):
        print("\nNew Visit")

        restaurant = input("Restaurant name: ").strip()

        if restaurant not in self.restaurants_visited:
            self.restaurants_visited.append(restaurant)

        bill = input("Total bill ($): ").strip()

        try:
            points = self.calculate_rewards(bill)
        except:
            print("Invalid input. Please enter a number.")
            return

        self.rewards_points += points

        print("\nVisit Summary")
        print(f"Restaurant: {restaurant}")
        print(f"Points earned: {points}")
        print(f"Total points: {self.rewards_points}\n")

        # NOTES:
        # I learned how to use classes to store customer data
        # I learned how methods update values step by step
        # I used lists to track restaurants visited
        # I used input() to make the program interactive

        # create a customer (object)
cust1 = RewardsProgram("Eyerusalem", "123-456-7890", "eyerusalem@gmail.com")

# show profile
cust1.profile()

# run visits (this will ask you for input)
cust1.visit_rest()
cust1.visit_rest()

# final summary
print("Restaurants visited:", cust1.restaurants_visited)
print("Total rewards points:", cust1.rewards_points)