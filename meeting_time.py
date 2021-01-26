#!/usr/local/bin/python3
# Made by @swisscoding on Instagram
# Follow now and share!

from colored import stylize, fg

# decoration
print(stylize("\n---- | Time when two rolling objects meet | ----\n", fg("red")))

# user interaction
v_obj_a = float(input("Constant velocity of object a (in km/hour): "))
v_obj_b = float(input("Constant velocity of object b (in km/hour): "))
distance = float(input("Distance between each other (in km): "))

# function
def meeting_time(va, vb, distance_in_km):
    return distance / (va + vb) * 60

time = stylize(meeting_time(v_obj_a, v_obj_b, distance), fg("red"))
print(f"\nThe two objects will meet in {time} minute/s.\n")
