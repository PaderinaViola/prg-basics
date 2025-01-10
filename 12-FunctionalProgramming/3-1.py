payments_euro = [15.90, 38.47, 4.07, 132.70, 9.15]
payments_pln = list(map(lambda amount: amount * 4.5, payments_euro))
print("Transaction amounts in Polish zlotys (PLN):")
for amount in payments_pln:
    print(amount)