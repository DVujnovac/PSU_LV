'''Napišite program koji od korisnika zahtijeva unos brojeva u beskonačnoj petlji sve dok 
korisnik ne upiše „Done“ (bez navodnika). Pri tome brojeve spremajte u listu. Nakon toga 
potrebno je ispisati koliko brojeva je korisnik unio, njihovu srednju, minimalnu i
maksimalnu vrijednost. Sortirajte listu i ispišite je na ekran. Dodatno: osigurajte program 
od pogrešnog unosa (npr. slovo umjesto brojke) na način da program zanemari taj unos i
ispiše odgovarajuću poruku.'''

lst = []

while True:
    try:
        n = input("Unesi broj(Ili unesi Done za zavrsetak): ")
        if (n=='Done'):
         break
        else:
            lst.append(int(n))
    except:
       print("Navedeni unos mora biti broj ili riječ Done")
duljina = len(lst)
print("Korisnik je unjeo",duljina,"brojeva")
avg = sum(lst)/duljina
print("Srednja vrijednost:", avg)
print("Minimalna vrijednost:", min(lst))
print("Maksimalna vrijednost:", max(lst))