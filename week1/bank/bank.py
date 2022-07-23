phrase=input('Greeting: ').lower().strip()

strVal=phrase[0:5]

if strVal=='hello':
    strOut='$0'
elif strVal[0:1]=='h':
    strOut='$20'
else:
    strOut='$100'

print(strOut)