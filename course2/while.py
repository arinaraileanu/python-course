x = 10
while x > 3:
    print("x e", x)
    x = x - 1
while 1:
    euro = input("valoare inainte de conversie:")
    if euro.isdigit():
        euro = int(euro)
        print("valoarea dupa conversie:", euro * 4.5, "RON")
    else:
        print("introdu un numar!")
    q = input("continuati?")
    if q.upper() == "Q":
        break
    else:
        pass


