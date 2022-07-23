amount_full=0
amount_due=50
while True:
    print('Amount due:',amount_due-amount_full)
    coin = int(input('Insert Coin:'))
    if coin==5 or coin==10 or coin==25:
        amount_full=amount_full+coin
        if amount_due>amount_full:
            #print('amount_full',amount_full)
            continue
        else:
            print('Change Owed',amount_full-amount_due)
            break
