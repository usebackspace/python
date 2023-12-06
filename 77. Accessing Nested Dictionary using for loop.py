my_di={1:'Marvel', 2:'DC', 'Hero':{100:'Spider-Man', 200:'Iron-Man'}}

for i in my_di:
    if type(my_di[i]) is dict:
        for j in my_di[i]:
            print(j,":",my_di[i][j])
    else:
        print(i,":",my_di[i])