def my_function(x):
    x = x + 1
    return x

x = 3
print(x)

def my_function(x):
    x = x + 1
    return x

x = 3
x = my_function(x)
print(x)

def my_function(y):
    y = y + x
    x = 2
    y = y + x
    return y

x = 3
y = 10
y = my_function(x)
print(x)
