strIn=input('Expression: ').strip()

oper=strIn.split()
x=0
y=''
z=0
result=0.0

try:
    x=int(oper[0], base=10)
    y=oper[1]
    z=int(oper[2], base=10)

    if y=='+':
        result=float(x+z)
    elif y=='-':
        result=float(x-z)
    elif y=='*':
        result=float(x*z)
    elif y=='/' and z!=0:
        result=float(x/z)
    else:
        result=0
    print (result)

except:
    print('It is Not Possible')
