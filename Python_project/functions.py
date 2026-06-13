
# def great_user(username): # Here the username works as a parameter.
#    """Display a simple greeting to the user """ # It is called as a docstring.
#    print(f"Hello,{username.title()}")


# great_user("Palak") # Here the argument is "Palak".


# """Positional argument """

# def describe_pet(animal_type, pet_name):
#    print(f"\nI have a {animal_type}.")
#    print(f"My {animal_type}'s name is {pet_name.title()}")

# describe_pet("hamster","harry")
# describe_pet("Dog","Tommy")

# """Keywords Arguments"""

# def describe_pet(animal_type, pet_name):
   
#    print(f"\nI have a {animal_type}.")
#    print(f"My {animal_type}'s name is {pet_name.title()}.")

# describe_pet(animal_type="hamaster", pet_name="harry")


"""Default Values"""
# def describer_pet(pet_name, animal_type="dog"):
#     print(f"\nI have a {animal_type}.")
#     print(f"My {animal_type}'s name is {pet_name.title()}.")

# describer_pet(pet_name="Tommy")
# describer_pet("Tommy")

"""Return values"""

# def get_formatted_name(first_name, last_name):
#     full_name=f"{first_name} {last_name}"
#     return full_name.title()

# musician= get_formatted_name("Palak","Yadav")
# print(musician)

"""Making an argument optional"""
# def get_formatted_name(first_name, middle_name, last_name):
#     full_name= f"{first_name} {middle_name} {last_name}"
#     return full_name.title()

# musician=get_formatted_name("AMAN", "DEEP","SAINI")
# print(musician)


# def get_formatted_name(first_name,last_name, middle_name=""):
#     if middle_name:
#         full_name= f"{first_name} {middle_name} {last_name}"
#     else:
#          full_name= f"{first_name} {last_name}"
#     return full_name.title()

# musician=get_formatted_name("AMAN", "DEEP")
# print(musician)

# musician=get_formatted_name("AMAN", "DEEP","SAINI")
# print(musician)

# def build_person(first_name, last_name):
#     person={"first": first_name,
#             "last" : last_name
#             }
#     return person

# musician=build_person("aman","saini")
# print(musician)

# def build_person(first_name, last_name,age=None):
#     person={"first": first_name,
#             "last" : last_name
#             }
#     if age:
#         person["age"]=age
#     return person

# musician=build_person("aman","saini",age=25)
# print(musician)

"""Using a function with a while loop"""
# def get_formatted_name(first_name, last_name):
#     full_name=f"{first_name} {last_name}"
#     return full_name.title()

# while True:
#     print("\n Please tell me your name:")
#     f_name=input("First name :")
#     l_name=input("Last name :")

#     formatted_name=get_formatted_name(f_name, l_name)
#     print(f"\n Hello, {formatted_name}!")

"""Passing a list to a function"""
# def greet_users(names):
#     for name in names:
#         message=f"Hello, {name.title()}!"
#         print(message)

# usernames=["hannah","ty","margot"]
# greet_users(usernames)

#Start with some designs that need to be printed.
# unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
# completed_models = []
# # Simulate printing each design, until none are left.
# # Move each design to completed_models after printing.
# while unprinted_designs:
#  current_design = unprinted_designs.pop()
#  print(f"Printing model: {current_design}")
#  completed_models.append(current_design)
# # Display all completed models.
# print("\nThe following models have been printed:")
# for completed_model in completed_models:
#  print(completed_model)

# def print_models(unprinted_designs, completed_models):
#     while unprinted_designs:
#         current_design=unprinted_designs.pop()
#         print(f"Printing model : {current_design}")
#         completed_models.append(current_design)

#         print("\n The following models have been printed :")
#         for completed_model in completed_models:
#             print(completed_model)

# unprinted_designs=['phone case','robot pendant','dodecahedron']
# completed_models=[]
# print_models(unprinted_designs, completed_models)

"""Passing an arbitrary number of arguments"""

# def make_pizza(*toppings): # The asterisk in the parameter name *toppings allows the function to accept an arbitrary number of arguments.
#     print(toppings)

# make_pizza("Pepperoni")
# make_pizza("Mushrooms","Green peppers","Extra cheese")

# def make_pizza(*toppings):
#     print("\n Mqking a pizza wirh the following toppings :")
#     for topping in toppings:
#         print(f"-{topping}")

# make_pizza("Pepperoni")
# make_pizza("Mushrooms","Green peppers","Extra cheese")


# def build_profile(first, last, **user_info):
#     """Build a dictionary containing everything we know about a user."""
#     user_info["first_name"]=first
#     user_info["last_name"]=last
#     return user_info

# user_profile=build_profile("albert","einstein",Location="princeton",field="physics")
# print(user_profile)
   


"""Storing your functions in modules"""
# Imoporting an entire module