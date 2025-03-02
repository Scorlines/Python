import os
import sys
import csv

FILE_NAME = "mahasiswa.csv"

# Memuat data mahasiswa dari file
def load_data():
    mahasiswa = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, mode='r', newline='') as file:
            reader = csv.reader(file)
            for row in reader:
                if row:
                    nim, nama, nilai = row
                    mahasiswa[nim] = {"nama": nama, "nilai": int(nilai)}
    return mahasiswa

# Menyimpan data mahasiswa ke file
def save_data(mahasiswa):
    with open(FILE_NAME, mode='w', newline='') as file:
        writer = csv.writer(file)
        for nim, data in mahasiswa.items():
            writer.writerow([nim, data['nama'], data['nilai']])

# Menambahkan mahasiswa
def tambah_mahasiswa(mahasiswa):
    nim = input("Masukkan NIM: ")
    if nim in mahasiswa:
        print("NIM sudah ada!")
        return
    nama = input("Masukkan Nama: ")
    try:
        nilai = int(input("Masukkan Nilai: "))
    except ValueError:
        print("Nilai harus berupa angka!")
        return
    mahasiswa[nim] = {"nama": nama, "nilai": nilai}
    print("Mahasiswa berhasil ditambahkan!")

# Menampilkan semua mahasiswa
def tampilkan_mahasiswa(mahasiswa):
    print("\n==== DATA MAHASISWA ====")
    print("NIM      | Nama  | Nilai")
    print("-------------------------")
    for nim, data in mahasiswa.items():
        print(f"{nim}  | {data['nama']}  | {data['nilai']}")

# Mencari mahasiswa berdasarkan NIM
def cari_mahasiswa(mahasiswa):
    nim = input("Masukkan NIM yang ingin dicari: ")
    if nim in mahasiswa:
        print("\nData Mahasiswa:")
        print(f"NIM: {nim}\nNama: {mahasiswa[nim]['nama']}\nNilai: {mahasiswa[nim]['nilai']}")
    else:
        print("Mahasiswa tidak ditemukan!")

# Mengedit data mahasiswa
def edit_mahasiswa(mahasiswa):
    nim = input("Masukkan NIM yang ingin diedit: ")
    if nim in mahasiswa:
        nama_baru = input("Nama baru (kosongkan jika tidak ingin mengubah): ")
        nilai_baru = input("Nilai baru (kosongkan jika tidak ingin mengubah): ")
        if nama_baru:
            mahasiswa[nim]['nama'] = nama_baru
        if nilai_baru:
            try:
                mahasiswa[nim]['nilai'] = int(nilai_baru)
            except ValueError:
                print("Nilai harus berupa angka!")
                return
        print("Data berhasil diperbarui!")
    else:
        print("Mahasiswa tidak ditemukan!")

# Menghapus data mahasiswa
def hapus_mahasiswa(mahasiswa):
    nim = input("Masukkan NIM yang ingin dihapus: ")
    if nim in mahasiswa:
        del mahasiswa[nim]
        print("Data mahasiswa berhasil dihapus.")
    else:
        print("Mahasiswa tidak ditemukan!")

# Menjalankan program utama
def main():
    mahasiswa = load_data()
    while True:
        print("\n==== SISTEM PENGELOLAAN DATA MAHASISWA ====")
        print("1. Tambah Mahasiswa")
        print("2. Tampilkan Semua Mahasiswa")
        print("3. Cari Mahasiswa Berdasarkan NIM")
        print("4. Edit Data Mahasiswa")
        print("5. Hapus Data Mahasiswa")
        print("6. Simpan & Keluar")
        pilihan = input("Pilihan: ")
        
        if pilihan == "1":
            tambah_mahasiswa(mahasiswa)
        elif pilihan == "2":
            tampilkan_mahasiswa(mahasiswa)
        elif pilihan == "3":
            cari_mahasiswa(mahasiswa)
        elif pilihan == "4":
            edit_mahasiswa(mahasiswa)
        elif pilihan == "5":
            hapus_mahasiswa(mahasiswa)
        elif pilihan == "6":
            save_data(mahasiswa)
            print("Data mahasiswa telah disimpan. Keluar...")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
