num = int(input("Enter a number: "))
digits = list(str(num))
power = len(digits)
total = 0
for d in digits:
    total += int(d) ** power
if total == num:
    print(num, "is an Armstrong number")
else:
    print(num, "is not an Armstrong number")
