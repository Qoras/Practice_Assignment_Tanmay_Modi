# Operators & its some basic implements.

# We have 7 Arithmatic Operators

x=2 # Here '=' is assignment operator stores value 2 in it. 
z=2
x=int(y) # Here '=' is assignment operator stores value of y in x or assigns value int type y in x.

w=x+z # Here '+' is an 'addition' operator category is 'arithmetic' operator.
w=x-z # Here '-' is an 'substraction' operator category is 'arithmetic' operator.
w=x*z # Here '*' is an 'multiplication' operator category is 'arithmetic' operator.
w=x/z # Here '/' is an 'division' operator category is 'arithmetic' operator.
w=x**z # Here '**' is an 'exponant' operator category is 'arithmetic' operator.
w=x//z # Here '//' is an 'floor division' operator category is 'arithmetic' operator.
w=x%z # Here '%' is an 'modulus' operator category is 'arithmetic' operator.
print(w)

# We have 6 Bitwise operators.

w=10 # Assigns value 10 into w variable.
w<<5 # left shift of bits when base its binary or base 2 & returns back values in decimal or base 10.
w>>5 # right shift of bits when base its binary or base 2 & returns back values in decimal or base 10.
w|5 # Binary or base 2 bits o/p 1 if either of one value/bits is one.
w&5 # Binary or base 2 bits o/p 1 if either of both value/bits are one.
w^5 # Binary or base 2 bits o/p 1 if one of both value/bits are one.
~5 # inverts bits or binary value, if 1 o/p will be 0, if 0 o/p will be 1.
print(w)

# We have 13 Assignment operators

y=z # Here '=' assigns value of z in y variable.
x+=5 # Here '+=' operator is first add value to x then assigns to x variable. 
x-=5 # Here '*=' operator is first substracts value to x then assigns to x variable.
x*=5 # Here '-=' operator is first multiplies value to x then assigns to x variable.
x/=5 # Here '/=' operator is first divides value to x then assigns to x variable. 
x%=5 # Here '%=' operator is first take modulus value to x then assigns to x variable.
z<<=5 # Here '<<=' operator is first left shifts value of z then assigns to z variable.
z>>=5 # Here '<<=' operator is first right shifts value of z then assigns to z variable.
z|=5 # Here '|=' operator is first do 'or' operation to value of z then assigns to z variable.
z&=5 # Here '&=' operator is first do 'and' operation to value of z then assigns to z variable.
z^=5 # Here '^=' operator is first do 'XOR' operation to value of z then assigns to z variable.
z**=5 # Here '**=' operator is first exponents to value of z & assigns it to z variable.
z//=5 # Here '//=' operator is first floor division to value of z & assigns it to z variable.

# We have 6 Comparision Operators

list1=[1,2,3,4,5,6,7,8,9] # Here '=' is assignment operator
list2=[9,8,7,6,5,4,3,2]
list3=[1,2,3,4,5,6,7,8,9]
list1of0_index= list1[0]
list2of0_index= list2[0]
list1_len= len(list1)
list2_len= len(list2)

if (list1<list2): # Here '<' is less than operator & category is comaparision operator.
  print("list1 is lesser than list 2")
if (list2>list1): # Here '>' is greater than operator & category is comaparision operator.
  print("list2 is greater than list 1")
else:
  print("invalid")
if ((list1)==(list3)): # Here '==' is equals operator & category is comaparision operator.
  print("both lists are equal")
if ((list1of0_index)<=(list2of0_index)): # Here '<=' is less than equals operator & category is comaparision operator.
  print("Index of list1 is lesser than index of list2")
if ((list1_len)>=(list2_len)): # Here '>=' is greater than equals operator & category is comaparision operator.
  print("length of list1 is greater than length of list2")
if ((list1of0_index)!=(list2of0_index)): # Here '!=' is not equals operator & category is comaparision operator.
  print("Both index values are same")
else:
  ("Both index values are not same")

# We have 3 Logical Operators

if ((list1<list2)and((list1)==(list3))): # Here 'and' operator is checking whether both conditions are true, if true executes block of code.
  print("Yes both conditions are true")
else:
  print("Might be one condition is wrong")

if ((list1<list2)or((list1)==(list3))): # Here 'or' operator is checking either one condition is true, if true executes block of code.
  print("Yes one condition among above two are true")
else:
  print("Might be one condition is wrong")

if (not((list1<list2)and((list1)==(list3)))): # Here 'not' operator is checking niether of one condition is true.
  print("Condition is true")
else:
  print("Condition is false so prints else statement")

# We have 2 Membership Operators.

list4=["Earth","Mars","Vega"]

if("Vega" in list4):
  print("Life is alive")
if("AlphaCentori" not in list4):
  print("Its a star")

# We have 2 Identity Operators.

if("Earth" is list4[0]):
  print("Yes Earth is at index 0 in list4")
if("Mars" is not list4[2]):
  print("Both value & indexes are not addresses same identity")

fruits = {"apple", "banana", "cherry"}
more_fruits = ["orange", "mango", "grapes"]
fruits.update(more_fruits) # update method to add more values of any list in set.
print(fruits)
