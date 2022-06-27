'''I valori vanno da 0 a 256, sono 3 valori per i primi 2 colori e 4 per il terzo, 3 colori ogni cubo, i cubi sono 1000'''


import random
f=open("a.txt", "w")
for i in range(1, 1001):
    f.write("cubo "+str(i)+"\n"+"\t")
    C1="["+"\t"+str(random.randint(0,255))+"\t"+str(random.randint(0,255))+"\t"+str(random.randint(0,255))+"\t"+"]"
    C2="["+"\t"+str(random.randint(0,255))+"\t"+str(random.randint(0,255))+"\t"+str(random.randint(0,255))+"\t"+"]"
    C3="["+"\t"+str(random.randint(0,255))+"\t"+str(random.randint(0,255))+"\t"+str(random.randint(0,255))+"\t"+str(random.randint(0,255))+"\t"+"]"
    f.write(C1+"\t"+C2 +"\t"+C3)
    f.write("\n \n")
f.close()
