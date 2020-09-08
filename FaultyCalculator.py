#Exercise2 Faulty_Calculator
# 45 * 3 = 555, 56+9 = 77, 56/6 = 4

print("What do you want to perform? +,-,*,/")
op=input()
num1=int(input("Please enter your first number : "))
num2=int(input("Please enter your second number : "))
if op=="*" and num1==45 and num2==3:
                                print("555")
elif op=="+" and num1==56 and num2==9:
                                   print("77")
elif op=="/" and num1==56 and num2==6:
                                    print("4")
elif op=="+":
            print(num1+num2)
elif op=="*":
            print(num1*num2)
elif op=="-":
            print(num1-num2)
elif op=="/":
            print(num1/num2)
else :
        print("Unexpected Error")
