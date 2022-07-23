list_name=[]
while True:
    try:
        name_input = input('Name:').strip().capitalize()
        list_name.append(name_input)
        continue
    except (EOFError, KeyboardInterrupt):
        print('\n')
        break
# print(list_name)
greetings='Adieu, adieu, to '
for i in range(len(list_name)):
    if len(list_name)==1 or i==0:
        greetings=greetings + list_name[i]
    elif len(list_name)==2 and i==1:
        greetings=greetings + ' and '+ list_name[i]
    elif len(list_name)-1==i:
        greetings=greetings + ', and '+ list_name[i]
    else:
        greetings=greetings + ', '+ list_name[i]

print(greetings)
