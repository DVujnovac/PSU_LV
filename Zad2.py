try:
    ocjena = float(input("Unesite ocjenu između 0.0 i 1.0: "))
    if (ocjena<0.0 or ocjena>1.0):
        print("Uneseni broj mora biti u između 0.0 i 1.0")
    elif ocjena>=0.9:
        print("A")
    elif ocjena>=0.8:
        print("B")
    elif ocjena>=0.7:
        print("C")
    elif ocjena>=0.6:
        print("D")
    elif ocjena<0.6:
        print("F")
except:
    print("Unos mora biti broj između 0.0 i 1.0")