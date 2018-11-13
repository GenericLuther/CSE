import random
money = int(15)
rolls = int(0)
maxmoney = int(15)
playing = True
d1 = random.randint(1,6)
d2 = random.randint(1,6)
roll= d1+d2
while money > 0:
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    roll = d1 + d2
    if roll == 7:
        money += 4
        print(" You rolled a %s and a %s" % (d1, d2))
        print(" You have %s Wiebe Coins left" % money)
        rolls += 1
        print(rolls)
    if maxmoney < money:
        maxmoney = money
    if roll > 7:
        money -= 1
        print(" You rolled a %s and a %s" %(d1, d2))
        print (" You have %s Wiebe Coins left" % money)
        rolls += 1
        print(rolls)
    if roll < 7:
        money -= 1
        print(" You rolled a %s and a %s" %(d1, d2))
        print (" You have %s Wiebe Coins left" % money)
        rolls += 1
        print(rolls)
        print(maxmoney)
    elif money == 0:
        print("You rolled %s times" % rolls)