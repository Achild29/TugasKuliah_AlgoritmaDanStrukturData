import os

class Buku:
    def __init__(self, judul, penulis, tahun):
        self.judul = judul
        self.penulis = penulis
        self.tahun = tahun

class Perpus:
    def __init__(self):
        self.rak = []
    
    def tambah_buku(self, buku):
        self.rak.append(buku)

    def lihat_rak(self):
        if not self.rak:
            print(f"Belum ada buku di perpustakaan")
            return
        
        print("\nDaftar Buku yang terdapat di Perpustakaan:")
        for i, buku in enumerate(self.rak):
            print(f"{i+1}. Judul: {buku.judul}, Penulis: {buku.penulis}, Tahun: {buku.tahun}")

    def jumlah_buku(self):
        print(f"Jumlah Buku yang tersimpan : {len(self.rak)}")

    def sort_books(self, books, sort_key, reverse=False):
        sorted_books = sorted(books, key=sort_key, reverse=reverse)
        return sorted_books

    def display_sorted_books(self, sort_key, reverse=False):
        sorted_books = self.sort_books(self.rak, sort_key, reverse)
        for buku in sorted_books:
            print(f"Judul: {buku.judul}, Penulis: {buku.penulis}, Tahun: {buku.tahun}")
    
    def pencarian_buku(self, judul, penulis):
        cari = input("Pilih metode pencarian (1: Judul, 2: Penulis): ")
        if cari == '1':
            hasil_pencarian = self.pencarian_judulBuku(judul)
        elif cari == '2':
            hasil_pencarian = self.pencarian_penulisBuku(penulis)
        else:
            print("Metode pencarian tidak valid, ketikan 1 atau 2")
            return []
        
        if hasil_pencarian:
            print("Hasil Pencarian: ")
            for buku in hasil_pencarian:
                print(f"Judul: {buku.judul}, Penulis: {buku.penulis}, Tahun: {buku.tahun}")
        else:
            print("Tidak ada buku yg cocok berdasarkan metode pencarian tersebut")
        return hasil_pencarian

    def pencarian_judulBuku(self, judul):
        hasil_pencarian = []
        for buku in self.rak:
            if judul.lower() in buku.judul.lower():
                hasil_pencarian.append(buku)
        return hasil_pencarian
    
    def pencarian_penulisBuku(self, penulis):
        hasil_pencarian=[]
        for buku in self.rak:
            if penulis.lower() in buku.penulis.lower():
                hasil_pencarian.append(buku)
        return hasil_pencarian
    
    def hapus_buku(self, judul):
        hasil_pencarian = self.pencarian_judulBuku(judul)
        if not hasil_pencarian:
            print("Tidak ada buku yang cocok")
            return
        print("\nHasil Pencarian:")
        for i, buku in enumerate(hasil_pencarian):
            print(f"{i+1}. Judul: {buku.judul}, Penulis: {buku.penulis}, Tahun: {buku.tahun}")
        konfir_hapus=input("\nApakah anda yakin akan menghapusnya? (y/n):")
        if konfir_hapus.lower() != 'y':
            print("Batal Hapus")
            return
        for buku in hasil_pencarian:
            for i, b in enumerate(self.rak):
                if b.judul == buku.judul:
                    del self.rak[i]
                    print("Buky dengan Judul", buku.judul, "Telah dihapus.")
                    break
        # for buku in self.rak:
        #     if buku.judul == judul:
        #         self.rak.remove(buku)
        #         break
        print("Hapus selesai.")

    def MenuUtama(self):
        while True:
            os.system("clear")
            print("Program Perpustkaan sederhana")
            print("Menu: ")
            print("1. Tambahkan Buku ke Perpustakaan") 
            print("2. Lihat Semua Buku yang ada di Perpustkaan")
            print("3. Jumlah Semua Buku yang ada di Perpustkaan")
            print("4. Urutkan Semua Buku Berdasarkan (Judul/Penulis)")
            print("5. Pencarian Buku Berdasarkan (Judul/Penulis)")          
            print("6. Hapus Buku dari Perpustakaan")
            print("7. EXIT")
            pilihan=input("Masukan Pilihan anda(1-8): ")
            if pilihan=='1':
                os.system("clear")
                print("Detail Buku yg akan ditambakan")
                judul=input("Judul Buku: ")
                penulis=input("Penulis Buku: ")
                i='i'
                while(i=='i'):
                    try:
                        tahun=int(input("Tahun Terbit Buku: "))
                    except ValueError:
                        print("Tahun terbit harus berupa angka!")
                        continue
                    i='a'
                bukuBaru = Buku(judul,penulis,tahun)
                self.tambah_buku(bukuBaru)
                print("Buku baru telah ditambahkan di Perpustakaan")
                x=input("")
            elif pilihan=='2':
                os.system("clear")
                self.lihat_rak()
                x=input("")
            elif pilihan=='3':
                os.system("clear")
                self.jumlah_buku()
                x=input("")
            elif pilihan=='4':
                os.system("clear")
                sort_type = input("Urutkan berdasarkan: (1: Judul, 2:Penulis): ")
                if sort_type=='1':
                    sort_key = lambda book: book.judul.lower()
                elif sort_type=='2':
                    sort_key = lambda book: book.penulis.lower()
                else:
                    print("Salah INPUT, masukan 1 atau 2")
                    x=input("")
                    continue
                reverse_sort = input("Urutkan secara Descending? (y/n): ")
                if reverse_sort.lower =='y':
                    reverse=True
                else:
                    reverse=False
                self.display_sorted_books(sort_key,reverse)
                x=input("")
            elif pilihan=='5':
                os.system("clear")
                data = input("Masukan kata kunci pencarian (Judul/Penulis): ")
                judul = data
                penulis = data
                hasil_pencarian = self.pencarian_buku(judul, penulis)
                x=input("")
            elif pilihan=='6':
                os.system("clear")
                judul = input("Masukan judul buku yang akan dihapus: ")
                self.hapus_buku(judul)
                x=input("")
            elif pilihan=='7':
                print("Thanks Bye!")
                x=input("")
                break
            else:
                print("salah input. Masukan 1-7")
                x=input("")

objPerpus = Perpus()
objPerpus.MenuUtama()