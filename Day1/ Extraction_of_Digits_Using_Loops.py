number=12345
digits=[ ]

while number>0:
    digit=number%10
    digits.append(digit)
    number=number//10

print(digits)