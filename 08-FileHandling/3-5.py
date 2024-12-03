###
# Checks the correctness of username and password
#
import re

# read username and password from keyboard
username = input("Enter your username here: ")
password = input("Enter your password here: ")

# pattern (criteria) for username and password
username_pattern = r'\b[a-z]\w{6,}\b'
password_pattern = r'^[a-zA-Z0-9_]{8,}$'

# check if username and password are ok
username_match = re.match(username_pattern, username)
password_match = re.match(password_pattern, password)

# print results
if username_match and password_match:
   print("All set!")
else:
   print("Nah change smth")