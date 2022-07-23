def findFruit(str_in):
    if (str_in=='apple'): return 130
    elif (str_in=='avocado'): return 50
    elif (str_in=='banana'): return 110
    elif (str_in=='cantaloupe'): return 50
    elif (str_in=='grapefruit'): return 60
    elif (str_in=='grapes'): return 90
    elif (str_in=='honeydew melon'): return 50
    elif (str_in=='kiwifruit'): return 90
    elif (str_in=='lemon'): return 15
    elif (str_in=='lime'): return 20
    elif (str_in=='nectarine'): return 60
    elif (str_in=='orange'): return 80
    elif (str_in=='peach'): return 60
    elif (str_in=='pear'): return 100
    elif (str_in=='pineapple'): return 50
    elif (str_in=='plums'): return 70
    elif (str_in=='strawberries'): return 50
    elif (str_in=='sweet cherries'): return 100
    elif (str_in=='tangerine'): return 50
    elif (str_in=='watermelon'): return 80
    else: return 0

def main():
    str_in=input('Item: ').strip().lower()
    cal=findFruit(str_in)
    if cal!=0:
        print('Calories:',cal)


if __name__ == "__main__":
    main()