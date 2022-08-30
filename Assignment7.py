# Inheritance, Encapsulation & Polymorphism examples

#1. Inheritance example:

class AI:
 algo="Nieve Byes"     
 nlp_meth="k-means"
 

class win(AI):        # inheriting prperties of AI in win class.
  nn="Neural Networks"
  classifier="Linear"

newobj=win()
print(newobj.algo)

#2. Encapsulation example:

class AI:
  def __init__(algo,sup_ml,unsup_ml):
    algo.sup_ml=sup_ml
    algo.__unsup_ml=unsup_ml      #making an attribute private
  def hided_attr(algo):           #creating attribute private 
    print(algo.__unsup_ml)

obj_ai=AI("KNN","K-means")
print(obj_ai.sup_ml)
#print(obj_ai.__unsup_ml)  # This gives error while making unsup_ml attribute private.
obj_ai.hided_attr() 

#3. Polymorphism example:

class AI:
  def AI_self(self):      # AI_self function having self as a convention.
    print("AI is vast")
  def tech_test(self):
    print("Many techs are not getting under AI")

class ml(AI):      # parrot class inherits AI class
  def tech_test(self):         # polymorphing with tech_test function having different denotation.
    print("ML is under AI")

class ioT(AI):                 # polymorphing with tech_test function having different denotation.
  def tech_test(self):
    print("ioT is not under AI, can collaborate with each other")

tech_test_AI=AI()              # Object creation of class AI 
tech_test_ml=ml()              # Object creation of class ml 
tech_test_ioT=ioT()            # Object creation of class ioT 

tech_test_AI.AI_self()         # function invokes  each time with object generates same output. 
tech_test_AI.tech_test()       # function invokes first time by object generates different output.
tech_test_ml.AI_self()
tech_test_ml.tech_test()       # function invokes second time by object generates different output.
tech_test_ioT.AI_self()
tech_test_ioT.tech_test()      # function invokes third time by object generates different output.
