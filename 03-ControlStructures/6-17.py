many_hours = input("Enter time (24-hour format): ")
smaller_hours, minutes = many_hours.split(':')
smaller_hours = int(smaller_hours)
if smaller_hours <= 12:
    many_hours = smaller_hours
    print(f"Time in 12-hour format: {smaller_hours} am")
if smaller_hours >=13 or smaller_hours <= 24:
    smaller_hours -= 12
    print(f"Time in 12-hour format: {smaller_hours}:{minutes} pm")