question='Fraction: '

x=0
y=0
result=0.0

while True:
    strIn=input(question).strip()
    try:
        oper=strIn.split(sep='/')
        # print('operacion',oper)
        x=int(oper[0], base=10)
        y=int(oper[1], base=10)
        if x<=y:
            result=int(round(float(x/y),2)*100)
            # print('resultado',result)
            if result<=10:
                str_out='E'
            elif result>=90:
                str_out='F'
            else:
                str_out=str(result)+'%'

            print(str_out)
            break
        else:
            raise ValueError

    except (ValueError, ZeroDivisionError):
        # print('error')
        continue
