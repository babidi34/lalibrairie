import csv

with open('passwd.csv',"r", newline="")as f:
    lire = csv.reader(f,delimiter=":")
    with open('passwd2.csv', "a", newline="") as f2:
        ecriture = csv.writer(f2, delimiter=":")
        for row in lire:
            ecriture.writerow(row[0])

