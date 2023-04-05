
lst1 = ['a']
print(f'This is lst1: {lst1}')
lst2 = ['b', lst1]
print(f'This is lst2: {lst2}')
lst2[1].append('c')
print(f"This is lst2 after modifying it: {lst2}")

###This is lst2 after modifying it: ['b', ['a', 'c']]
print(f"This is lst1 after modifying lst2: {lst1}")
###This is lst1 after modifying lst2: ['a', 'c']

lst1 = ['a']
print(f'This is lst1: {lst1}')
lst3 = ['b', ['a']]
print(f'This is lst3: {lst3}')
lst3[1].append('c')
print(f"This is lst3 after appending 'c': {lst3}")
###This is lst3 after appending 'c': ['b', ['a', 'c']]
print(f"This is lst1 after modifying lst3: {lst1}")
###This is lst1 after modifying lst3: ['a']

# 1 COntrol flow
# 1.1 if statments
happy = False
if happy is True:
 print("I am happy")#不printed这个
print("This will print regardless of the value of happy")


happy = True # <-- This is now True
if happy is True:
 print("I am happy")
print("This will print regardless of the value of happy")  ##both run
# Output
# I am happy
# This will print regardless of the value of happy

happy = True
very_happy = True
if happy is True:
    print("I am happy") # <-- 4 spaces indentation
    if very_happy is True: # <-- 4 spaces indentation
        print("Actually, I'm really happy!") # <-- 8 spaces indentation

happy = True
if happy:
    print("I am happy")

happy = 5
if happy:
    print("I am happy")

print(1 == True)#True
print(1 is True)# error

var1 = 'a'
var2 = 'a'
var3 = ['a']
var4 = ['a']

print(var1 == var2)###string immutable
print(var1 is var2)

print(var3 == var4)##list is mutable
print(var3 is var4)

#-----------The else statement
b = False
if b is True:
 print("b is True")
else:
 print("b is not True")


 a = 0
 b = True
 if a != 0:
     print("a is non-zero")
 elif b is True: #执行这个
     print("b is True")
 elif a < 0 and b is True:
     print("a is negative and b is True")
 else:
     print("None of the conditions above hold")
###python 只执行第一个对的
#Example: What will be printed out from the code below?
a = -1
b = True
if a != 0:
 print("a is non-zero") #执行
elif b is True:
 print("b is True")
elif a < 0 and b is True:
 print("a is negative and b is True")
else:
 print("None of the conditions above hold")

 ##The pass statement
 #the pass is mean "do nothing here"
 happy = True
 if happy is True:
     pass

 if x > 0 and y is True:
     # Write code for this case later
     pass
 elif x <= 0 and y is True:
     # Write code for this case later
     pass
 else:
     # Write code for this case later
     pass

 ####-----------input funtion
 name = input('Who are you?')
 print(type(name))
 print('Welcome to the class,', name)

#------------In-class Exercise 1


hours = input('Enter number of hours you worked this week: ')

#Python 3 output numeric value as a string in input () function
hours = int(hours)
normal_rate = 51.45
overload_rate = 88.9
if hours > 35 :
 pay = (35 * normal_rate) + ((hours - 35) * overload_rate)
else :
 pay = hours * normal_rate
print(f'This weekly payment is: {pay}')

##-------loop
letters_lst = ["a", "b", "c", "d"]
print(letters_lst[0])
print(letters_lst[1])
print(letters_lst[2])
print(letters_lst[3])
#---用loop更简单
letters_lst = ["a", "b", "c", "d"]
for letter in letters_lst:
 print(letter)

import yfinance
start = '2020-01-01'
end = None
tickers = ["QAN.AX", "WES.AX"]
for tic in tickers:
 # Download data from yfinance
 df = yfinance.download(tic, start, end, ignore_tz=True)
 print(df)
 # Get the base name of the ticker
 # E.g. QAN.AX -> qan
 tic_base = tic.lower().split('.')[0]
 # Save data to a csv file named after tic_base
 df.to_csv(f'{tic_base}_stk_prc.csv')

## loop---tuple
for v in ("string", True, 1):
 print(v)

 # Loop set
 tickers = set()
 tickers.add("QAN.AX")  # --相同set只print一次
 tickers.add("QAN.AX")  # --相同的set只print一次
 tickers.add("WES.AX")
 for tic in tickers:
     print(tic)

# Loop dict
d = {
 "beauty": True,
 "truth": True,
 "red wheelbarrow": 100000,
 5: "fingers",
}
# Loop key
for key in d:
    print(key)
# Loop value
for val in d.values():#---只要value不要key
    print(val)


for key_value_tuple in d.items():
 #print(f"key_value_tuple is {key_value_tuple}")
 # Unpacking
 key, value = key_value_tuple
 print(f"KEY: {key} VALUE: {value}")

 d = {
     "beauty": True,
     "truth": True,
     "red wheelbarrow": 100000,
     5: "fingers",
 }
for key, value in d.items():
    print(f'KEY: {key} VALUE: {value}')

 #omitting the `step` parameter
for i in range(0, 5):
 print(f"i is now {i}")

for i in range(0, 5, 1):
     print(f"i is now {i}")

for i in range(5):
 print(f"i is now {i}")

for even in range(0, 10, 2):##---0,2,4,6,8每隔两个空一个
 print(f"even is now {even}")


for i in range(5,0):
 print("This will not execute because start is greater than stop.")
for i in range(5,0,-1):
 print("This message will self-destruct in {} secs...".format(i))

 letters = ["a", "b", "c", "d", "e"]
 for tup in enumerate(letters):
     print(tup)

the_sum = 0
i = 1
while i <= 100:
 the_sum = the_sum + i
 i = i + 1
print(the_sum)

