print ("Half Pyramid Pattern of Numbers(i): ")
n = int(input("Enter number of rows: "))
t = 1
for i in range(n):
    for j in range(1+i):
       print(t, end="")
       t = 1+t
    print()  