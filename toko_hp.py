class Handphone:
    def __init__(self, merk, model, harga, stok):
        self.merk = merk
        self.model = model
        self.harga = harga
        self.stok = stok

    def info(self):
        print(f"Gadget: {self.merk} {self.model} | Harga: Rp{self.harga:,} | Stok: {self.stok}")

    def jual(self, jumlah):
        if jumlah <= self.stok:
            self.stok -= jumlah
            total = jumlah * self.harga
            print(f"--- Penjualan Berhasil! ---")
            print(f"Item: {self.model} x{jumlah}")
            print(f"Total Bayar: Rp{total:,}")
        else:
            print(f"--- Gagal! Stok {self.model} tidak cukup (Sisa: {self.stok}) ---")