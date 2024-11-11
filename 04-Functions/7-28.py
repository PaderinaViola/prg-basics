def f(dice):
    max_digit = dice[0]
    max_count = 1
    current_count = 0
    for i in range(1, len(dice)):
        if dice[i] == dice[i-1]:
            current_count += 1
        else:
            if current_count > max_count:
                max_count = current_count
                max_digit = dice[i - 1]
            current_count = 1
        if current_count > max_count:
            max_digit = dice[-1]
    return int(max_digit)

def main():
    print(f("5233165554211"))
    print(f("2133"))

if __name__ == "__main__":
    main()