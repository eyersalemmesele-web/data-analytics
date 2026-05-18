# Exercise 2.B Using library functions
# Lab 3. Math and statistics

import random
import math
import statistics

# Starting variables
vals_1_100 = range(1, 100)
vals_sample = random.sample(vals_1_100, 75)
vals_choices = random.choices(vals_1_100, k=200)

radius = random.randint(3, 10)
pi = math.pi

# 75 sample values (subset)

print("_Experimenting with a subset of integers 1-100:")

print("Sum of 75 sample values:", sum(vals_sample))
# i used sum to add all the values in the sample

print("Average of 75 sample values:", statistics.mean(vals_sample))
# i used mean to find the average of the sample values

print("Median of 75 sample values:", statistics.median(vals_sample))
# i used median to find the middle value of the sample

print("\n")

# 200 values (superset)

print("_Experimenting with a superset of 200 values, integers 1-100:")

print("Average of 200 values:", statistics.mean(vals_choices))
# i used mean to calculate average of 200 values

print("Median of 200 values:", statistics.median(vals_choices))
# i used median to find middle value of 200 values

print("Mode of 200 values:", statistics.mode(vals_choices))
# i used mode to find most common value

print("Standard deviation of 200 values:", statistics.stdev(vals_choices))
# i used stdev to measure spread of values

print("Variance of 200 values:", statistics.variance(vals_choices))
# i used variance to measure how data is spread

print("\n")

# Circle calculations

print("_Modeling a random circle:")

area = pi * (radius ** 2)
# i used pi times radius squared to calculate circle area

print("Radius =", radius, ", area =", round(area))
# i rounded the area to nearest whole number

print("Radius =", radius, ", area =", int(area))
# i converted area to integer to remove decimals