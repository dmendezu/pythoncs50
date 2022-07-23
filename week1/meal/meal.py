def convert(time):
    timeOut=0.0
    if time.find('a.m.')!=-1:
        hourF=time.split()[0].rsplit(':',1)
        h=int(hourF[0])
        m=int(hourF[1])
    elif time.find('p.m.')!=-1:
        hourF=time.split()[0].rsplit(':',1)
        h=int(hourF[0])
        if h>=1 and h<=11:
            h=h+12
        m=int(hourF[1])
    else:
        hourF=time.rsplit(':',1)
        h=int(hourF[0])
        m=int(hourF[1])

    if (h<0 or h>23) or (m<0 or m>59):
        timeOut=0.0
    else:
        timeOut=h+(m/60)

    return timeOut


def main():
    strIn=input('What time is it?: ').strip()
    hourOut=convert(strIn)

    if hourOut>=7 and hourOut<=8:
        strOut='breakfast time'
    elif hourOut>=12 and hourOut<=13:
        strOut='lunch time'
    elif hourOut>=18 and hourOut<=19:
        strOut='dinner time'
    else:
        strOut=''

    print (strOut)

if __name__ == "__main__":
    main()