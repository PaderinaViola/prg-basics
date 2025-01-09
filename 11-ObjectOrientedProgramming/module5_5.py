import random
class Thermometer:
    def __init__(self):
        self.status = False

    def turn_on(self):
        self.status = True
        print("Thermometer is on")
    
    def turn_off(self):
        self.status = False
        print("Thermometer is off")

    def measure_temp(self):
        if self.status:
            self.measure = round(random.uniform(34.0, 42.0), 1)
        else:
            print("Cant measure, thermometer is off")
    
    def dislay_temp(self):
        if self.status:
            if self.measure >= 37.0:
                print(f"Temprature: {self.measure} (fever)")
            elif self.measure >= 41.0:
                print(f"Temprature: {self.measure} (CRITICAL TEMPERATURE!!)")
            else:
                print(f"Temprature: {self.measure}")
 