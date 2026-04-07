# Nama File: praktikum_mobil.py

class Mobil:
    def __init__(self, merk, tahun, harga_awal):
        self.merk = merk
        self.tahun = tahun
        self.harga = harga_awal

    def hitung_usia_mobil(self, tahun_sekarang):
        usia = tahun_sekarang - self.tahun
        return usia

    def harga_setelah_diskon(self, persen_diskon):
        potongan = self.harga * (persen_diskon / 100)
        return self.harga - potongan

# Penggunaan
mobil_saya = Mobil("Toyota Supra", 2020, 1000000000)

print(f"Mobil: {mobil_saya.merk}")
print(f"Usia Mobil: {mobil_saya.hitung_usia_mobil(2024)} tahun")
print(f"Harga Diskon 10%: Rp{mobil_saya.harga_setelah_diskon(10):,}")