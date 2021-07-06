from faker import Faker
import random

fake = Faker()
klasifikasi = ['E1','E2','FB']

dt = open('dt.csv','a')
dt.write('dt_id,ag_id,sk_id,ht_id,dt_tgltelaah,dt_prta1,dt_prta2,dt_prta3,dt_prta4,dt_prta5,dt_prta6,dt_prtb1,dt_prtb2,dt_rekomklasifikasi,dt_catatantelaah\n')

def dnt():
    n = 1
    for i in range(1,1000):
        if i / 10 < 10 and i < 10:
            ag_id = 'A000'+str(i)
        elif i / 100 < 100 and i < 100:
            ag_id = 'B00' + str(i)
        elif i / 1000 < 1000 and i < 1000:
            ag_id = 'C0' + str(i)
        elif i / 1000 == 0:
            ag_id = 'D' + str(i)
        
        if i % 200 != 0:
            sk_id = i % 200
        else :
            sk_id = 200
        
        for j in range(1,5000):
            dt_tgltelaah = fake.date()
            dt_prta1 = fake.sentence()
            dt_prta2 = fake.sentence()
            dt_prta3 = fake.date()
            dt_prta4 = fake.date()
            dt_prta5 = 'true'
            dt_prta6 = fake.sentence()
            dt_prtb1 = fake.sentence()
            dt_prtb2 = fake.sentence()
            dt_rekomklasif = klasifikasi[random.randint(0,2)]    
            dt_catatantelaah = fake.sentence()
            dt.write(str(n)+','+str(ag_id)+','+str(sk_id)+','+str(j)+','+dt_tgltelaah+','+dt_prta1+','+dt_prta2+','+dt_prta3+','+dt_prta4+','+dt_prta5+','+dt_prta6+','+dt_prtb1+','+dt_prtb2+','+dt_rekomklasif+','+dt_catatantelaah+'\n')
            n += 1

dnt()