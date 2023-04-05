# Example of boolean
a=True
print(type(a))
b=False
print(type(b))

#Built-in method bool()
#Returns False as x is not equal to y
x=5
y=10

#Returns False as x is None
x=None
print(bool(x))

#empty False
x=()
print(bool(x))

#empty False
x={}
print(bool(x))

#False with 0
x=0.0
print(bool(x))

#True for non- empty
x='Hlleo_world'
print(bool(x))

#not
print(not True)#---False
print(not False)#---True
#and
print(True and True)#---True
print(True and False)#--False
print(False and False)#--False
#or
print(True or True)#--True
print(True or False)#--True
print(False or True)#--True
print(False or False)#--True