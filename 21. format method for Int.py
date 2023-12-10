# {index/key:[fill][align][sign][#][0][width][,][.presion]type}

print("{}".format(100)) # No Space is Allowed in brace bracket
print("No Space is allowed in {} brace bracket , we can add {} any number of space in Start End  and Mid".format(100,200))
print("{0} {1}".format(100,200)) # Representing  with key
print("{1}".format(100,200))
print("{x}".format(x=100))
print("{y} {x}".format(x=100,y=200))

print()

print('----------Integer Datatype-----------')  # Bydefault Numbers are align to the left
print("11: {:d}".format(100)) #Repsenting value with Int Datatype 'd' 
print("12: {x:d}".format(x=100)) #Representing with Value 
print("13: {1:d}".format(300,220))  #Representing with Index
print("14: {x:6d}".format(x=100)) # Having width 6
print("15: {x:06d}".format(x=100)) # Having width 6 and padding with zero from Left side
print("16: {x:+6d}".format(x=100)) # + sign added to number 
print("17: {x:+06d}".format(x=102)) # + sign added at starting of the number after that zero added as a padding, but overall width will be of 6 only...Only zero can be used in place of padding.
print("18: {x:<+06d}".format(x=102)) # By default padding is from the left side as we saw in line 17 ... In this case we are using right align so padding will be apply to the right of the number
print("19: {x:<6d}".format(x=100))   # By default number are align to the right, but still we align to the left 
print("20: {x:#<6d}".format(x=100)) # Aligning Number to the right
print("21: {x:*>6d}".format(x=100)) # First number will align to the right after that it will be fill with star
print("22: {x:*<6d}".format(x=100)) #First number will align to the right after that it will be fill with star
print("23: {x:^7d}".format(x=100)) # Number will align at the center but from the right side
print("24: {x:*^7d}".format(x=100))
print("25: {x:,}".format(x=123456789))
print("25: {x:_}".format(x=123456789))

print()

# Thousand seperator
print("-------------- Thousand Seperator-----------------")
print("Thousand Seperator using ','  : {:,}".format(123456789))
print("Thousand Seperator using  '_' : {:_}".format(123456789))

print()

print('------------- First Assigning Value and then Passing Value -------------')
name='Captain America'
power='1000 HP'
print('Power of {} is {} .'.format(name,power))

print()
print('----------- Passing Tuple value -------------')
tup1=(100,200,300)
tup2=(500,600,700)
print('Tuple 1 value: {0[0]} {0[1]} -- Tuple 2 Value: {1[0]} {1[2]}'.format(tup1,tup2))

print()

print('-------- Passing Dictionaries Vaue through Index and Also Specifying datatype -------------')
dict1 ={'Captain America':1000 ,'Iron Man':2000}
dict2 ={'Thor':3000 ,'Spider-Man':4000}
print('Dictionary 1 value: {0[Captain America]} {0[Iron Man]} -- Dictionary 2 Value: {1[Thor]} {1[Spider-Man]}'.format(dict1,dict2))
print('Dictionary 1 value with datatype: {0[Captain America]:d} {0[Iron Man]:d} -- Dictionary 2 Value with datatype: {1[Thor]} {1[Spider-Man]}'.format(dict1,dict2))


print()
print('---------- Naming The Dicitonaries ----------------')
dict1 ={'Captain America':1000 ,'Iron Man':2000}
dict2 ={'Thor':3000 ,'Spider-Man':4000}
print('Dictionary 1 value: {x[Captain America]} {x[Iron Man]} -- Dictionary 2 Value: {y[Thor]} {y[Spider-Man]}'.format(x=dict1,y=dict2))


print()
print('-------- passing value with Format paramter(**) --------')
dict1 ={'Captain America':1000 ,'Iron Man':2000}
dict2 ={'Thor':3000 ,'Spider-Man':4000}
print('Dictionary 1 value: {Captain America} {Iron Man} -- Dictionary 2 Value: {Thor} {Spider-Man}'.format(**dict1,**dict2))















