# Tips: PyCharm Shortcuts
# Only run selected block of code in Pycharm
# Select lines of code you wish to run
# press alt + shift + e key for Windows user
# Comment/uncomment a block of code

# Press Ctrl + / key for Windows user

# Indent/Unindent a block of code
# Select lines of code you wish to move
# Press tab key to indent or press shift + tab key to uninden

# A simple Python function: no parameters---无参数
def hello_world():
    print("Hello World")

hello_world() # Calling a function


# Function with parameters and return---自定义参数
# A simple Python function to check
# whether x is even or odd
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
# Driver code to call the function
#---可以整除2为even number
evenOdd(4)
#---不能整除2为odd number
evenOdd(5)

# Python program to demonstrate default arguments--默认参数
def myFun(x, y=50):
    print("x: ", x)
    print("y: ", y)
# Driver code (We call myFun() with only
# argument)
#----默认10为x的值，50是默认的y值
myFun(10)
#---默认10为x的值，50是会被覆盖，y值为4
myFun(10, 4)



# Python program to demonstrate Keyword Arguments----关键字参数
def student(firstname, lastname):
    print(firstname, lastname)
# Keyword arguments
student(firstname='Tony', lastname='Stark')


# Return statement----退出函数，并将指定的值或数据项返回给caller
def square_value(num):
    """This function returns the square
    value of the entered number"""
    return num ** 2#---square为**
print(square_value(2))
print(square_value(-4))


# Here x is a new reference to same list lst
def myFun1(x):
    x[0] = 20

# Driver Code (Note that lst is modified after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun1(lst)
print(lst)#-----改变了第一个值，变成了20
#

def myFun2(x):
    # After below line link of x with previous
    # object gets broken. A new object is assigned
    # to x.
    x = [20, 30, 40]
    return x

# Driver Code (Note that lst is not modified after function call.
lst = [10, 11, 12, 13, 14, 15]
myFun2(lst)
print(lst)
print(myFun2(lst))
#
#
# def myFun3(x):
#     # After below line link of x with previous
#     # object gets broken. A new object is assigned
#     # to x.
#     x = 20
# # Driver Code (Note that x is not modified
# # after function call.
# x = 10
# myFun3(x)
# print(x)
#
#
def mk_csv_name(tic):
    tic = tic.lower()
    tic_base = tic.split('.')[0]
    csv_name = f'{tic_base}_stk_prc.csv'
    return csv_name

mk_csv_name('QAN.AX')



def qan_tic(): # (1)
    tic = "QAN.AX" # (2)
    print(tic) # (3)
    return tic # (4)

print(tic)


def qan_tic():
    tic = "QAN.AX" # <-- local
    print(tic)
tic = "WES.AX" # <-- global
print(qan_tic())
print(tic)


######comprehension
# Create a list with all even integers from 0 to 1 million
evens = []
for x in range(1_000_000 + 1):
    if x % 2 == 0:
        evens.append(x)
print(evens[:10])

# Create a list with all even integers from 0 to 1 million
evens = [x for x in range(1_000_000 + 1) if x % 2 == 0]
print(evens[:10])


data = [
 ('a', 1),
 ('b', 2),
 ('c', 3),
 ]

# Create a dict comprehension
dic = {k:v for k, v in data}
print(f'`dic` is {dic}')
print(f'type(dic) is: {type(dic)}')

# Create a list comprehension
lst = [(k, v) for k, v in data]
print(f'`lst` is {lst}')
print(f'type(lst) is {type(lst)}')

# Create a set comprehension
st = {k for k, v in data}
print(f'`set` is {st}')
print(f'type(set) is {type(st)}')

# Is this a tuple comprehension?
not_a_tup = (k for k, v in data)
print(f'The type of `(k for k, v in data)` is {type(not_a_tup)}')