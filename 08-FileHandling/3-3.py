import re
text = "Alice was born on March 12, 1992. Her brother, John, was born on June 5, 1988. They have a mutual friend named Mike, whose phone number is 555-123-4567. In their hometown, which has a population of 1,234 or 1,235 people, a holiday festival is held every year on December 25. Alice works in an office with 30 employees. Her phone number is 555-765-4321."
dates = re.findall("\w+\s\d{1,2},\s\d{4}", text)
print(dates)
phone_numbers = re.findall("\d{3}-\d{3}-\d{4}", text)
print(phone_numbers)
numbers = re.findall("\d,\d+", text)
print(numbers)
names = re.findall("\b[A-Z][a-z]+\b", text)
print(names)