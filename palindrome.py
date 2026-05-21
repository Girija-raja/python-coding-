n=str(input("Enter a word:"))
print("The word is",n)
rev=n[::-1]
if(n==rev):
    print("Palindrome")
else:
    print("Not palindrome")
