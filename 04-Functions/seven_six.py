def hide(card_number):
    card_number = str(card_number)
    if len(card_number) == 16:
        masked_number = card_number[:2] + "*********" + card_number[11:16]
    return masked_number

def main():
    card_number = (int(input("Enter 16 digit card number: ")))
    print(hide(card_number))

if __name__ == "__main__":
    main()
