import matplotlib.pyplot as plt 
from randomwalk import randwalk
# make a random walk 
# rw=randwalk()
# rw.fill_walk()

# #Plot the points in the walk.
# plt.style.use('classic')
# fig, ax=plt.subplots()
# ax.scatter(rw.x_values, rw.y_values, s=15)
# ax.set_aspect("equal")
# plt.show()

"""Generating multiple random walks."""
# Kepp making new walks, as long as the program is active.
# while True:
#     rw=randwalk()
#     rw.fill_walk()

#      #Plot the points in the walk.
#     plt.style.use('classic')
#     fig, ax=plt.subplots()
#     ax.scatter(rw.x_values, rw.y_values, s=15)
#     ax.set_aspect("equal")
#     plt.show()

#     keep_running=input("Make another walk ?(Y/N):")
#     if keep_running=="N":
#         break

"""Coloring the points in as walks."""

while True:
    rw=randwalk(50000)
    rw.fill_walk()

     #Plot the points in the walk.

    plt.style.use('classic')
    # fig, ax=plt.subplots(figsize=(15,9))
    fig, ax=plt.subplots(figsize=(10,6), dpi=128)


    point_numbers=range(rw.num_points)
    ax.scatter(rw.x_values, rw.y_values, c=point_numbers, cmap=plt.cm.Blues,edgecolors="none", s=1)
    ax.set_aspect("equal")

    # Plotting the starting and ending points.
    ax.scatter(0,0,c="green",edgecolors="none", s=100)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c="red", edgecolors="none", s=100)

    # Remove the axes.
    ax.get_xaxis().set_visible(False)
    ax.get_yaxis().set_visible(False)

    plt.show()
    keep_running=input("Make another walk ?(Y/N):")
    if keep_running=="N":
        break