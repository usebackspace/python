my_di={1:'Marvel', 2:'DC', 'Hero':{1:'Spider-Man', 2:'Iron-Man'}}

print(my_di[1])

print(my_di[2])

print(my_di['Hero'][1])

print(my_di['Hero'][2])

print(my_di)

print()

my_di[1]='Captain America'

my_di['Hero'][1]='Super-Man'

print(my_di)

print()

my_di[3]='Willian'

print(my_di)

print()

my_di[2]={100:'Steve', 200:'Roger'}

print(my_di)

print()

my_di['Hero'][1]={500:'Tony', 600:'Stark'}

print(my_di)

print(my_di['Hero'][1][500])
