# Exercise 2.D Lambdas and Generators
# Lab 1 - Quick Multiplier


# doubler lambda


doubler = lambda n: n * 2

print(doubler(8))
print(doubler(-4))
print(doubler("banana"))

# i created a lambda function that doubles the argument

# tripler lambda


tripler = lambda n: n * 3

print(tripler(8))
print(tripler(-4))
print(tripler("banana"))

# i created a lambda function that triples the argument


# multiplier function


def multiplier(x):
    return lambda n: n * x

# i created a function that returns lambda multipliers


times4 = multiplier(4)
times5 = multiplier(5)
times6 = multiplier(6)
times7 = multiplier(7)
times8 = multiplier(8)
times9 = multiplier(9)
times10 = multiplier(10)

# i created multiplier variables from 4 through 10


print(times4(2))
print(times5(2))
print(times6(2))
print(times7(2))
print(times8(2))
print(times9(2))
print(times10(2))

# i tested all multiplier variables using the value 2