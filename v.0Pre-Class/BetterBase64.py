"""
Jan-Gys Malan
15462757
"""
import math

s = open("encode.txt","r")
#decode_table = {}
def words_2_decimal():
    n = ()
    for item in s:
        for letter in item:
            n = int(ord(letter))
            decimal_2_binary(n)

def decimal_2_binary(n):
    '''convert denary integer n to binary string bStr'''
    bStr = ''
    word = []
    if n < 0:  raise ValueError, "must be a positive integer"
    if n == 0: return '0'
    while n > 0:
        bStr = str(n % 2) + bStr
        n = n >> 1
        word.append(bStr)

        
    print bStr
    print word
  

"""
    _6bitA = ''
    _6bitAA = ''
    _6bitB = ''
    _6bitBB = ''
    _6bitC = ''
    _6bitCC = ''
    _6bitD = ''
    _6bitDD = ''
    end = ''

# for every 24 binary digits this will loop until the whole sentence  
# has been converted.

    for nibblets in word:
        _6bitA = _6bit[:5]
        print binascii.b2a_base64(_6bitAA)
        _6bitB = _6bit[6:11]
        print binascii.b2a_base64(_6bitBB)
        _6bitC = _6bit[12:17]
        print binascii.b2a_base64(_6bitCC)
        _6bitD = _6bit[18:23]
        print binascii.b2a_base64(_6bitDD)
        
# creates a string of the final product

        end += _6bitAA + _6bitBB + _6bitCC + _6bitDD


# this will convert every individual character back into binary.
# The binary strings will be combined and returned to their original
# 8bit length and converted back into normal ASCII notation

def words_2_decimal():
    n = ()
    for item in end:
        for letter in item:
            n = binascii.a2b_base64(letter)


def decimal_2_binary(n):
    



"""

    
    


   
  

words_2_decimal()
