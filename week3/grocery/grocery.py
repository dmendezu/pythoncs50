list={}
while True:
    try:
        item = input().strip().upper()
        list[item]+=1
        continue
    except KeyError:
        list[item]=1
        continue
    except (EOFError, KeyboardInterrupt):
        print('\n')
        break

list_order=sorted(list.items())

for key, value in list_order:
    print(str(value)+' '+ str(key) )