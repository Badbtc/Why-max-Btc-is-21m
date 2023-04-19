total = 0
C = 0 

while (True):
    halving = int(C / 210000)
    if halving >= 64:
        sub = 0 #Subside
    else:
        sub = (50*100000000) >> halving
    
    total += sub
    print (C, sub, total)
    C += 1
