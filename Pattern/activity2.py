print ("Half Pyramid Pattern of Numbers(i): ")
n = int(input("Enter number of rows: "))
t = 1
for i in range(n):
    for j in range(i+1):
       print(t, end="")
       t = t+1
    print()  