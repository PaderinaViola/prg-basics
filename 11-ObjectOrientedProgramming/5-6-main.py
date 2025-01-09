from module5_6 import Bank
def main():
    my_acc = Bank("12 3456 5555 9090 1111 0000 7722")
    my_acc.display_status()
    my_acc.deposit(25.30)
    my_acc.display_status()
    my_acc.withdraw(31.70)
    my_acc.display_status()
    my_acc.withdraw(14)
    my_acc.display_status()


if __name__ == "__main__":
   main()