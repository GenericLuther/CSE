import random
money = int(15)
rolls = int(0)
maxroll = int(0)
maxmoney = int(15)
playing = True
d1 = random.randint(1, 6)
d2 = random.randint(1, 6)
roll = d1+d2
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
            maxroll = rolls
    elif roll > 7:
        money -= 1
        print(" You rolled a %s and a %s" % (d1, d2))
        print(" You have %s Wiebe Coins left" % money)
        rolls += 1
        print(rolls)
    else:  # if roll < 7
        money -= 1
        print(" You rolled a %s and a %s" % (d1, d2))
        print(" You have %s Wiebe Coins left" % money)
        rolls += 1
        print(rolls)

if maxmoney == 15:
    maxmoney = "15.... You Should Have Stayed Home"
print("You Rolled %s Times" % rolls)
print("Your Highest Total Was %s" % maxmoney)
print("You Should Have Stopped On Roll %s" % maxroll)
