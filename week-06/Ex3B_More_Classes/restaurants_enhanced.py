# Exercise 3.B More fun with classes

class Restaurant:
    """A class that represents a restaurant with serving tracking and ratings."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type
        self.number_served = 0
        self.customer_ratings = []

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

    def add_num_served(self, amount):
        self.number_served += amount

    def print_num_served(self):
        print(f"{self.rest_name} has served {self.number_served} customers")

    def customer_rating(self, rating):
        try:
            rating = int(rating)

            if rating < 1 or rating > 5:
                print("Please enter a rating from 1 to 5.")
                return

            self.customer_ratings.append(rating)
            avg = sum(self.customer_ratings) / len(self.customer_ratings)

            print(f"Your rating was {rating}. The average rating for this restaurant is {avg:.2f}")

        except ValueError:
            print("Invalid input. Please enter a whole number between 1 and 5.")

rest1 = Restaurant("In-N-Out", "fast food")
rest2 = Restaurant("Olive Garden", "Italian food")
rest3 = Restaurant("Banna Restaurant", "Eritrean and Ethiopian food")

# check initial served value
rest1.print_num_served()

# add customers served
rest1.add_num_served(50)
rest1.add_num_served(20)
rest1.print_num_served()

# ratings test
rest1.customer_rating(5)
rest1.customer_rating(4)
rest1.customer_rating("bad")   # test error handling
rest1.customer_rating(6)       # invalid range