# Input function used to take an input from the user and store it in a variable.
# message=input("Tell me something, and I will repeat it back to you :")
# print(message)

# name=input("Please enter you name :")
# print(f"Hello dear {name}!")

# prompt="If you share your name, we can personalize the message you see."
# prompt+="\nWhar is you first name ?"

# name =input(prompt)
# print(f"\nHello,{name}!")

# age=int(input("How old are you ?"))
# print(age)

# height=int(input("How tall are you, in inches?"))
# if height>=48:
#     print("\n Your are tall enough to ride") 
# else:
#     print("\n You will be ablr to ride when you are a little older.")

# Modulo operator is used to find the remainder of a division operation. It is represented by the % symbol.
# number =int(input("ENter a number and I will tell you if iit is even or odd :"))
# if number%2==0:
#     print(f"\n THe number {number} is even.")
# else:
#     print(f"\n The number {number} is odd.")

# While loop is used to execute a block of code repeatedly unitl the given condition is true.

# i=1
# while i<=5:
#     print(i)
#     i+=1

# prompt="\n tell me something and I will repeat it back to you:"
# prompt+="\n ENter 'quit' to end the program."

# message=""
# while message !='quit' :
#     message=input(prompt)
#     print(message)
    

# prompt="\n Do you like me ?"
# prompt+="\n Enter Yes or not to answer."

# answer=""
# while answer !="Yes":
#     answer=input(prompt)
#     print("Please answer Yes to continue.")

# """Flag is a variable that is used to control the flow of a program. It is used to indicate whether a certain condition has been met or not. It is often used in while loops to control the loop's execution."""

# prompt="\n tell me something and I will repeat it back to you:"
# prompt+="\n ENter 'quit' to end the program."

# active=True
# while active:
#     message=input(prompt)

#     if message=='quit':
#         active=False
#     else:
#         print(message)
     

""" The Break statement is used to exit the statement in which it is used."""
# prompt="\n Please enter the name of a city you ave visited :"
# prompt+="\n (Enter 'quite' when you are finished.)"

# while True:
#     city=input(prompt)

#     if city=="quite":
#         break
#     else:
#         print(f"I would love to go to {city.title()}!")


"""The continue statement is used to skip the rest of the code inside a loop for the current iteration only."""

# i=0
# while i<10:
#     i+=1
#     if i%2==0:
#         continue

#     print(i)



# x=1
# while x<=5:
#     print(x)
#     # x+=1

# Start the users that need to be verified, and an empty list to hold confirmed users.
# unconfirmed_users=["alice","brian","candace"]
# confirmed_users=[]

# while unconfirmed_users:
#     current_user= unconfirmed_users.pop()

#     print(f"Verifyning user: {current_user.title()}")
#     confirmed_users.append(current_user)

# print("\n THe following users have been confirmed :")
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())


# pets=["dogs","cat","dog","goldfish","cat","rabbit","cat"]
# print(pets)

# while "cat" in pets:
#     pets.remove('cat')

# print(pets)


"""Fillling a dictionary with user input"""
responses={}
#set a flag to indicate that pollinng is active.
polling_active=True

while polling_active:
    name = input("\n What is your name ?")
    response= input("\n Which mountain would you like to climb someday ?")

    responses[name]=response

    repeat=input("Would you like to let another person respond ?(Yes or No)")
    if repeat=="No" or repeat=="no":
        polling_active=False

print("\n ---Poll Results--")
print(f"{name} would like to climb {response}.")