import random
money = int(15)
playing = True
d1 = random.randint(1,6)
d2 = random.randint(1,6)
roll= d1+d2
while money > 0 :
    d1 = random.randint(1, 6)
    d2 = random.randint(1, 6)
    roll = d1 + d2
    if roll == 7:
        money += 4
        print(" You rolled a %s and a %s" % (d1, d2))
        print("You have %s Weeb Coins left" % money)
    else:
        money -= 1
        print(" You rolled a %s and a %s" %(d1, d2))
        print (" You have %s Weeb Coins left" % money)