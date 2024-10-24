ean = input("Enter EAN-13 article number: ")
if len(ean) == 13 and ean.isdigit():
    print(f"Article number is correct")
    if ean.startswith('590'):
        print(f"Article manufactured in Poland")
else:
    print(f"Article is wrong")