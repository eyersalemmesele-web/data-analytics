# food_truck_bonus

class Restaurant:
    """Basic restaurant class used as the parent class."""

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
                print("Please enter a rating between 1 and 5.")
                return

            self.customer_ratings.append(rating)
            avg = sum(self.customer_ratings) / len(self.customer_ratings)

            print(f"Your rating was {rating}. Average rating: {avg:.2f}")

        except:
            print("Invalid input. Please enter a number from 1 to 5.")


# FOOD TRUCK (CHILD CLASS) 

class FoodTruck(Restaurant):
    """Child class that adds food truck-specific features."""

    def __init__(self, rest_name, food_type):
        super().__init__(rest_name, food_type)

        self.private_bookings = "N"
        self.truck_location = ""
        self.location_history = []

    def accepts_private_bookings(self):
        answer = input("Does this food truck accept private bookings? (Y/N): ").upper()

        self.private_bookings = answer

        if answer == "Y":
            print("This food truck accepts private bookings.")
        else:
            print("This food truck does not accept private bookings.")

    def relocate_truck(self):
        location = input("Enter current truck location (address, city): ")

        self.truck_location = location
        self.location_history.append(location)

        print(f"Truck is currently located at {location}")

    # NOTES 
    # I learned how inheritance works (FoodTruck inherits Restaurant)
    # I learned how super() connects parent and child classes
    # I used lists to store location history
    # I practiced using input() inside class methods
        
truck1 = FoodTruck("In-N-Out Truck", "Fast Food")

truck1.describe_rest()
truck1.rest_open()

truck1.print_num_served()
truck1.add_num_served(50)
truck1.print_num_served()

truck1.customer_rating(5)
truck1.customer_rating(4)

truck1.accepts_private_bookings()
truck1.relocate_truck()

print("Location history:", truck1.location_history)