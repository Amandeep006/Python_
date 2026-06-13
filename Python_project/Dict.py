# alien_0 ={
#     'color': 'green',
#     'points': 5
# }

# print(alien_0['color'])
# print(alien_0['points'])

# new_points =alien_0['points']
# print(f" You just earned {new_points} points !")

# print(alien_0)
# alien_0['x_position'] = 0
# alien_0['y_position'] = 25
# print(alien_0)


# we define a dictionary to empty and then add key value pairs to it.
# alien_0={}

# alien_0['color']='green'
# alien_0['points']=5

# print(alien_0)

# alien_0['color']='Yellow' # we can change the value of a key in a dictionary by reassigning it.
# print(f" The alien is now {alien_0['color']}")

# let's track the pistion of an alien that moves at differnet speeds.

# alien_0={'x_position':0, 'y_position':25, 'speed':'medium'}
# print(f"original postion of alien : {alien_0['x_position']}")

# # move the alien to the right.
# # Detemine how far to move the alien based on its current speed.
# if alien_0['speed']=='slow':
#     x_increment=1
# elif alien_0['speed']=='medium':
#     x_increment=2
# else:
#     # this must be a dast alien 
#     x_increment=3

# alien_0['x_position']= alien_0['x_position']+x_increment

# print(f"New Position of alien : {alien_0['x_position']}") 


# fav_lang={
#     'jen':'python',
#     'sarah':'c',
#     'edward':'ruby',
#     'phil':'python'
# }

# language=fav_lang['sarah'].title()
# print(f"Sarah's favorite language is {language}.")

# Get() method is used to access the value of a key which is not present in the dictionary.
 
# alien_0={'color':'green','speed':'slow'}
# point_value=alien_0.get('points', 'No point value assigned.')
# print(point_value)

# Looping through all key-value pairs.
# user_0={
#     'username':'efermi',
#     'first':'enrico',
#     'last':'fermi'
# }

# for key, value in user_0.items():
#     print(f"\nKey: {key}")
#     print(f"Value: {value}")

# fav_lang={
#     'jen':'python',
#     'sarah':'c',
#     'edward':'ruby',
#     'phil':'python'
# }

# for name, language in fav_lang.items():
#     print(f"{name.title()}'s favorite language is {language.title()}.")

# for name in fav_lang.keys(): # Keys() method is used to access the keys of a dictionary.
#     print(name.title())

# for name in fav_lang():
#     print(name.title())

# friends=['phil','sarah']
# for name in fav_lang.keys():
#     print(f" Hii {name.title()}.")

#     if name in friends:
#         language=fav_lang[name].title()
#         print(f"\t{name.title()}, I see you love {language} !")

# Sorted() function is used to sort the keys of a dictionary in alphabetical order.

# for name in sorted(fav_lang.keys()):
#     print(f"{name.title()}, thank you for taking the poll.")

# Values() method is used to access the values of a dictionary.
# print("The following language hav ebeen mentioned :")
# for language in fav_lang.values():
#     print(language.title())

# Set is a collection in which each item must be unique. It is used to store unique items.

# for lang in set(fav_lang.values()):
#     print(lang.title())

# Make an empty list for storing aliens.
# aliens=[]

# for alien_number in range(30):
#     new_alien={
#         'color':'green',
#         'points':5,
#         'speed':'slow'
#     }
#     aliens.append(new_alien)
# # Show the first 5 aliens.

# for alien in aliens[:5]:
#     print(alien)

# print(f"TOtal number of aliens : {len(aliens)}")

# Store information abiut a pizza being ordered.
pizza={'crust':'thick',
       'toppings':['mushrooms','extra cheese']
       }
print(f" You ordered a {pizza['crust']}-crust pizza with the following toppings:")

for topping in pizza['toppings']:
    print(f"{topping}")
