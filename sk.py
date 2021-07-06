from faker import Faker
import random

#kep_id = 1 - 5
#sk_id,kep_id,sk_nomorsk,sk_validstart,sk_validend
fake = Faker()

def sk():
    sk = open('sk.csv','a')
    sk.write('sk_id,kep_id,sk_nomorsk,sk_validstart,sk_validend')
    for i in range(6,1000000):
        sk_id = i
        kep_id = random.randrange(1,5)
        sk_nomorsk = 'SK/KEPK/' + str(fake.year()) + '.ABC' + str(i)
        sk_validstart = fake.date()
        sk_validend = fake.date()
        sk.write(str(sk_id)+','+str(kep_id)+','+sk_nomorsk+','+sk_validstart+','+sk_validend+'\n')
    sk.close()
        
sk()    