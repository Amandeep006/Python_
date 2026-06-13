# import matplotlib.pyplot as plt


"""Plotting  a single line graph """
# squares=[1,4,9,16,24]

# fig, ax=plt.subplots()
# ax.plot(squares)
# plt.show()

"""Changing the label type and line thickness."""
# squares=[1,4,9,16,24]

# fig, ax=plt.subplots() # subplots() function to create a figure and a set of subplots. The function returns a tuple containing the figure and the axes objects. In this case, we are only creating one subplot, so we can unpack the tuple into two variables: fig and ax.
# ax.set_title("Square Numbers", fontsize=24) # set_title() method to set the title of the graph and fontsize to set the size of the title.
# ax.set_xlabel("Values", fontsize=14)# set_xlabel() method to set the label for the x-axis and fontsize to set the size of the label.
# ax.set_ylabel("Square of Values", fontsize=14) # set_ylabel() method to set the label for the y-axis and fontsize to set the size of the label.

# ax.tick_params(labelsize=14) # Tick_params() method to set the size of the tick labels.
# ax.plot(squares)
# plt.show()


"""Correcting the plot."""
# input_values=[1,2,3,4,5]
# squares=[1,4,9,16,25]

# fig, ax=plt.subplots()
# ax.plot(input_values, squares, linewidth=3)
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Values", fontsize=14)
# ax.set_ylabel("Square of Values", fontsize=14)
# ax.tick_params(labelsize=14)
# plt.show()


"""Using built-in styles."""

# import matplotlib.pyplot as plt 
# plt.style.available 
# ['Solarize_Light2','_classic_test_patch', '_mpl-gallery']

# squares=[1,4,9,16,25]
# input_values=[1,2,3,4,5]
# plt.style.use('Solarize_Light2')
# fig, ax=plt.subplots()
# ax.plot(input_values, squares, linewidth=3)
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Values", fontsize=14)
# ax.set_ylabel("Square of Values", fontsize=14)
# ax.tick_params(labelsize=14)
# plt.show()



"""Plotting and Styling individual points with scatter() methods"""
# import matplotlib.pyplot as plt 
# plt.style.available 
# ['Solarize_Light2','_classic_test_patch', '_mpl-gallery','seaborn']

# plt.style.use('Solarize_Light2')
# fig, ax=plt.subplots()
# ax.scatter(2,4,s=200)

# #set chart title and lable axes.
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Values",fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)

# ax.tick_params(labelsize=14)
# plt.show()



"""Plotting a Series of Points with scatter() method."""

# import matplotlib.pyplot as plt 

# x_values=[1,2,3,4,5]
# y_values=[1,4,9,16,25]

# plt.style.use('Solarize_Light2')
# fig, ax=plt.subplots()
# ax.scatter(x_values, y_values, s=100)
# ax.set_title("Square Numbers", fontsize=24)
# ax.set_xlabel("Values",fontsize=14)
# ax.set_ylabel("Square of Value", fontsize=14)

# ax.tick_params(labelsize=14)
# plt.show()


"""Calculating Data Automatically"""

import matplotlib.pyplot as plt
x_values=range(1,1000)
y_values=[x**2 for x in x_values]

plt.style.use("Solarize_Light2")
fig, ax=plt.subplots()

# we can use differemt colors in the chart.
# ax.scatter(x_values, y_values,color='red', s=10) 

# # we can also use RGB value between 0 to 1
# ax.scatter(x_values, y_values,color=(0,0.8,0), s=10) 

# Using a colormap
ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)


ax.axis([0,1100,0,1_100_000])
ax.ticklabel_format(style='plain')
 # The ticklabel_format() method allows you to override the default ticklabel style for any plot.
# plt.show() # It is used to show the chart.
plt.savefig("square_plot.png") # It is used to save the chart in the same directory where you save all the files.


"""A number raised to the third power is a cube. Plot the first five
cubic numbers, and then plot the first 5,000 cubic numbers."""

# import matplotlib.pyplot as plt 

# x_value=range(0,5000)
# y_values=[x*x*x for x in x_values]

# plt.style.use("Solarize_Light2")
# fig, ax=plt.subplots()
# ax.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, s=10)
# ax.axis([0,1100,0,1_100_000])
# ax.ticklabel_format(style='plain')
# plt.show()


