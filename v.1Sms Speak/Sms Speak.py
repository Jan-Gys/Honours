"""
Jan-Gys Malan
15462757
Sms Speak using Regular Expressions
"""
import re
import time

text = ""
fh = open("books.txt", "r")
#user = raw_input("Enter message: ")
for item in fh:
    text = item
    print text
    for f in re.findall("([A-Z]+)", text):
        text = text.replace(f, f.lower())
        text = re.sub(r'[^"A-Za-z0-9 "]',"",text)
        text = re.sub(r'\B[aeiou]\B',"",user)
        text = re.sub(r'([a-z])\1', r"\1", user)
        print c
    print time.time() - start_time, "seconds"
