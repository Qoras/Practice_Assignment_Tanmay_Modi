def calc():
  x=int(input("Enter the first value :"))
  y=int(input("Enter the second value :"))
  z=(input("Enter the arithmatic operation you want to perform :"))
  if(z=="+"):
    print("Addition of two numbers is :",x+y)
  elif(z=="-"):
    print("Substraction of two numbers is :",x-y)
  elif(z=="*"):
    print("Multiplication of two numbers is :",x*y)
  elif(z=="/"):
    print("Division of two numbers is :",x/y)
  elif(z=="%"):
    print("Modulus of x over y is :",x%y)

  else:
    print("You have entered a invalid operator!!")
  
calc()
