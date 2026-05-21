num=(input("enter a number"))
power=len(num)
sum=0
for digit in num:
    sum+=(digit)**power
if sum==(num):
   print(num," is a armstrong number")
else:
    print(num,"is not a armstrong number")
