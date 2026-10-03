def judul():
    return "Data Kelas Mahasiswa by Adilla Zaky KELOMPOK 49 SHIFT 8"

def hitung_total_mahasiswa(jml_a, jml_b, jml_c, jml_d):
    return jml_a + jml_b + jml_c + jml_d


class KelasKuliah:
    def __init__(self, nama_kelas, jumlah_mahasiswa):
        self.nama_kelas = nama_kelas
        self.jumlah_mahasiswa = jumlah_mahasiswa

    def tampilkan_info(self):
        print("\n" + "=" * 30)
        print(f"KELAS           : Kelas {self.nama_kelas}")
        print(f"JUMLAH MAHASISWA: {self.jumlah_mahasiswa} orang")
        print("=" * 30)


if __name__ == "__main__":
  print(judul() + "\n")

  kelas_a = KelasKuliah("A", 35)
  kelas_b = KelasKuliah("B", 42)
  kelas_c = KelasKuliah("C", 28)
  kelas_d = KelasKuliah("D", 20)

  sistem_jalan = True

  while sistem_jalan:
    print("\nDATA KELAS KULIAH")
    print("1. Kelas A")
    print("2. Kelas B")
    print("3. Kelas C")
    print("4. Kelas D")
    print("5. Total Seluruh Mahasiswa")
    print("6. Keluar")

    pilihan = input("Pilih menu (1-6): ")

    if pilihan == "1":
      kelas_a.tampilkan_info()
    elif pilihan == "2":
      kelas_b.tampilkan_info()
    elif pilihan == "3":
      kelas_c.tampilkan_info()
    elif pilihan == "4":
      kelas_d.tampilkan_info()
    elif pilihan == "5":
      total = hitung_total_mahasiswa(
          kelas_a.jumlah_mahasiswa,
          kelas_b.jumlah_mahasiswa,
          kelas_c.jumlah_mahasiswa,
          kelas_d.jumlah_mahasiswa,
      )
      print(f"Total Seluruh Mahasiswa (Kelas A - D): {total} orang")
    elif pilihan == "6":
      print("\nDone......")
      sistem_jalan = False
    else:
      print("\nGada pilihannya! Yang bener! PIlih angka 1 sampai 6.")