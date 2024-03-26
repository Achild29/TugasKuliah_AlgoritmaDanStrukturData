# membuat list kosong dengan nilai element nya 10
kosong = [0 for i in range(10)]
print(kosong)
# update angka pada list kosong 
kosong[:4] = [1, 2, 3, 4]
kosong [7:] = [8, 9, 10]
print(kosong)
# menghapus list pada index ke-4 sampai ke-6
del kosong[4:7]
#menghapus list yang mempunyai nilai elemet 10
kosong.remove(10)
print(kosong)
#Fungsi Built-in List
panjang = len(kosong)
print("Panjang list kosong adalah ", panjang)
print("Nilai terendahnya adalah ", min(kosong))
print("Nilai terbesarnya adalah ", max(kosong))
#methods Built-in List
kosong.reverse()
print("me-reverse list ", kosong)
#List Multi Dimensi
multiDimen = [["Matakuliah", "SKS", "Jadwal"],
              ["Algorimta & Struktur data", 3, "Selasa"],
              ["Perancangan Basis Data", 2, "Senin"]]
print(multiDimen)



