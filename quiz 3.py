#---Q1
l= ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Forest Glen",
    "Forest Lodge",
    "Forestville",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]

for i in l:
    if i[0:5]!="Forest":
        print(i)

print('\n')
# Loop key
for x in l:
    print(x)

# Q2
l = ["Fairfield",
    "Fairfield East",
    "Fairfield Heights",
    "Fairfield West",
    "Fairlight",
    "Fiddletown",
    "Five Dock",
    "Flemington",
    "Freemans Reach",
    "Frenchs Forest",
    "Freshwater"]

for x in l:
    if x!="Forest":
        print(x)

#----Q3
f_suburbs = dict()
f_suburbs["Fairfield"] = 18081
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

#for key,value in  f_suburbs.items():
 #   if key[0:6] != 'Forest' and value != None:
   #     print(key+':',value)
print('\n')
# Loop key and value
for key_value_tuple in f_suburbs.items():
    print(f"key_value_tuple is {key_value_tuple}")
    # Unpacking
    key, value = key_value_tuple
    print(f"KEY: {key} VALUE: {value}")