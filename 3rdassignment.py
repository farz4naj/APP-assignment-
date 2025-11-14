# Assignment 3
# Name: Farzana Jafary
# Description:
# This program asks the user for their name and favorite number,
# then converts a given number of seconds into hours, minutes, and seconds

user_name = input("Enter your name: ")


favorite_number = int(input("Enter your favorite number: "))
print(f'\nThis is "{user_name}" and their favorite number is "{favorite_number}".\n')
total_seconds = int(input("Enter the number of seconds: "))
seconds_in_minute = 60
minutes_in_hour = 60
seconds_in_hour = seconds_in_minute * minutes_in_hour

hours = total_seconds // seconds_in_hour
remaining_seconds = total_seconds % seconds_in_hour

minutes = remaining_seconds // seconds_in_minute
seconds = remaining_seconds % seconds_in_minute

print(f"{total_seconds} seconds = {hours} hours, {minutes} minutes, {seconds} seconds")
