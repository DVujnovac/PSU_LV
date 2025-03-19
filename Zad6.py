spamZbr = 0
hamZbr = 0
ham_counter = 0
spam_counter = 0
usklicnici = 0
try:
    dat = open(r'C:\Users\vujno\Desktop\SMSSpamCollection.txt')

except:
    print("Datoteka nije pronadjena")
    exit()

for linija in dat:
    linija = linija.split()
    if linija[0] == 'ham':
        ham_counter += 1
        hamZbr += len(linija[1:])
    elif linija[0] == 'spam':
        spam_counter += 1
        spamZbr += len(linija[1:])
    if linija[-1] == '!':
        usklicnici += 1
print("Prosjecan broj rijeci koje su tipa ham: ", hamZbr/ham_counter)
print("Prosjecan broj rijeci koje su tipa spam: ", spamZbr/spam_counter)
print("Broj poruka koje zavrsavaju sa usklicnikom: ", usklicnici)