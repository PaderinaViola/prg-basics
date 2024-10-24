good_pin = '0805'
for attempt in range(3):
    pin = input("Enter pin: ")
    if pin == good_pin:
        print(f"Access granted")
        break
    elif pin != good_pin:
        print(f"Incorrect...")
if pin != good_pin:
    print(f"Sorry, your payment card has been blocked :)")
