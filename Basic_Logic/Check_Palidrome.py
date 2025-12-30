n=int(input("Enter a number: "))

num =n
result=0

while num>0:
    digit = num %10
    result = result * 10 +digit
    num = num // 10

if result == n:
    print("palindrome")

else:
    print("not palindrome")
