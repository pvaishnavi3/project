print("1 - Add")
print("2 - subtract")
print("3 - multiply")
print("4 - divide")
option = int(input("Choose an opertaion"))

if(option in [1,2,3,4]):
    num1 = int(input("Enter first number: "))
    num2  = int(input("Enter second number: "))

    if(option == 1):
        result = num1 + num2
    elif(option == 2):
        result = num1 - num2
    elif(option == 3): 
        result = num1 * num2
    elif(option == 4): 
        result = num1 // num2    

else:
    print("invalid operation entered")

print("The result of the operation is {}".format(result))              

