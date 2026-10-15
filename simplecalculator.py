a=int(input("enter a number:"))
b=int(input("enter b number:"))
op=int(input("enter the operator(+,-,*,/):"))
if(op=="+"):
  print(a+b)
elif(op=="-"):
  print(a-b)
elif(op=="*"):
  print(a*b)
elif(op=="/"):
  print(a/b)
else:
  print("not a simple calculator")