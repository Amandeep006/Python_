"""Reading from a File"""
# from pathlib import Path 
# path=Path("Python_course\pi_digits.txt")

# contents=path.read_text() # .read_text() is used to read the contents of the file.
# print(contents)
"""The only difference between this output and the original file is the
extra blank line at the end of the output. The blank line appears because
read_text() returns an empty string when it reaches the end of the file; this
empty string shows up as a blank line."""

# We can resmove this extra blank line with using rstrip()
# content=contents.rstrip()
# print(content)

# Using the splitlines() method to turn a long string into a set of lines.
# lines=contents.splitlines()
# for line in lines:
#     print(line)


"""Working with a File's Contents """

# from pathlib import Path 
# path=Path("Python_course\pi_digits.txt")

# contents=path.read_text()
# lines=contents.splitlines()
# pi_string=" "
# for line in lines:
#     pi_string+=line

# print(pi_string)
# print(len(pi_string))

"""IS your birthday contained in PI?"""
# birthday=input("Enter your birthday, in the form mmddyy:")
# if birthday in pi_string :
#     print("Your birthday appears in the first millions digits of pi!")
# else:
#     print("Your birthday does not appears in the first millions digits of pi .")


""" WRITING TO A FILE"""


"""Writing a single line : It is write a last single line in the file."""
from pathlib import Path
# path=Path("Python_course\write.text")
# path.write_text("I love to work on myself.") # write_text() method is used to write a contnet in a file.
# value=str([14,26,86,59])
# path.write_text((value))

"""Writing Multiple Lines"""
contents="I love programming.\n"
contents+="I love creating new games.\n"
contents+="I also love working with data. \n"

path=Path("programming.txt")
path.write_text(contents)