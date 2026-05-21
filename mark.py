M1=float(input("Enter M1 value"))
M2=float(input("Enter M2 value"))
M3=float(input("Enter M3 value"))
M4=float(input("Enter M4 value"))
M5=float(input("Enter M5 value"))
print("The M1 is",M1)
print("The M2 is",M2)
print("The M3 is",M3)
print("The M4 is",M4)
print("The M5 is",M5)
if(M1>=50 and M2>=50 and M3>=50 and M4>=50 and M5>=50):
    print("PASS")
    total=M1+M2+M3+M4+M5
    print("Total:",total)
    avg=total/5
    print("AVG:",avg)
    if(avg>=90):
        grade="A+"
    elif(avg>=80):
        grade="A"
    elif(avg>=70):
        grade="B+"
    elif(avg>=60):
        grade="B"
    else:
        grade="C"
    print("Grade:",grade)    
        
else:
    print("FAIL")
