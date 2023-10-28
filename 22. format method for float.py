print("{}".format(100.12)) # No datatype is Defined It wil be consider as a Stirng
print("{0} {1}".format(100,200)) # Representing  with key
print("{1}".format(100,200))
print("{x}".format(x=100))
print("{y} {x}".format(x=100,y=200))

print()

print('----------Float Datatype-----------')  # Bydefault Numbers are align to the left
print("11: {:f}  If we provide precission by defaut it wi take 6 digit after point ".format(100.12)) #Repsenting value with Int Datatype 'f' 
print("12: {x:7f}  Giving output of 10 width becouse, by default it takes 6 digit after point ".format(x=100.12))  
print("14: {x:.3f} Giving output after 3 precision".format(x=100.12)) 
print("15: {x:8.1f}".format(x=100.12)) # Having width 8 and padding with zero from Left side
print("16: {x:+8.1f}".format(x=100.12)) # + sign added to number 
print("17: {x:+08.1f}".format(x=102)) # + sign added at starting of the number after that zero added as a padding, but overall width will be of 8 only...Only zero can be used in place of padding.
print("18: {x:<+08.1f}".format(x=102)) # By default padding is from the left side as we saw in line 17 ... In this case we are using right align so padding will be apply to the right of the number
print("19: {x:<8.1f}".format(x=100.12))   # By default number are align to the right, but still we align to the left 
print("20: {x:#<8.1f}".format(x=100.12)) # Aligning Number to the right
print("21: {x:*>8.1f}".format(x=100.12)) # First number will align to the right after that it will be fill with star
print("22: {x:*<8.1f}".format(x=100.12)) #First number will align to the right after that it will be fill with star
print("23: {x:^7.1f}".format(x=100.12)) # Number will align at the center but from the right side
print("24: {x:*^7.1f}".format(x=100.12))
print("25: {x:,}".format(x=1234567.89))
print("25: {x:_}".format(x=1234567.89))


