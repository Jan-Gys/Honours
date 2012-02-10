"""
Jan-Gys Malan
15462757
"""
import re

lookup2 = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9,
           'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17,
           'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25,
           'z':26}
lookup3 = {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', 6:'f', 7:'g', 8:'h', 9:'i',
           10:'j', 11:'k', 12:'l', 13:'m', 14:'n', 15:'o', 16:'p', 17:'q',
           18:'r', 19:'s', 20:'t', 21:'u', 22:'v', 23:'w', 24:'x', 25:'y',
           26:'z'}

def rot13():
    ct = raw_input("Enter the text: ")
    ct = ct.lower()
    ct = ct.strip()
    cypher = []
    for i in ct:
        if i in lookup2:
            x = int(lookup2.get(i))
            if x + 13 > 26:
                cypher.append(lookup3[x-13])
            else:
                cypher.append(lookup3[x+13])
       
    print cypher
    
        
rot13()

def re_rot13():
    ct2 = raw_input("Enter the text: ")
    ct2 = ct2.lower()
    ct2 = ct2.strip()
    cypher2 = []
    test = re.compile('[a-z]')
    x = test.search(ct2)
    if x:
        for i in ct2:
            if i in lookup2:
                y = int(lookup2.get(i))
            if y + 13 > 26:
                cypher2.append(lookup3[y-13])
            else:
                cypher2.append(lookup3[y+13])                    
    else:
        print "Incorrect input"
    print cypher2
    
re_rot13()
