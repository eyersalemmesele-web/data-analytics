# sampling_tools

import random

products = [
    'Laptop', 'Monitor', 'Keyboard', 'Mouse', 'Webcam',
    'Headset', 'Docking Station', 'USB Hub', 'Desk Lamp',
    'Surge Protector'
]

# Product of the Day
print("Product of the Day:", random.choice(products))
# i used random.choice to select one random product from the list

# Survey (3 random products)
print("Survey Products:", random.sample(products, 3))
# i used random.sample to select 3 different products without repeating

# Shuffle all products
random.shuffle(products)
print("Shuffled Products:", products)
# i used shuffle to rearrange the list in random order

# Random transaction count
print("Daily Transactions:", random.randint(50, 300))
# i used randint to generate a random number between 50 and 300