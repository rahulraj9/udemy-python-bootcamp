num1 = int(input("enter the value of num1:- "))
num2 = int(input("enter the value of num2:- "))

print("Before replacing value of \n")
print("num1 is:- %d \nnum2 is :- %d "%(num1,num2))
temp_num = num1
num1 =num2
num2 =temp_num

print("After Replacing the value of \n10")

print("num1 is:- %d \nnum2 is :- %d "%(num1,num2))