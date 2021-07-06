### YUK BISA YUK FPNYA!

1- ini yang harus dilakukan pertama kali ya teman-teman. data-data lamanya harus dihapus dulu biar mempermudah import. copas langsung aja dan gak perlu ubah posisi yaa. karena itu dependensinya udah diurutkan:D
```
DELETE FROM PROTOKOL_PENELITI;
DELETE FROM MULTICENTER;
DELETE FROM DETAIL_NILAI_TELAAH;
DELETE FROM MEMBER_PENELAAH;
DELETE FROM HASIL_TELAAH;
DELETE FROM PROTOKOL;
DELETE FROM MEMBER_KEP;
DELETE FROM ANGGOTA;
```
2- ini yang harus dilakukan buat import datanya ya teman-teman. importnya kalo bisa urut. kalo enggak juga gak papa asalkan tabel yang jadi parent harus diimport terlebih dahulu. copas lebih aman. jangan lupa sesuaikan pathnya di PC masing2 ya.
```
COPY PROTOKOL FROM 'D:\stepdal\protokol.csv' DELIMITER ',' csv header;
COPY HASIL_TELAAH FROM 'D:\stepdal\ht.csv' DELIMITER ',' csv header;
COPY ANGGOTA FROM 'D:\stepdal\anggota.csv' DELIMITER ',' csv header;
COPY SK_KEP FROM 'D:\stepdal\sk.csv' DELIMITER ',' csv header;
COPY MEMBER_KEP FROM 'D:\stepdal\mk.csv' DELIMITER ',' csv header;
COPY MEMBER_PENELAAH FROM 'D:\stepdal\mp.csv' DELIMITER ',' csv header;
COPY DETAIL_NILAI_TELAAH FROM 'D:\stepdal\dt.csv' DELIMITER ',' CSV HEADER;
```
