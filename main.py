import re
import math


def combination(n,k):
    num = math.factorial(n)
    denom = math.factorial(k) * (math.factorial(n - k))
    return int(num/denom)

def pos_neg(num):
    if num > 0:
        return("+" + str(num))
    
    if num < 0:
        return(str(num))

def expand(expr):
    returning_string = ""
    
    #parse to get n
    r,n = expr.split("^")
    n = int(n)
    #parse to get x
    r = r.replace("(","")
    r = r.replace(")","")
    letter_pos = re.search("[a-zA-Z]", r)
    l = r[letter_pos.start()]
    
    #parse to get a
    a = r[0:letter_pos.start()]
    if a == '':
        a = 1
    elif a == '-':
        a = -1
    else:
        a = int(a)

    #parse to get b
    b = r[letter_pos.start()+1:]
    if b == '':
        b = 0
    elif b[0] == '+':
        b = int(b[1:])
    elif b[0] == '-':
        b = int(b)
    
    #put together binomial expansion
    for k in range(n+1):
        x = combination(n,k)
        y = a**(n-k)
        z = b**k
        co = x * y * z
        s = pos_neg(co)
        
        t = l + "^" + str(n-k)
        if k == 0:
            if s[0] == "+":
                s = s[1:]
        if k == n:
            t = ""
        if k == n-1:
            t = l
        returning_string = returning_string + s + t
        
    letter_pos = re.search("[a-zA-Z]", returning_string)
    if letter_pos != None:
        l = returning_string[0:letter_pos.start()]
        if l == "1":
            returning_string = returning_string[1:]
        if l == "-1":
            returning_string = returning_string[2:]

        
    return(returning_string)
    
