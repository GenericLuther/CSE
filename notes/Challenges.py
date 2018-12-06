# 1.
def challenge1(firstname, lastname):
    return lastname, firstname


print(challenge1('Luther', 'Pavline'))
# 2.


def challenge2(a):
    if a % 2 == 0:
        print(a, "is an even number")
    else:
        print(a, "is an odd number")


print(challenge2(3))
# 3.


def challenge3(h, b):
    return h*b/2


print(challenge3(2, 6))
# 4.


def challenge4(a):
    if a > 0:
        print(a, "is a positive number")
    if a == 0:
        print(a, "is zero")
    elif a < 0:
            print(a, "is a negative number")


print(challenge4(2))
# 5.
def challenge5(r):
    return 3.14159 * r**2


print(challenge5(1.1))
# 6.


def challenge6(r):
    return 4/3 * 3.14159 * r**3


print(challenge6(2))