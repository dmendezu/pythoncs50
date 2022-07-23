def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    str_plate=s.strip().upper()
    if len(str_plate)<2 or len(str_plate)>6:
        return False
    else:
        cont=0
        valid=False
        for letter in str_plate:
            cont+=1
            if (cont==1 or cont==2) and letter.isalpha():
                valid=True
            elif cont==3 and (letter.isalpha() or letter.isdigit()):
                if letter!='0': valid=True
                else:
                    valid=False
                    break
            elif cont==4  and (letter.isalpha() or letter.isdigit()):
                if (len(str_plate)>4 and letter=='0'):
                    valid=False
                    break
                else:
                    valid=True
            elif (cont==5 or cont==6 ) and (letter.isalpha() or letter.isdigit()):
                valid=True
            else:
                valid=False
                break
        return valid


if __name__ == "__main__":
    main()