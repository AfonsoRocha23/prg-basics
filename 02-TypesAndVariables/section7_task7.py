###
# A program that checks whether the vehicle speed entered
# from the keyboard is correct.
# The speed must be between 40 and 140 km/h.
#
speed = int(input('Enter vehicle speed: '))
speed_valid = 40 <= speed <= 140
print(f'Speed is valid: {speed_valid}')
