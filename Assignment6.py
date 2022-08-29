#4. Generator Comperehensions
gen_com=(x**2 for x in range(1,11)) # Generation comprehension command used for generation for iterations.
print(next(gen_com))
print(next(gen_com))
print(next(gen_com))
print(next(gen_com))
print(next(gen_com))
print(next(gen_com))
print(next(gen_com))
print(next(gen_com))
print(next(gen_com))

gen_com=(x**2 for x in range(1,11)) # Generation comprehension command used for generation for iterations.
for x in gen_com:                   #first loop :>iteration takes place
   print(x)
for x in gen_com:                   #second loop same as first:. iteration wont take place as generator iterates already.. used for single time.
   print(x)
