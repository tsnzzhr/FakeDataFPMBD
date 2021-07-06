from faker import Faker
import random

fake = Faker()
instansi = ['Universitas Airlangga','Universitas Andalas','Universitas Udayana',
            'Universitas Sebelas Maret, Institut Teknologi Bandung, Sekolah Tinggi Ilmu Statistika',
            'Institut Teknologi Sepuluh Nopember','Universitas Hasanudin','Institut Teknologi Sumatera']

name_id = ['F','L','M']
status = ['perbaikan','menunggu']
keputusan = ['diterima','ditolak']
klasifikasi = ['E1','E2','FB']

#detailtelaah = open('dt.csv','a') 
#detailtelaah.write('dt_id,ag_id,sk_id,ht_id,dt_tgltelaah,dt_prta1,dt_prta2,dt_prta3,dt_prta4,dt_prta5,dt_prta6,dt_prtb1,dt_prtb2,dt_rekomklasifikasi,dt_catatantelaah')
#fileku = open('anggota.csv','a')

def generate_test():
    protokol = open('protokol.csv','a')
    hasiltelaah = open('ht.csv','a')
    protokol.write('pr_id,pu_id,pr_judul,pr_tglpengajuan,pr_tglkeputusankep,pr_tglpenugasantim,pr_nosle,pr_tglsle,pr_tgluploadsle,pr__pathfilesle,pr_klasifikasikep\n')
    hasiltelaah.write('ht_id,pr_id,ht_fileproposal,ht_tglsubmitproposal,ht_perbaikanke,ht_statusproses,ht_tglapprovalkep,ht_klasifikasi,ht_keputusan,ht_tglkeputusan,ht_ringkasansekretaris,ht_catatanperbaikan,ht_uploadIC,ht_prta1,ht_prta2,ht_prta3,ht_prta4,ht_prta5,ht_prta6,ht_prtb1,ht_prtb2\n')
    for i in range(1,1000001):
        pu_id = random.randint(1,6)
        pr_id = random.randrange(1,1000000)
        pr_judul = fake.catch_phrase()
        pr_tglpengajuan = fake.date()
        pr_tglkeputusan = fake.date()
        pr_tglpenugasantim = fake.date()
        pr_nosle = fake.catch_phrase()
        pr_tglsle = fake.date()
        pr_tgluploadsle = fake.date()
        pr__pathfilesle = '/Upload/SLE'
        pr_klasifikasikep = klasifikasi[random.randrange(1,3)-1]
        ht_fileproposal = '/Uploads/Proposal'
        ht_tglsubmitproposal = fake.date()
        ht_perbaikanke = random.randrange(1,5)
        ht_statusproses = status[random.randrange(0,2)-1]
        ht_tglapprovalkep = fake.date()
        ht_klasifikasi = klasifikasi[random.randrange(0,3)-1]
        ht_keputusan = keputusan[random.randrange(0,2)-1]
        ht_tglkeputusan = fake.date()
        ht_ringkasansekretaris = fake.sentence()
        ht_catatanperbaikan = fake.sentence()
        ht_uploadIC = '/Uploads/IC'
        ht_prta1 = fake.sentence() 
        ht_prta2 = fake.catch_phrase()
        ht_prta3 = fake.date()
        ht_prta4 = fake.date()
        ht_prta5 = i%2
        ht_prta6 = fake.catch_phrase()
        ht_prtb1 = fake.catch_phrase()
        ht_prtb2 = fake.catch_phrase()
        protokol.write(str(i)+','+ str(pu_id) +','+str(pr_judul)+','+str(pr_tglpengajuan)+','+str(pr_tglkeputusan)+','+str(pr_tglpenugasantim)+','+str(pr_nosle)+','+str(pr_tglsle)+','+str(pr_tgluploadsle)+','+str(pr__pathfilesle)+'/'+str(i)+'.pdf'+','+str(pr_klasifikasikep)+'\n')
        hasiltelaah.write(str(i)+','+str(pr_id)+','+str(ht_fileproposal)+'/'+str(i)+'.pdf'+','+str(ht_tglsubmitproposal)+','+str(ht_perbaikanke)+','+str(ht_statusproses)+','+str(ht_tglapprovalkep)+','+str(ht_klasifikasi)+','+str(ht_keputusan)+','+str(ht_tglkeputusan)+','+str(ht_ringkasansekretaris)+','+str(ht_catatanperbaikan)+','+str(ht_uploadIC)+'/'+str(i)+'.pdf'+','+str(ht_prta1)+','+str(ht_prta2)+','+str(ht_prta3)+','+str(ht_prta4)+','+str(ht_prta5)+','+str(ht_prta6)+','+str(ht_prtb1)+','+str(ht_prtb2)+'\n')
    protokol.close()
    hasiltelaah.close()

generate_test()