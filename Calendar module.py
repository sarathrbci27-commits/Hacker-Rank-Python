import calendar

# Read the input
month, day, year = map(int, input().split())

# Get the day of the week
day_of_week = calendar.weekday(year, month, day)

# Convert the day of the week to the corresponding name
day_name = calendar.day_name[day_of_week].upper()

# Print the day name
print(day_name)
