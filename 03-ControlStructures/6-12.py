number_products = int(input("Enter the number of purchased products: "))
price = int(input("Enter the product price: "))
count = 0
if number_products <= 2:
    count = price * number_products
elif number_products > 3:
    reduce = price * 0.25
    count = (price - reduce) * number_products + 20
print(f"Amount to pay: {count}")