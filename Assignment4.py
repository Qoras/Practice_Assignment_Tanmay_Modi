# Advanced Arguments passing in functions: arguments are passed values wrt parameters.

def name(s_name,id):           # s_name & id are two parameters.
  print("Tanmay ",s_name,id)
name("Modi ", "00aed432")      # Modi & 00aed432 are two parameters.

#Positional arguments: # order is set while calling, parameters & arguments respectively.

def com(ip,op,code):          #parameters ip, op, code
  print("My pc having input device as ",ip," & having ",op," screen as output device using ",code," as communication language.") #positional mapped parameters ip, op, code
com("keyboard","led","binary") #positional arguments wrt positional parameters.

#Keyword arguments:
#keyword agruments having keys & values as arguments.

#Default arguments:           
def com(code,ip="keyboard",op="led"):   # Default arguments
  print("My pc having input device as ",ip," & having ",op," screen as output device using ",code," as communication language.")
com("py")           # called function
com("mouse","abacus","py") 

# * arguments: arbitary args:> if we have one arg as static & other args are in multiple in count used * args.
def devices(inp,*var):
  print(inp)
  for x in var:
    print(x)
devices("Joystick",9,8,7)

# ** key words arguments:
def devices(inp,*var,**kvar):
  print(inp)
  for x in var:
    print(x)
  for ip_device in kvar:
    print(ip_device,kvar[ip_device])
devices("Joystick",9,8,7,ip1="mouse",ip2="keyboard")

# To print numbers in ascending order using Function

def asc():
 print("Input some integers sapartaed by space : ")
 nums = list(map(int, input().split()))             # nums variable having mapped splitted input of type int list.
 nums.sort()                                        # sorts integers in list.
 print("Entered Numbers in Ascending orders are :")
 print(*nums)                                       #prints sorted list itegers or values.
asc()

# To print numbers in descending order using Function

def desc():
 print("Input some integers sapartaed by space : ")
 nums = list(map(int, input().split()))           # nums variable having mapped splitted input of type int list.
 nums.sort()                                      # sorts integers in list.
 nums.reverse()                                   # reverse orders of integers in variable nums.
 print("Entered Numbers in Descending orders are :")
 print(*nums)                                     #prints reversed sorted list itegers or values.
desc()

