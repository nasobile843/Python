lower = int(input("Please enter a lower range : "))
upper = int(input("Please enter a upper range: "))

print("Prime numbers between",lower,"and",upper,"are:")

for num in range(lower,upper + 1):
    if num > 1:
        for i in range (2,num):
            if(num % i) == 0:
                break

        else:
            print(num)

        