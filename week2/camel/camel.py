str_in=input('camelCase: ').strip()
cont=0
string_out=''
for letter in str_in:
    if letter.isupper() and cont>0:
        string_out=string_out + '_' + letter.lower()
    elif letter.isupper() and cont==0:
        string_out=string_out + letter.lower()
    else:
        string_out=string_out + letter

    cont+=1

print('snake_case: ',string_out)
