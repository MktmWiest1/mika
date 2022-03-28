
while True:
   x = float(input("введите операцию:"))
   oper = input("введите операцию(+, -, *, /):" )
   y = float(input("введите операцию:"))

   if oper == "+":
       print(x+y)

   elif oper == "-":
       print(x-y)
   elif oper == "*":
       print(x*y)
   elif oper == "/" and y == 0:
       print("на ноль делить нельзя")
   elif oper == "/":
       print(x/y)

   else:
       print("неопознанная операция")

