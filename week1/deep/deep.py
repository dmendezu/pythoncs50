strIn=input('What is the answer to the Great Question of Life, the Universe and Everything? ').lower().strip()

if strIn=='42':
    strOut='Yes'
elif strIn=='forty-two':
    strOut='Yes'
elif strIn=='forty two':
    strOut='Yes'
else:
    strOut='No'

print(strOut)