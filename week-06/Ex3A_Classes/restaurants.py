# Exercise 3.A Working with classes

class Restaurant:
    """A class that represents a restaurant and its basic information."""

    def __init__(self, rest_name, food_type):
        self.rest_name = rest_name
        self.food_type = food_type

    def describe_rest(self):
        print(f"{self.rest_name} serves {self.food_type}.")

    def rest_open(self):
        print(f"{self.rest_name} is open.")

# create 3 restaurants (including your favorite)
rest1 = Restaurant("In-N-Out", "fast food")
rest2 = Restaurant("Olive Garden", "Italian food")
rest3 = Restaurant("Banna Restaurant", "Eritrean and Ethiopian food")

# test methods
rest1.describe_rest()
rest1.rest_open()

rest2.describe_rest()
rest2.rest_open()

rest3.describe_rest()
rest3.rest_open()