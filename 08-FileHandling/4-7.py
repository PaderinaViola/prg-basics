import re
char = input("Enter: ")
def vowel(char):
    vowel_count = 0
    pattern = r'[aeiouAEIOU]'
    match = re.findall(pattern, char)
    for _ in match:
        vowel_count += 1
    return vowel_count

print(vowel(char))

