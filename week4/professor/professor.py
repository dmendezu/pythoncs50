from random import randint

def main():
    level_in=get_level()
    if level_in>=1 and level_in<=3:
        operations_list=generate_integer(level_in)
        # print(operations_list)

    good=0
    for ope in operations_list:
        wrong=0
        # print (ope)
        while True:
            try:
                value_input=int(input(ope["operation"]+' = ').strip())
                if value_input==ope["result"]:
                    good+=1
                    break
                else:
                    raise ValueError
            except ValueError:
                print('EEE')
                wrong+=1
                if wrong==3:
                    print (ope["operation"]+' = '+str(ope["result"]))
                    break
                continue
    print('Score:',good)

def get_level():
    while True:
        try:
            level_input=int(input('Level:').strip())

            if level_input>=1 and level_input<=3:
                return level_input
            else:
                raise ValueError
        except ValueError:
            continue


def generate_integer(level):
    operations=[]
    for _ in range(10):
        if level==1:
            value_expected_x = randint(0,9)
            value_expected_y = randint(0,9)
        elif level==2:
            value_expected_x = randint(10,99)
            value_expected_y = randint(10,99)
        elif level==3:
            value_expected_x = randint(100,999)
            value_expected_y = randint(100,999)
        value_result= value_expected_x + value_expected_y
        operations.append({'operation':str(value_expected_x)+' + '+str(value_expected_y),'result':value_result})
    return operations



if __name__ == "__main__":
    main()