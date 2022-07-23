str_in=input('Input: ').strip()
string_out=''
for letter in str_in:
    if letter.lower()!='a' and letter.lower()!='e' and letter.lower()!='i' and letter.lower()!='o' and letter.lower()!='u':
        string_out=string_out + letter

print ('Output: ',string_out)