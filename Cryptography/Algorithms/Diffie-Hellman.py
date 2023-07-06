n = int(input("prime no: \n"))
g = int(input("prime no: \n"))
x = 3
y = 6


def al():
    A = (g**x) % n
    return A


def bob():
    B = (g**y) % n
    return B


def akey():
    Bval = bob()
    k1 = (Bval**x) % n
    return k1


def bkey():
    Aval = al()
    k2 = (Aval**y) % n
    return k2


if akey() == bkey():
    print("shared symmetric key")
    print(akey(), bkey())
else:
    print("error")
