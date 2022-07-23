import sys
from random import choice
from pyfiglet import Figlet

figlet = Figlet()

if len(sys.argv)<2:
    list_fonts=figlet.getFonts()
    font_apply=choice(list_fonts)
    figlet.setFont(font=font_apply)
    print(figlet.renderText(input('Input: ')))

else:
    try:
        val2=sys.argv[1].lower()
        val3=sys.argv[2].lower()
        if (val2=='-f' or val2=='--font') and val3!='':
            figlet.setFont(font=val3)
            print(figlet.renderText(input('Input: ')))
        else:
            sys.exit('Invalid usage')
    except:
        sys.exit('Invalid usage')
