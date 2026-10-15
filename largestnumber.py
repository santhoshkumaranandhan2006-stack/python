a=int(input("enter a value:"))
b=int(input("enter b value:"))
c=int(input("enter c value:"))
if((a>b) & (a>c)):
  print("a is greater")
elif((b>a) & (b>c)):
   print("b is greater")
elif((c>a) & (c>b)):
   print("c is greater")
else:
  print("all are equal")