rijecnik = {}
fhand = open(r'C:\Users\vujno\Desktop\song.txt')
for linija in fhand:
    linija = linija.split()
    for rijec in linija:
        if rijec not in rijecnik:
            rijecnik[rijec] = 1
        else:
            rijecnik[rijec] += 1
        

jednom = []

for rijec in rijecnik:
    if rijecnik[rijec] == 1:
        jednom.append(rijec)

print(rijecnik)
print("Broj rijeci koje se pojavljuju jednom: ", len(jednom))
print(jednom)
    