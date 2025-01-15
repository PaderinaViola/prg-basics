dict = {"Krakow":7,"Warszawa":-2,"Sopot":4,"Koszalin":-1,"Opole":3}
positive = list(filter(lambda value: dict[value]>0, dict))
print(f"Cities with positive temperatures: {positive}")