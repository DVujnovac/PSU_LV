i=0
sum = 0.0
ime = input("Unesi ime tekstualne datoteke: ")
imeD = "C:\\Users\\student\\Desktop\\LV1\\"+ime
try: 
    fhand = open(imeD, 'r')
    for line in fhand:
        line = line.split()
        if ("X-DSPAM-Confidence:" in line):
            i+=1
            sum+=float(line[1])
    print("Avarage X-DSPAM-CONFIDENCE:",sum/i)
except FileNotFoundError: 
    print("The file does not exist.")
