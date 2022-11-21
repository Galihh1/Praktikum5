# Praktikum5

# PENJELASAN PERULANGAN WHILE PADA PYTHON
*Perulangan while pada python adalah proses pengulangan suatu blok kode program selama sebuah kondisi terpenuhi. Singkatnya, perulangan while adalah perulangan yang bersifat indefinite alias tidak pasti, atau bahkan tidak terbatasSebuah blok kode akan dilakukan terus-menerus selama suatu kondisi terpenuhi. Jika suatu kondisi ternyata tidak terpenuhi pada iterasi ke 10, maka perulangan akan berhenti. Jika kondisi yang sama pada saat yang berbeda ternyata berhenti pada iterasi ke 100, maka perulangan akan berhenti pada jumlah tersebut.*
- Penjelasan lainnya ada [disini](https://www.programiz.com/python-programming/while-loop) dan [disini](https://pythonbasics.org/while-loop/)
# Penulisan Sintaks While
- Kita bisa memulai dengan cara berikut:
```bash
 while <kondisi>:
  # blok kode yang akan diulang-ulang
```

# PERULANGAN TANPA BATAS
Perulangan while **sangat berkaitan** dengan variabel boolean, atau *logical statement*. Karena penentuan **kapan suatu blok kode akan diulang-ulang** ditinjau dari `True` or `False` dari suatu pernyataan logika.

Sehingga jika suatu kondisi itu selalu benar, maka perulangannya pun akan selalu di eksekusi.

## PROGRAM SEDERHANA UNTUK MENAMBAHKAN DATA KEDALAM SEBUAH LIST DENGAN RINCIAN BERIKUT :
- Progam meminta memasukkan data sebanyak-banyaknya (gunakan
perulangan)
- Tampilkan pertanyaan untuk menambah data (y/t?), apabila jawaban
t (Tidak), maka program akan menampilkan daftar datanya.
- Nilai Akhir diambil dari perhitungan 3 komponen nilai (tugas: 30%, uts: 35%, uas: 35%)

# Alur dan Penjelasan program tersebut
 1. Pastikan kita mempunya software pycharm atau vscode, jika belum anda bisa download [Pycharm](https://www.jetbrains.com/pycharm/download/#section=windows) atau [VSCode](https://code.visualstudio.com/download)
 2. Instalasi salah satu software tersebut hingga selesai, lalu buka 
 3. Jika sudah semua masukan kodingan seperti dibawah ini
 ```bash
 print("Masukan Data Mahasiswa")
data =[]
while True :
    nama       = input    ("Nama        : ")
    nim        = input    ("NIM         : ")
    tugas      = int(input("Nilai Tugas : "))
    uts        = int(input("Nilai UTS   : "))
    uas        = int(input("Nilai UAS   : "))
    nilaiakhir = float(tugas)*30/100+(uts)*35/100+(uas)*35/100
    data.append([nama,nim,tugas,uts,uas,nilaiakhir])

    lagi= input("Tambah data (y/t)? ")
    if lagi.lower() =="t":
        break


print("=====================================================================================")
print("|  No  |     Nama     |     NIM     |   Tugas   |   UTS   |   UAS   |  Nilai Akhir  |")
print("=====================================================================================")
i=0
for x in data:
    i+=1
    print("|  {6:2}  |  {0:10}  |  {1:9}  |  {2:7}  |  {3:5}  | {4:6}  |  {5:11.2f}  |"\
          .format (x[0][:9] , x[1][:9],x[2],x[3],x[4],x[5], i))
print("=====================================================================================")
```
![image1.png](screenshot/kod.png)

 4. Lalu save dan Run program tersebut, maka akan keluar hasil
 5. Input data list tersebut terserah yang kita mau, maka akan keluar hasil seperti dibawah ini
![image2.png](screenshot/hasil.png)
**Penjelasan**

- Membuat list bernama data[]
- lalu menggunakan perulangan while
    While True :
Jika benar maka akan menjalankan kodingan selanjutnya yaitu menginput data-data
- Untuk `nama` dan `nim` kita menggunakan fungsi input biasa
- Untuk `tugas`,`uts` dan `uas` kita menggunakan fungsi int untuk menjadikannya integer
- Dibagian nilaiakhir kita menggunakan fungsi `float` karena dapat digunakan sebagai argumen dan dapat juga melakukan operasi hitung secara langsung di dalam fungsi dengan bilangan bertipe integer atau sesama float.
- Membuat kondisi dimana ingin `Tambah Data (y/t)?` jika `y` maka kondisi true dan akan mengulang ke awal untuk iput data selanjutnya.
 Jika `t` maka kondisi akan break, dan apabila kondisi break maka otomatis mengikuti syntax yang berada di luar perulangan seperti contoh yang ada diatas membuat list dengan rapih menggunakan kondisi string.format

- Penjelasan Kondisional dan Perulangan bisa anda akses [disini](https://drive.google.com/file/d/103JBAxfEujCQ9pBUfe3mM8cJo6-CEcET/view)