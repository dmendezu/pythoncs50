from random import randint

while True:
    try:
        level_input=int(input('Level:').strip())

        if level_input>=0:
            value_expected = randint(1,level_input)
            # print(value_expected)
            while True:
                try:
                    value_input = int(input('Guess:').strip())

                    if value_input==value_expected:
                        print('Just right!')
                        break
                    elif value_input<value_expected:
                        print('Too small!')
                        continue
                    elif value_input>value_expected:
                        print('Too large!')
                        continue
                except (ValueError):
                    continue
        else:
            raise ValueError
        break
    except ValueError:
        continue