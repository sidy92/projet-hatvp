import csv

cur = baseDonn.cursor()
cur.execute("CREATE TABLE membres (adresse, code postal, pays)")
cur.execute("INSERT INTO membres(adresse,code postal,pays) VALUES('UNION DES PORTS DE FRANCE',75017,'FRANCE')")
cur.execute("INSERT INTO membres(adresse,code postal,pays) VALUES('OBSERVATOIRE DU VEHICULE D ENTREPRISE',92564,'FRANCE')")
cur.execute("INSERT INTO membres(adresse,code postal,pays) VALUES(FEDERAT SCE AUX PARTICULIERS F E S P,75007',FRANCE)")
baseDonn.commit()