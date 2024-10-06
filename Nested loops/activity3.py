num = int(input("Enter a number: "))
t = num
numlen = 0

while t>0:
    numlen = numlen+1
    t = int(t/10)

if numlen>=4:
    numlen = int(numlen/2)
    chk = 0
    while num>0:
        rem = num%10
        if chk==numlen:
            midOne = rem
