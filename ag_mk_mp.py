from faker import Faker
import random

fake = Faker()
instansi = ['Universitas Airlangga','Universitas Andalas','Universitas Udayana',
            'Universitas Sebelas Maret', 'Institut Teknologi Bandung', 'Sekolah Tinggi Ilmu Statistika',
            'Institut Teknologi Sepuluh Nopember','Universitas Hasanudin','Institut Teknologi Sumatera']

name_id = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P'
            'Q','R','S','T','U','V','W','X','Y','Z']
klasifikasi = ['E1','E2','FB']
#dt_id,ag_id,sk_id,ht_id,dt_tgltelaah,dt_prta1,dt_prta2,dt_prta3,dt_prta4,dt_prta5,dt_prta6,dt_prtb1,dt_prtb2
#mk.write('ag_id,sk_id,mk_role,mk_statusaktif\n')


dt = open('dt.csv','a')
dt.write('dt_id,ag_id,sk_id,ht_id,dt_tgltelaah,dt_prta1,dt_prta2,dt_prta3,dt_prta4,dt_prta5,dt_prta6,dt_prtb1,dt_prtb2,dt_rekomklasifikasi,dt_catatantelaah')

def dnt(ag_id,n):
    for i in range(1,2001):
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
        if i > 199:
            dt.write(str(i)+','+ag_id+','+str(n)+','+str(n)+','+dt_tgltelaah+','+dt_prta1+','+dt_prta2+','+dt_prta3+','
            +dt_prta4+','+dt_prta5+','+dt_prta6+','+dt_prtb1+','+dt_prtb2+','+dt_rekomklasif+','+dt_catatantelaah+'\n')
        else:
            dt.write(str(i)+','+ag_id+','+str(n)+','+str(n)+','+dt_tgltelaah+','+dt_prta1+','+dt_prta2+','+dt_prta3+','
            +dt_prta4+','+dt_prta5+','+dt_prta6+','+dt_prtb1+','+dt_prtb2+','+dt_rekomklasif+','+dt_catatantelaah+'\n')
        n += 1
    

def member_kep(ag_id,n): 
    mp = open('mp.csv','a')
    mk = open('mk.csv','a')
    mk.write(ag_id+','+str(n)+','+'ANGGOTA'+','+'TRUE'+'\n')
    mp.write(ag_id+','+str(n)+','+str(n)+'\n')
    #dnt(ag_id,n)

def anggota():
    ag = open('anggota.csv','a')
    ag.write('ag_id,ag_nama,ag_institusiasal,ag_email,ag_password\n')
    for i in range(1,1001):
        ag_nama = fake.name()
        ag_institusiasal = instansi[random.randint(1,9)-1]
        ag_email = fake.email()
        ag_password = fake.password()
        n = (i % 200)
        if i < 10 :
            ag_id = 'A000'+str(i)
            ag.write(ag_id+','+ag_nama+','+ag_institusiasal+','+ag_email+','+ag_password+'\n')
            member_kep(ag_id,n)
        elif i >= 10 and i < 100 :
            ag_id = 'B00' + str(i)
            ag.write(ag_id+','+ag_nama+','+ag_institusiasal+','+ag_email+','+ag_password+'\n')
            member_kep(ag_id,n)
        elif i >= 100 and i < 1000 :
            ag_id = 'C0' + str(i)
            ag.write(ag_id+','+ag_nama+','+ag_institusiasal+','+ag_email+','+ag_password+'\n')
            member_kep(ag_id,n)
        elif i == 1000 :
            ag_id = 'D' + str(i)
            ag.write(ag_id+','+ag_nama+','+ag_institusiasal+','+ag_email+','+ag_password+'\n')
            member_kep(ag_id,n)
anggota()