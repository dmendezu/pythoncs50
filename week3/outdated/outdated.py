import re
from datetime import datetime

month=[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

while True:
    try:
        str_date=input('Date:').strip()
        part_date=re.split(r"[\s /\\ ,]+" ,str_date)

        m=part_date[0]
        d=part_date[1]
        y=part_date[2]

        if m.isdigit():
            str_m=f"{int(m):02}"
        elif m.isalpha():
            if str_date.find(',')!=-1:
                str_m=f"{month.index(m)+1:02}"
            else:
                raise ValueError
        if d.isdigit():
            str_d=f"{int(d):02}"
        elif d.isalpha():
            raise ValueError

        new_date=y+'-'+str_m+'-'+str_d

        fecha_dt = datetime.strptime(new_date, '%Y-%m-%d')

        print (new_date)
        break
    except (IndexError,ValueError):
        continue