def convert(strConvert):
    strExit=strConvert.replace(":)","\U0001F642").replace(":(","\U0001F641")
    return (strExit)

def main():
    strImput=input('Insert text with emoji smiling or Frowning face : ');
    ret= convert(strImput)
    print(ret)


if __name__ == "__main__":
    main()