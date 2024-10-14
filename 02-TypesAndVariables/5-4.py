amount_string = input("Amount:")
amount = float(amount_string)
vat = amount * 23 / 100
vat = round(vat, 2)
print(f"VAT: {vat}")