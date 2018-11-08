import random
money = int(15)
playing = True
d1 = random.randint(1,6)
d2 = random.randint(1,6)
while money > 0 and playing:
    if d1+d2 == 7:
        money += 4
        print("%s" % money)
    if d1+d2 > 7:
        money -= 1
        print("%s" % money)
    if d1+d2 < 7:
        money -= 1
        print("%s" % money)