The distance to the horizon depends on the height of the observer above the ground. The higher you are, the farther away the horizon is. For most situations, you can use the following formula:

    d = 3.57 × √h

    Where:

    * d is the distance to the horizon in kilometers
    * h is the height of the observer in meters

    Write a program that calculates the distance to the horizon from a height given in meters from the keyboard. Then, using the program, calculate the distance to the horizon in km when:

    1. You are standing on a beach, by the sea, on the water line (calculate the distance for your height in m). You have probably been to the seaside many times. Can you believe that the horizon is only a few kilometers away?
    1. You are looking out of a hotel window located by the sea, the window is at a height of 20 meters.

# 1. Calculation for standing on a beach (assuming an eye-level height of ~1.7 meters)
    h_beach = 1.7
distance_beach = 3.57 * math.sqrt(h_beach)
print(f"1. Standing on the beach (height {h_beach} m): distance to horizon = {distance_beach:.2f} km")

# 2. Calculation for the hotel window at a height of 20 meters
h_hotel = 20
distance_hotel = 3.57 * math.sqrt(h_hotel)
print(f"2. Hotel window (height {h_hotel} m): distance to horizon = {distance_hotel:.2f} km")
