price_string = input("Enter price:")
price = float(price_string)
discount_string = input("Enter discount %:")
discount = float(discount_string)
reduction = price * discount / 100 
price_discount = price - reduction
price_discount = round(price_discount, 2)
reduction = round(reduction, 2)
print(f"Price with discount: {price_discount}")
print(f"Reduction: {reduction}")