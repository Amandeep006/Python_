"""Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
"""

# num1=int(input("Enter your first number :"))
# num2=int(input("Enter your second number :"))
# # Addition 
# sum=num1+num2
# print(f"The addition of {num1} & {num2} : {sum}")

# # Subtraction 
# sub=num1-num2
# print(f"The subtraction of {num1} & {num2} : {sub}")

# # Multipication
# mult=num1*num2
# print(f"The Multipilcation of {num1} & {num2} : {mult}")

# # Division 
# div=num1//num2
# print(f"The divison of {num1} & {num2} : {div}")



"""Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
"""

# first_name=input("Enter your first name :")
# last_name=input("Enter your last name :")

# full_name=f"{first_name} {last_name}"

# print(f"Hello {full_name}!, Welcome to the python world. Hope your journey is going pleasant and enjoyable.")



n=int(input("Enter a number from 1 to 50 :"))

if n%2!=0:
    print("weird")

elif (n%2==0 and n>2 and n<5 ):
    print("Not weird")

elif (n%2==0 and n>6 and n<20):
    print("Weird")

else :
    print("Not weird ")