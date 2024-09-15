print("Enter marks obtained in 4 subjects:")
Math = int(input("math:"))
English = int(input("english:"))
Science = int(input("science:"))
Hindi = int(input("hindi:"))


sum = Math+Science+English+Hindi
print("sum of math, science, english and hindi")
perc = (sum/400)*100

print(end="Percentage Mark =")
print(perc)
