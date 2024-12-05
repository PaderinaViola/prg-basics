import re
text = "email.txt"
pattern_sender = r'(From: \w+ \w+ <(\w+.\w+@\w+.com)>)'

def sender(text):
    with open(text, 'r') as file:
        content = file.read()
        match = re.search(pattern_sender, content)
        for _ in content:
            if match:
                return match.group(2)
            
print(sender(text))

pattern_recepient = r"(To: \w+ \w+ <(\w+.\w+@\w+.com)>)"

def recepient(text):
    with open(text, 'r') as file:
        content = file.read()
        match = re.search(pattern_recepient, content)
        for _ in content:
            if match:
                return match.group(2)
        
print(recepient(text))

pattern_subject = r"(Subject: (.+))"

def subject(text):
    with open(text, 'r') as file:
        content = file.read()
        match = re.search(pattern_subject, content)
        for _ in content:
            if match:
                return match.group(2)
            
print(subject(text))

pattern_body = r"\r?\n{2}([\s\S]+)"
def body(text):
    with open(text, 'r') as file:
        content = file.read()
        match = re.search(pattern_body, content)
        for _ in content:
            if match:
                return match.group(1)
            
print(body(text))