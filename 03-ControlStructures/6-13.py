car_speed = int(input("Enter car speed: "))
speed_limit_min = 40
speed_limit_max = 140
if car_speed >= speed_limit_min and car_speed <= speed_limit_max:
    print(f"Entered car speed: {car_speed}")
    print(f"Your speed is ok")
else:
    print(f"Entered car speed: {car_speed}")
    print(f"Warning: invalid car speed!!")