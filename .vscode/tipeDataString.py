# a. Hitung panjang string
# kata = "Mahasiswa"
kata = input("Masukan kata: ")
panjang_kata = len(kata)
print(f"Panjang kata: {panjang_kata}")

# b. Dapatkan kata "asis" dari string tersebut
kata_asis = kata[3:7]
print(f"Kata 'asis': {kata_asis}")

# c. Jadikan string tersebut menjadi "MAHASISWA"
kata_upper = kata.upper()
print(f"String menjadi 'MAHASISWA': {kata_upper}")

# d. Pisahkan string menjadi "maha siswa"
kata_pisah = kata.split("h")
print(f"String menjadi 'maha siswa': {kata_pisah}")

# e. Jadikan string menjadi "Saya mahasiswa UNPAM"
nama = "Andini"
universitas = "UNPAM"
kalimat = f"Saya {kata.lower()} {universitas}"
print(f"String menjadi 'Saya mahasiswa UNPAM': {kalimat}")
