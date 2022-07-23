menu={
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
amount=0
while True:
    try:
        price=0
        if amount>0:
            print("Total: ${:.2f}".format(float(amount)))
        item = input('Item: ').strip().title()
        # print (item)
        price= float(menu[item])
        if price>0:
            amount=amount+price

        continue
    except KeyError:
        continue
    except EOFError:
        print('\n')
        break