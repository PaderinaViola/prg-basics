def m_to_cm(n):
    return n*100

def cm_to_m(n):
    return n/100

def cm_to_inch(n):
    return n/2.54

def inch_feet_to_cm(n, m):
    #first the whole number into inches, so foot in inches + inches, then inches into cm, there are 12 inches in the feet
    total_inches = n * 12 + m
    cm = total_inches * 2.54
    formatted_cm = round(cm, 1)
    return formatted_cm

if __name__ == "__main__":
    # only execute when you run this module
    # so you can test the functions in this place
    print(f'2m = {m_to_cm(2)}cm')
    print(f'532cm = {cm_to_m(532)}m')
    print(f"6.1 inches = {inch_feet_to_cm(6, 1)} cm")

