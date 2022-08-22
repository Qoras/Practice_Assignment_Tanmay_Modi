#r+ , w+ , a+ & operations..

#1 r+ operation do read then write.

print("r+ starts from here")
x=open("/content/prac.txt","r+") #r+ command used
print(x.tell())                  #tells position of counter initially before read
data= x.read()                   # reads file,
print(x.tell())                  #tells position of counter after reading file prac.txt
x.write('Greetings')             #writes Greetings to the file
print(x.tell())                  #tells position of counter after writing 'Greetings' file prac.txt
print(data)                      #prints data which been read & write.
print(x.tell())                  #tells position of counter after printing overall data in file prac.txt


#2 w+ operation do write then read.

print("w+ starts from here")
x=open("/content/prac.txt","w+") #r+ command used.
print(x.tell())                  #tells position of counter initially before read.
x.write('Greetings')             #writes Greetings to the file.
print(x.tell())                  #tells position of counter after writing 'Greetings' file prac.txt.
x.seek(0)                        #makes counter be on position 0.
print(x.tell())                  #tells position of counter after writing 'Greetings' file prac.txt.
data= x.read()                   # reads file.
print(x.tell())                  #tells position of counter after reading file prac.txt.
print(data)                      #prints data which been read & write.
print(x.tell())                  #tells position of counter after printing overall data in file prac.txt.

#2 w+ operation do append then read.

print("a+ starts from here")
x=open("/content/prac.txt","a+") #a+ command used.
print(x.tell())                  #tells position of counter initially before read.
x.write('appends this text ')    #writes Greetings to the file.
print(x.tell())                  #tells position of counter after writing 'Greetings' file prac.txt.                      
data= x.read()                   # reads file.
print(x.tell())                  #tells position of counter after reading file prac.txt.
print(data)                      #prints data which been read & write.
print(x.tell())                  #tells position of counter after printing overall data in file prac.txt.
