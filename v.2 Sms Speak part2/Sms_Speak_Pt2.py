"""
Jan-Gys Malan
15462757
"""

import re
import time
lib = {}
text = ""
smse = ""
final = ""
ss = ""
match = 0
no_match = 0
start_time = time.time()

file_in = open('books2.txt')
the_book = open('book.txt','w')
for line in file_in:
    line_fix = line.lower().split()
    if line_fix:
        the_book.write(' '.join(line_fix)+' ')
the_book.close()

transms = open('book.txt')
for kk in transms:
    final += kk
transms.close()

sms_book = open("sms_book.txt","w")

smse = re.sub(r'[^"A-Za-z0-9 "]',"",final)
smse = re.sub(r'\B[aeiou]\B',"",smse)
smse = re.sub(r'([a-z])\1', r"\1", smse)
for it in smse:
    sms_book.write(it)
sms_book.close()

real_sms = smse.split()
old_sms = final.split()
map(lambda k, v: lib.update({k: v}), real_sms, old_sms)
transms.close()

gh = open("reverse.txt", "w")
for back in real_sms:
    if back in lib:
        gh.write(lib[back] + " ")
    else:
        pass


print time.time() - start_time, "seconds"
"""
print " Accuracy "

la = open("sms_book.txt", "r")
lb = open("reverse.txt", "r")

for word in lb:
    print word
for other_word in la:
    print other_word
    if word == other_word:
        match += 1
        print match
    else:
        no_match += 1
        print no_match
"""
