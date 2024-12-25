hotels_in_Krakow = [
   {"name":"Sky","price":320.00},
   {"name":"Metropol","price":480.00},
   {"name":"New Port","price":420.00},
   {"name":"Aparthotel","price":390.00}
]

hotels_in_Sopot = [
   {"name":"Focus","price":510.00},
   {"name":"Aqua","price":345.00},
   {"name":"La Boutique","price":390.00},
   {"name":"Marina","price":410.00}
]

def hotel_list(hotels):
    list_hotels = []
    for dictionaries in hotels:
        for key, values in dictionaries.items():
            if values == str(values):
                list_hotels.append(values)
    return list_hotels

def avg_price(hotels):
    price = 0
    count = 0
    for dictionaries in hotels:
        for key, values in dictionaries.items():
            if values != str(values):
                price += values
                count += 1
    avg_p = price / count
    return int(avg_p)

    


print("Hotels in Krakow:", ", ".join(hotel_list(hotels_in_Krakow)))
print("Average hotel price in Krakow:", avg_price(hotels_in_Krakow))
print("Hotels in Sopot:", ", ".join(hotel_list(hotels_in_Sopot)))
print("Average hotel price in Sopot:", avg_price(hotels_in_Sopot))
if hotel_list(hotels_in_Krakow) > hotel_list(hotels_in_Sopot):
    print("Cheaper hotels in: Krakow")
else:
    print("Cheaper hotels in: Sopot")