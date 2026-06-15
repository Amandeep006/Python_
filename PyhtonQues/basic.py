"""Write a Python program that does the following:
1.  Takes two numbers as input from the user.
2.  Performs the basic mathematical operations on these two numbers:
"""

num1=int(input("Enter your first number :"))
num2=int(input("Enter your second number :"))
# Addition 
sum=num1+num2
print(f"The addition of {num1} & {num2} : {sum}")

# Subtraction 
sub=num1-num2
print(f"The subtraction of {num1} & {num2} : {sub}")

# Multipication
mult=num1*num2
print(f"The Multipilcation of {num1} & {num2} : {mult}")

# Division 
div=num1//num2
print(f"The divison of {num1} & {num2} : {div}")



"""Write a Python program that:
1.  Takes a user's first name and last name as input.
2.  Concatenates the first name and last name into a full name.
3.  Prints a personalized greeting message using the full name.
"""

first_name=input("Enter your first name :")
last_name=input("Enter your last name :")

full_name=f"{first_name} {last_name}"

print(f"Hello {full_name}!, Welcome to the python world. Hope your journey is going pleasant and enjoyable.")



n=int(input("Enter a number from 1 to 50 :"))

if n%2!=0:
    print("weird")

elif (n%2==0 and n>2 and n<5 ):
    print("Not weird")

elif (n%2==0 and n>6 and n<20):
    print("Weird")

else :
    print("Not weird ")


"""
Write a Python program that:
1. 	Takes an integer input from the user.
2. 	Checks whether the number is even or odd using an if-else statement.
3. 	Displays the result accordingly.

"""

num= "\nAnytime you want to quit just enter 'q'. "
num+="\nEnter any number: "

while True:
    if num=='q':
        break

    else:
        n1=int(input(num))
        if n1%2==0:
            print(f"The number {n1} is even.")
        else:
            print(f"The number {n1} is odd.")


                   
"""
 Write a Python program that:
1.   Uses a for loop to iterate over numbers from 1 to 50.
2.   Calculates the sum of all integers in this range.
3.   Displays the final sum.

"""
sum=0
for i in range(1,51):
    sum+=i

print(f"THe sum of all numbers between 1 to 50: {sum}" )
    


"""
 Write a Python program that:
1.   Defines a function named factorial that takes a number as an argument and calculates its factorial using a loop or recursion.
2.   Returns the calculated factorial.
3.   Calls the function with a sample number and prints the output.

"""

def factorial(n):
    fact=1
    while(n>0):
        fact=n*fact
        n=n-1

    return fact

num=int(input("Enter any number :"))
print(f"The factorial of {num} is {factorial(num)}")


"""
Write a Python program that:
1.   Asks the user for a number as input.
2.   Uses the math module to calculate the:
o   Square root of the number
o   Natural logarithm (log base e) of the number
o   Sine of the number (in radians)
3.   Displays the calculated results.

"""
import math
num=int(input("Enter you any number :"))
sqr=math.sqrt(num)
lgn=math.log(num)
rad=math.radians(num)
snum=math.sin(rad)

print(f"The Square root of {num} is {sqr}")
print(f"The logarithm of {num} is {lgn}")
print(f"The Sine of {num} is {snum}")