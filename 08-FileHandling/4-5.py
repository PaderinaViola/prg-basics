import re
text = "email.txt"
pattern = r'(From: \w+ \w+ <(\w+.\w+@\w+.com)>)'

def f(text):
    with open(text, 'r') as file:
        content = file.read()
        match = re.search(pattern, content)
        for mail in content:
            if match:
                return match.group(2)
            
print(f(text))

