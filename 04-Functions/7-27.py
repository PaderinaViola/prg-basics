def f(product_code):
    first_num = product_code[0]
    first_num = int(first_num)
    second_num = product_code[1]
    second_num = int(second_num)
    third_num = product_code[2]
    third_num = int(third_num)
    fourth_num = product_code[3]
    fourth_num = int(fourth_num)
    sum_num = first_num + second_num + third_num
    if fourth_num == sum_num % 7:
        return True
    return False

def main():
    print(f("1082"))
    print(f("2035"))
    print(f("1114"))
    print(f("7071"))

if __name__ == "__main__":
    main()