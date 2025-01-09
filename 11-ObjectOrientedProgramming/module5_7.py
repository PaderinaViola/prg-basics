class Statistics:
    def __init__(self, array_set):
        self.array_set = array_set

    def numb_space(self):
        without_coma = " ".join(map(str, self.array_set))
        print(without_coma)

    def greatest_numb(self):
        self.greatest_number = max(self.array_set)
    
    def smallest_numb(self):
        self.smallest_number = min(self.array_set)
    
    def ar_mean_numb(self):
        total = 0
        count = 0
        for numbers in self.array_set:
            total += numbers
            count += 1
        self.ar_min = total / count
    
    def median(self):
        n = len(self.array_set)
        self.array_set.sort()
        if n % 2 == 1:  # Odd length
            self.median_ = self.array_set[n // 2]
        else:  # Even length
            mid1 = self.array_set[n // 2 - 1]
            mid2 = self.array_set[n // 2]
            self.median_ = (mid1 + mid2) / 2
    
    def show_everything(self):
        print(f"Minimum: {self.greatest_number}\nMaximum: {self.smallest_number}\nArithmetic mean: {self.ar_min}\nMedian: {self.median_}")

def main():
    my_arr = Statistics([12, 37, 6, 9, 17])
    my_arr.numb_space()
    my_arr.greatest_numb()
    my_arr.smallest_numb()
    my_arr.ar_mean_numb()
    my_arr.median()
    my_arr.show_everything()

if __name__ == "__main__":
   main()