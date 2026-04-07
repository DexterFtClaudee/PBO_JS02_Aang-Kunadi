# Nama File: praktikum_class.py

class Mahasiswa:
    # Fungsi __init__ untuk inisialisasi data (Atribut)
    def __init__(self, nama, nim, jurusan):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan

    # Method untuk menampilkan data
    def tampilkan_profil(self):
        print(f"Nama    : {self.nama}")
        print(f"NIM     : {self.nim}")
        print(f"Jurusan : {self.jurusan}")
        print("-" * 20)

# Membuat Objek (Instansiasi)
mhs1 = Mahasiswa("Aang Kunadi", "240101", "Teknologi Rekayasa Komputer")
mhs2 = Mahasiswa("Siska", "240102", "Teknik Elektro")

# Memanggil Method
print("Data Mahasiswa Polines:")
mhs1.tampilkan_profil()
mhs2.tampilkan_profil()