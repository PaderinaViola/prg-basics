class Phone():
    def __init__(self, battery_level, color, storage_capacity):
        self.battery_level = battery_level
        self.color = color
        self.storage_capacity = storage_capacity
        self.basic_bat = 50
    
    def low_bat_warning(self):
        if self.battery_level <= 15:
            print("Charge yo phone")
        else:
            print("Your battery is alr. For now")

    def phone_color(self):
        if self.color == "black" or self.color == "white":
            print("Bro you got boring color")
        else:
            print(f"You have a nice {self.color} color of your phone!!")

    def install_smh(self, app_size):
        if app_size <= self.storage_capacity:
            self.storage_capacity -= app_size
            print(f"The app installed. Remaining storage: {self.storage_capacity}")
        else:
            print("Bruh too big")
    
def main():
    smartphone = Phone(25, "black", 128)
    smartphone.low_bat_warning()
    smartphone.phone_color()
    smartphone.install_smh(30)

if __name__ =="__main__":
    main()