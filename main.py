print("Masukan Data Mahasiswa")
data =[]
no = []
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


print("=====================================================================================");
print("|  No  |     Nama     |     NIM     |   Tugas   |   UTS   |   UAS   |  Nilai Akhir  |");
print("=====================================================================================");
i=0
for x in data:
    i+=1
    print("|  {6:2}  |  {0:10}  |  {1:9}  |  {2:7}  |  {3:5}  | {4:6}  |  {5:11.2f}  |"\
          .format (x[0][:9] , x[1][:9],x[2],x[3],x[4],x[5], i))
print("=====================================================================================");