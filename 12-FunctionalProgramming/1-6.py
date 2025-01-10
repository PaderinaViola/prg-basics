ms_to_kmh = lambda  dist, h, m: dist/(h+m/60)

distance = float(input("Enter distance in km: "))
hours = float(input("Enter number of travel hours: "))
minutes = float(input("Enter number of travel minutes: "))
print(ms_to_kmh(distance,hours,minutes))