"""Handling the zerodivision error exception"""
# print(5/0)

"""Using Try-Except Blocks"""

# try:
#     print(5/0)
# except ZeroDivisionError :
#     print("You can't divide by zero ")


"""Using Exxceptions to prevent Crashes"""
# print("Give me two numbers, and I will divide them.")
# print("Enter 'q' to quit.")

# while True :
#     first_number=int(input("First number :"))
#     if first_number=="q":
#         break

#     second_number =int(input("Second number :"))
#     if second_number=="q":
#         break

#     try:
#         answer=first_number/second_number 
    
#     except ZeroDivisionError:
#         print("You can't divide by 0!")
    
#     else :
#         print(answer)


"""Handling the FileNotFoundError Exception"""
# from pathlib import Path 

# path =Path("alice.txt") 
# try:
#     content=path.read_text(encoding="utf-8") # Encoding argument is needed when your system's default encoding doesn;t match the encoding of the file that's being read.
# except FileNotFoundError:
#     print(f"Sorry, the file {path} does not exist.")


""" Analyzing Text """
# from pathlib import Path 

# path =Path("programming.txt") 
# try:
#     content=path.read_text(encoding="utf-8") 
# except FileNotFoundError:
#     print(f"Sorry, the file {path} does not exist.")
# else:
#     # count the approximate number of words in the file:
#     words=content.split()
#     num_word=len(words)
#     print(f"The file {path} has about {num_word} words.")


""" Working with Multiple Files """
# from pathlib import Path 
# def count_words(path):
#     """count the approximation number of words in a file """
#     try :
#         contents =path.read_text(encoding="utf-8")
#     except FileNotFoundError :
#         pass         
#         print(f"Sorry, The file {path} does not exits. ")
    
#     else:
#         words=contents.split()
#         num_word=len(words)
#         print(f"The file {path} has about {num_word} words.")

# path=Path("programming.txt")
# count_words(path)

# filenames=["I","Love"]

# for filename in filenames:
#     path=Path(filename)
#     count_words(path)


"""Pass Statement : It is a statement tell python to do nothing in a block."""

""" STORING DATA """    
""" Using json.dumps() and json.loads() """
# The first program will use json.dumps() to store the set of numbers, and the second program will use json.loads().

# from pathlib import Path 
# import json

# # number =[2,3,4,5,6,7]
# # path=Path('numbers.json')
# # contents=json.dumps(number)
# # path.write_text(contents)

# path=Path("numbers.json")
# content=path.read_text()
# numbers=json.loads(content)
# print(numbers)


"""Saving and Reading user generated data """
# from pathlib import Path
# import json 
# username=input("What is your name ?")
# path=Path("usrname.json")
# contents=json.dumps(username)
# path.write_text(contents)

# print(f"We will remember you when you come back,  {username} ! ")

# # Now greet the person who already in the program.
# path=Path("usrname.json")
# content=path.read_text()
# load=json.loads(content)

# print(f"Welcome back, {load}")


# from pathlib import Path
# import json
# path = Path('usrname.json')
# if path.exists():
#  contents = path.read_text()
#  usrname = json.loads(contents)
#  print(f"Welcome back, {usrname}!")
# else:
#  usrname = input("What is your name? ")
#  contents = json.dumps(usrname)
#  path.write_text(contents)
#  print(f"We'll remember you when you come back, {usrname}!")


"""REFACTORING : Refactoring makes
your code cleaner, easier to understand, and easier to extend """

from pathlib import Path 
import json

def get_stored_username (path):
    """Get stored username if available """
    if path.exists():
        contents=path.read_text()
        usrname=json.loads(contents)
        return usrname
    
    else:
        return None
    

def get_new_username(path):
    """Prompt for a new username."""
    usrname=input("What is your name ?")
    contents=json.dumps(usrname)
    path.write_text(contents)
    return usrname

def greet_user():
    """Greet the user by name."""
    path=Path("usrname.json")
    usrname=get_stored_username(path)
    if usrname :
        print(f"Welcome back , {usrname}")
    
    else:
        # usrname=input("What is your name ?")
        # contents=json.dumps(usrname)
        # path.write_text()
        usrname=get_new_username(path)
        print(f"We will remember you when you come back, {usrname}! ")

greet_user()
