

print(f"{5}") # No datatype is Defined It wil be consider as a Stirng


print()


x=100.12
print('----------Float Datatype-----------')  # Bydefault Numbers are align to the left
print(f"11: {x:f}  If we provide precission by defaut it wi take 6 digit after point ") #Repsenting value with Int Datatype 'f' 
print(f"12: {x:7f}  Giving output of 10 width becouse, by default it takes 6 digit after point ")  
print(f"14: {x:.3f} Giving output after 3 precision") 
print(f"15: {x:08.1f}") # Having width 8 and padding with zero from Left side
print(f"16: {x:+8.1f}") # + sign added to number 
print(f"17: {102:+08.1f}".format(x=102)) # + sign added at starting of the number after that zero added as a padding, but overall width will be of 8 only...Only zero can be used in place of padding.
print(f"18: {102:<+08.1f}".format(x=102)) # By default padding is from the left side as we saw in line 17 ... In this case we are using right align so padding will be apply to the right of the number
print(f"19: {x:<8.1f}")   # By default number are align to the right, but still we align to the left 
print(f"20: {x:#<8.1f}") # Aligning Number to the right
print(f"21: {x:*>8.1f}") # First number will align to the right after that it will be fill with star
print(f"22: {x:*<8.1f}") #First number will align to the right after that it will be fill with star
print(f"23: {x:^7.1f}") # Number will align at the center but from the right side
print(f"24: {x:*^7.1f}")
print(f"25: {1234567.89:,}")
print(f"25: {123456789.89:_}")


