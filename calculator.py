a=int(input("Enter a value"))
b=int(input("Enter b value"))
print("The a value is:",a)
print("The b value is:",b)
print("The choices are:")
print("+","-","*","/","%")
choice=input("Enter your choice")
if(choice=="+"):
    c=a+b
    print("The sum of",a,"and",b,"is",c)
elif(choice=="-"):
    c=a-b
    print("The subtraction of",a,"and",b,"is",c)
elif(choice=="*"):
    c=a*b
    print("The multiplication of",a,"and",b,"is",c)
elif(choice=="/"):
    c=a/b
    print("The division of",a,"and",b,"is",c)
elif(choice=="%"):
    c=a%b
    print("The reminder of",a,"and",b,"is",c)
else:
    print("Invalid input")
