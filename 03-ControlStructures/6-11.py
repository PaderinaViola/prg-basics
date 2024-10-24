current_price = 140
previous_price = 200
price_new = (current_price/previous_price) * 100
price_reduce = 100 - price_new
if price_reduce > 10:
    print(f"Previous price is {previous_price}")
    print(f"Current price is {current_price}")
    print(f"Buy the product!!")
    print(f"Product price reduced by {price_reduce}%")
else:
    print(f"dont bye it")
    print(f"Previous price is {previous_price}")
    print(f"Current price is {current_price}")
    print(f"Product price reduced by {price_reduce}%")