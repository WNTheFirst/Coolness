no1 = float(input("add your first number: "))
op = input("enter operator: ")
no2 = float(input("add your second number: "))

if op == "+":
  print(no1 + no2)
elif op == "-":
  print(no1 - no2)
elif op == "/":
  print(no1 / no2)
elif op == "*":
  print(no1 * no2)

else:
  print("Invalid Operator.")