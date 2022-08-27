# Using lambda Function to print table of any number.

import numpy as np

def table():
  i= int(input("Type the no. of which table you want to print : "))
  b= np.arange(1,11)
  print(b)

  n=[lambda x=x:x*i for x in range(1,11)] 
  for n in n:
     print(i*b,"=",n())
   
table()


# To write multiple lines in a file using %s & \n

file =open("a.txt","a") 

line1="This us first line"
line2="This us second line"
line3="This us third line"
file.write("%s \n %s \n %s \n" % (line1, line2, line3))

file =open("a.txt","r") 
print(file.read())
