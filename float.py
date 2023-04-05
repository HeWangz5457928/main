#(1) create float and check for type
print("create float and check for type")
num=3/4
print(type(num))

# A float is also produced by running an operation on two floats, or a float and an integer.
num_two=6*7.0
print(type(num_two))

#(2) Performing arithemic Operations on float type
print('')
print("Performing arithmetic Operations on float type")

a=5.5
b=3.2

#Addition
c=a+b
print("Addition;",c)

#Subtraction
c=a-b
print("Subtraction;",c)

#Division
c=a//b
print("Divison;",c)

#Multplication
c=a*b
print("Multplication;",c)

#(3) Type conversion using bulit-in functions
print('')
a_2=2
print(type(a_2))
print(float(a_2))
print(int('2')+int('3'))
