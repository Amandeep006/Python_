
"""Importing an entire module"""
# import pizza

# pizza.make_pizza(16, "Pepperoni")
# pizza.make_pizza(12, "Mushrooms","Green peppers","Extra cheese")

"""Importing a function"""

# from pizza import make_pizza 
# make_pizza(16, "Pepperoni")

"""Importing a function with an alias"""
# from pizza import make_pizza as mp
# mp(10, "Mushrooms","Green peppers","Extra cheese")

"""Importing an entire module with an alias"""
# import pizza as p
# p.make_pizza(16, "Pepperoni")

"""Importing all functions in a module"""
from pizza import *
make_pizza(15, "Cheese")