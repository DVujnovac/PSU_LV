def umnozak(radni, euri):
    return radni*euri

radni = float(input("Unesite radne sate: "))
euri = float(input("Unesite koliko je plaćen sat: "))

ukupno = umnozak(radni, euri)

print("Ukupno: ", ukupno, " eura")