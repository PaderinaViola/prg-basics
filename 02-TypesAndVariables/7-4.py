circumference = float(input("Enter tree circumference in cm: "))
diameter = circumference / 3.14
cut_tree = diameter >= 50
print(f"Tree can be cut down: {cut_tree}")