###
# Calculates the total value of money spent
#
import re # module for regular expressions

# file name with shopping report
email_file = 'report.txt'

# read the content of email
with open(email_file, 'r') as file:
   email_content = file.read()


# regular expression pattern
# for amounts
pattern = r'\d+'

# extract numbers from email
# tip: findall() method returns an array
amounts = re.findall(pattern, email_content)

# calculate the total purchases
total = 0
for amount in amounts:
   total += int(amount)

# print result
print(total)