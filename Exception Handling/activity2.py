try:
    num1, num2 = eval(input("Enter two numbers, separetad by a comma :"))
    result = num1/num2
    print("Result is", result)

except ZeroDivisionError:
    print("Division by zero is error!!!") 

except SyntaxError:
    print("Comma is missing. Enter numbers with comma like this 1, 2")

except:
    print("Wrong input!")

else:
    print("No exceptions") 

finally:
    print("This will excecute no matter what!")
      