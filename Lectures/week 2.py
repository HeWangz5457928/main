# Try it!
#tic = QAN.AX

# in class excercise
John_said = 'lets learn python together'
print(John_said)
#或者是
c = 'john said: lets learn python together'
print(c)
# Try it!
string3 = '''When Cleese says: 
  "Now that's what I call a dead parrot" '''
print(string3)

x = 0.2 + 0.2
print(x)
print(x == 0.4)#True

x = 0.2 + 0.2 + 0.2
print(x)
print(x == 0.6)# False

import math
x = 0.2 + 0.2 + 0.2
print(math.isclose(x, 0.6))#True

x = "0.2" + "0.2" + "0.2"
print(x)

i = 1
test = i == 1#----Ture
print(test)

x = 1
print(type(x))          # <class 'int'>

xstr = '1'
print(type(xstr))       # <class 'str'>

test = x == xstr        # --> False
print(test)
print(type(test))       # <class 'bool'>

a = 3+2
print(a)   #5
print(type(a))  # integer

b = '3' +'2'
print(b)     #32
print(type(b))   #string

print('c'*3)#表示运作了3次

# 变成大写
x = str('abc')
x_upper=str.upper(x)
print(x_upper)
#或者是更简洁的
y = 'acc'.upper()
print(y)

weird_case = "My fUnNy tYpEcAsE sTrInG"
weird_case_upper = weird_case.upper()
print(weird_case_upper)

weird_case = "My fUnNy tYpEcAsE sTrInG"
# Convert the string to upper case and then to lower case
weird_case_lower = weird_case.upper().lower() # --> "my funny typecase string"
print(weird_case_lower)

#parameter
"Hi".center(40)
"Hi".center(40, '-')

f = 1 / 2.0000000000000000000001
test = f == 1 / 2
print(test)

a = True
b = 5
print(f"The value of a is {a} and the value of b is {b}")
print("The value of a is {} and the value of b is {}".format(a , b))

x = str(5)
print(x) # --> '5'



Length=56
width=33
height=30.5
volume=Length*width*height
print(f"the volume of the box is {volume}cm cubed")
print("the volume of the box is {} cm cubed".format(volume))

line = 'From nickname.surname@unsw.edu.au Tue Oct 06 10:10:15 2020'

domain = line.split()[1].split('@')[1]

print(domain)


#list
lst = [1, 2, 3]
print(lst)

t = type(lst) # --> <class 'list'>
print(t)

lst_a = [1, "string", True, None]
lst_b = ["a" , lst_a]
print(lst_b)

#Append
lst_a = [1]             # lst_a is [1]
list.append(lst_a, 2)   # lst_a is now [1, 2]
print(lst_a)
#建议用这个方式
lst_a = [1]       # lst_a is [1]
lst_a.append(2)   # lst_a is now [1, 2]
print(lst_a)

##Extend
lst_a = [1]
lst_b = [2, 3]
lst_a.extend(lst_b) # --> lst_a now is [1, 2, 3]
print(lst_a)

lst_a = [1]
lst_b = [2, 3]
lst_a.append(lst_b) # --> lst_a now is [1, [2, 3] ]
print(lst_a)

lst = [1, "string", True, None, True]
print(f"Original lst is {lst}")

lst.remove(True)## 1 will be removed
print(f"lst after removing the first True is {lst}")

lst.pop(2)
print(f"lst after removing the element CURRENTLY at index 2 is {lst}")

lst.pop()
print(f"lst after removing the CURRENT last element is {lst}")

#split
Line = ' i am karl'
x = Line.split()
print(x)

# exercise 3: 'From firstname.surname@unsw.edu.au Tue Oct 06 10'
line = 'From firstname.surname@unsw.edu.au Tue Oct 06 10'
domain = line.split()[1].split('@')[1]
print(domain)

#########Tuple---indexing & Indexing and slicing
t = ("word", 5, False)

print(f"The item at index 0 is {t[0]}")
print(f"The item at index 1 is {t[1]}")
print(f"The item at index 2 is {t[2]}")

print(f"The item at index -3 is {t[-3]}")
print(f"The item at index -2 is {t[-2]}")
print(f"The item at index -1 is {t[-1]}")

print(f"The slice from index 0 through 2 is {t[0:2]}" )

###Packing and unpacking
# Create a tuple with two elements
tup = (1, 2)

# unpack the tuple into two variables:
(a, b) = tup

# print
print(f"`a` is {a} and `b` is {b}")
print("a is {} and b is {}".format(a,b))

######Set
s = set()
s.add("QAN.AX")   # s is {"QAN.AX"}
s.add("WES.AX")   # s is {"QAN.AX", "WES.AX"}
s.add("CBA.AX")   # s is {"QAN.AX", "WES.AX", "CBA.AX"}
s.add("CBA.AX")   # s is {"QAN.AX", "WES.AX", "CBA.AX"} (so no change)

print(f"After adding objects, s is {s}")

s.remove("CBA.AX") # s is {"QAN.AX", "WES.AX"}
print(f"After removing 'CBA.AX', s is {s}")

s = {1, 2, 3}
1 in s # --> True
4 in s # --> False

1 not in s # --> False
4 not in s # --> True

s = {1, 2, 3}
n_of_elements = len(s)
print(f"s contains {n_of_elements} objects")

########Dictionary
prc_dic = {
  '2020-01-02': 7.1600,
  '2020-01-03': 7.1900,
  '2020-01-06': 7.0000,
  '2020-01-07': 7.1000,
  '2020-01-08': 6.8600,
  '2020-01-09': 6.9500,
  '2020-01-10': 7.0000,
  '2020-01-13': 7.0200,
  '2020-01-14': 7.1100,
  '2020-01-15': 7.0400,
  }
print(prc_dic)
print(prc_dic['2020-01-02'])###要search the key

###adding &seraching
prc_dic = {
 '2020-01-02': 7.1600,
 '2020-01-03': 7.1900,
 '2020-01-06': 7.0000,
 }
# Modify the value for '2020-01-02'
prc_dic['2020-01-02'] = 1.0000
# Store the next date in the dic
prc_dic['2020-01-07'] = 6.9200
print(prc_dic)

###remove object的时候用pop
d = {'a': 1, 'b': 2 }
d.pop('a')
print(f"After popping 'a', d is now {d}")

###quiz
#Code challenge: Formatting output
#This code challenge provides practice with simple formatting statements and variable creation. Your code should create three variables:
#asx_value: A floating point number with the value of 7111.4
#date: A string with the value of 2021-01-25
#units: An integer with the value of 1
#currency: A string with the value of AUD
#Once these variables are created, write a print statement that outputs:
#The closing value of 1 unit of the All Ordinaries on 2021-01-25 was 7111.4 AUD.

asx_value = 7111.4
date = '2021-01-25'
units = 1
currency = 'AUD'

print(f"The closing value of {units} unit of the All Ordinaries on {date} was {asx_value}{currency}")
print("The closing value of {} unit of the All Ordinaries on {} was {}{}".format(units,date,asx_value,currency))

### quiz list
# Use the provided list_a and list_b as your starting point.
# Then, perform the following steps:
# 1. Create a new list called sol (for solution) consisting of a slice
#    from list_a from the second element through to the word 'it'[1:7}
# 2. Remove the value 'bad' from sol
# 3. Add a value 'including' so that it is the last value in sol
# 4. Add a value 'good' so that it is the third value in sol
# 5. Add all elements from list_b to the end of sol
list_a = ['this', 'list', 'has', 'bad', 'words', 'in', 'it', 'bad', 'naughty', 'impish']
list_b = ['good', 'nice', 'friendly']
sol = list_a[1:7]
print(sol)

sol.pop(2)
print(sol)

sol.append('including')
print(sol)

sol.insert(2,'good')
print(sol)

sol.extend(list_b)
print(sol)

# Use the set f_suburbs as given as your starting point. Then,
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that the suburbs listed below are in your set
#         Fairfield
#         Fairfield East
#         Fairfield Heights
#         Fairfield West
#         Fairlight
#         Fiddletown
#         Five Dock
#         Flemington
#         Forest Glen
#         Forest Lodge
#         Forestville
#         Freemans Reach
#         Frenchs Forest
#         Freshwater

f_suburbs = {"Randwick", "Kensington", "Frenchs Forest", "Flemington"}
f_suburbs.remove("Randwick")
f_suburbs.remove("Kensington")
print(f_suburbs)

f_suburbs.add("Fairfield")

print(f_suburbs)

# Use the dictionary f_suburbs as given as your starting point.
# This dictionary contains Sydney suburb/population pairs,
# with the mapping going from suburb keys to population values.

# Do the following steps:
# 1. Remove all suburbs that don't start with a F
# 2. Ensure that your dictionary contains:
#
#     Fairfield: 18081
#     Fairfield East: 5273
#     Fairfield Heights: 7517
#     Fairfield West: 11575
#     Fairlight: 5840
#     Fiddletown: 233
#     Five Dock: 9356
#     Flemington: None
#     Forest Glen: None
#     Forest Lodge: 4583
#     Forestville: 8329
#     Freemans Reach: 1973
#     Frenchs Forest: 13473
#     Freshwater: 8866

# The None values indicate the Wikipedia did not have population data.
# These should be INCLUDED in your dictionary.

# The None values indicate the Wikipedia did not have population data.
# These should be INCLUDED in your dictionary.

# This dictionary was given to you
f_suburbs = {"Randwick": 29986, "Kensington": 15004, "Frenchs Forest": 13473, "Flemington": None}

f_suburbs.pop("Randwick")
f_suburbs.pop("Kensington")
print(f_suburbs)

f_suburbs[" Fairfield"] = 18081
f_suburbs["Fairfield East"] = 5273
f_suburbs["Fairfield Heights"] = 7517
f_suburbs["Fairfield West"] = 11575
f_suburbs["Fairlight"] = 5840
f_suburbs["Fiddletown"] = 233
f_suburbs["Five Dock"] = 9356
f_suburbs["Flemington"] = None
f_suburbs["Forest Glen"] = None
f_suburbs["Forest Lodge"] = 4583
f_suburbs["Forestville"] = 8329
f_suburbs["Freemans Reach"] = 1973
f_suburbs["Frenchs Forest"] = 13473
f_suburbs["Freshwater"] = 8866
print(f_suburbs)