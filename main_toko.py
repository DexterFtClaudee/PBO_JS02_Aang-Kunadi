from toko_hp import Handphone

def main():
    print("=== PROGRAM PENJUALAN HP POLINES ===\n")
    # Bikin objek HP
    hp_aang = Handphone("Samsung", "S24 Ultra", 20000000, 5)
    
    # Cek info awal
    hp_aang.info()
    
    # Simulasi beli
    print("\nSedang memproses pembelian 2 unit...")
    hp_aang.jual(2)
    
    # Cek stok akhir
    print("\nUpdate Stok:")
    hp_aang.info()

if __name__ == "__main__":
    main()