print ('Calculate E=MC^2')
c=300000000
m=input('Insert Mass in Kilograms: ')

try:
    mass=int(m)
    calc=(mass)*c**2
    strExit=str(calc)

except ValueError:
    strExit='The number is Not Integer'

print(strExit)