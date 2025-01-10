def avg_speed(distance,hours,minutes):
    actual_hours = hours + minutes/60
    return f"Average speed: {distance/actual_hours}"

distance = float(input("Enter distance in km: "))
hours = float(input("Enter number of travel hours: "))
minutes = float(input("Enter number of travel minutes: "))
print(avg_speed(distance,hours,minutes))