n=int(input("Enter first number: "))
m=int(input("Enter second number: "))
op=input("Enter operation (+, -, *, /): ")
if op=="+":
    print(f"{n} + {m} = {n+m}")
elif op=="-":
    print(f"{n} - {m} = {n-m}")
elif op=="*":
    print(f"{n} * {m} = {n*m}")
elif op=="/":
    if m!=0:
        print(f"{n} / {m} = {n/m}")
    else:
        print("Division by zero is not allowed")