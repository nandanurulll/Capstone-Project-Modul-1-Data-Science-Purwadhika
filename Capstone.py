print("\n\nHallo Nama Saya Nanda Nurul Inayah Sofyan. Berikut Capstone Project Modul I saya:).")

barang_toko = {
    1001 : {"Nama" : "Gunting", "Merk" : "Kenko", "Stock" : 15, "Harga" : 12000},
    1002 : {"Nama" : "Isi Pensil", "Merk" : "Joyko", "Stock" : 20, "Harga" : 7000},
    1003 : {"Nama" : "Penggaris", "Merk" : "Joyko", "Stock" : 10, "Harga" : 6000},
    1004 : {"Nama" : "Highligther", "Merk" : "Deli", "Stock" : 7, "Harga" : 5000},
    1005 : {"Nama" : "Penghapus", "Merk" : "Boxy", "Stock" : 30, "Harga" : 3500}
}


def tabel():
    print(" Kode\t| Nama\t\t\t| Merk\t\t| Stock\t\t| Harga\t\t|")
    for i in barang_toko:
        print(f'{i}\t|{barang_toko[i]["Nama"]}\t\t|{barang_toko[i]["Merk"]}\t\t|{barang_toko[i]["Stock"]}\t\t|{barang_toko[i]["Harga"]}\t\t|')


def Menampilkan():
    print(''' 
    Anda berada dalam Menu Menampilkan Data:

    1. Tampilkan seluruh data
    2. Tampilkan data tertentu
    3. Kembali pada menu utama
    ''')
    opsi = input("Pilih nomor program yang ingin dijalankan:  ")
    opsi = int(opsi)
    if opsi == 1:
        if len(barang_toko.keys()) == 0:
            print("\nDatabase Kosong.")
            Menampilkan()
        else:
            print('\n\tData tersedia.\n')
            tabel()
            Menampilkan()
    elif opsi == 2:
        if len(barang_toko.keys()) == 0:
            print("\nData tidak tersedia.")
            Menampilkan()
        else:
            prim_key = input("Masukkan Kode Barang: ")
            prim_key = int(prim_key)
            if prim_key in list(barang_toko.keys()):
                print(" Kode\t| Nama\t\t\t| Merk\t\t| Stock\t\t| Harga\t\t|")
                print(f'{prim_key}\t|{barang_toko[prim_key]["Nama"]}\t\t|{barang_toko[prim_key]["Merk"]}\t\t|{barang_toko[prim_key]["Stock"]}\t\t|{barang_toko[prim_key]["Harga"]}\t\t|')
                Menampilkan()
            else:
                print("\nTidak ada data.\nMasukkan kode barang dengan benar.")
                Menampilkan()
    elif opsi == 3:
        print('''
    Apakah anda yakin ingin keluar dari Menu Menampilkan Data?
    1. Ya
    2. Tidak
    ''')
        pilih = input("Masukan nomor yang ingin dijalankan: ")
        pilih = int(pilih)
        if pilih == 1:
            print("Kembali pada Menu Utama")
            MenuUtama()
        else:
            Menampilkan()
    else:
        print("\nPilihan yang anda pilih tidak tersedia.")
        Menampilkan()


def Menambahkan():
    print('''
    Anda berada dalam menu Menambahkan Data.

    1. Menambahkan Data Baru
    2. Kembali ke Menu Utama
    ''')
    pilih = input("Masukkan nomor menu yang ingin dijalankan: ")
    pilih = int(pilih)
    if pilih == 1:
        print("\nMasukkan 4 digit kode yang ingin anda tambahkan\n")
        kode_baru = input("Masukkan Kode Barang Baru: ")
        if kode_baru.isdigit():
            if len(kode_baru) == 4 and int(kode_baru) in barang_toko.keys():
                print("\nData Barang dengan kode tersebut sudah digunakan.")
                Menambahkan()
            elif len(kode_baru) == 4 and int(kode_baru) not in barang_toko.keys():
                nama_baru = input("Masukkan Nama Barang baru: ")
                merk_baru = input("Masukkan Merk Barang baru: ")
                stock_baru = input("Masukkan Stock Barang baru: ")
                harga_baru = input("Masukkan Harga Barang baru: ")
                print(''' 
    Apakah anda yakin ingin menambahkan data baru tersebut?
    1. Ya
    2. Tidak
                ''')
                yakin = input("Masukan nomor yang ingin dijalankan: ")
                if int(yakin) == 1:
                    if stock_baru.isdigit() and harga_baru.isdigit():
                        barang_toko.update({
                            int(kode_baru) : {"Nama" : nama_baru, "Merk" : merk_baru, "Stock" : int(stock_baru), "Harga" : int(harga_baru)}
                            })
                        tabel()
                        print("\n\tData baru telah tersimpan.")
                    else:
                        print("\nData baru yang anda masukkan tidak valid. Stock dan harga harus berisi angka.")
                        Menambahkan()
                elif int(yakin) == 2:
                    print("\n\tData baru tidak tersimpan.")
                    tabel()
                else:
                    print("\nPilihan tidak tersedia.\nData baru tidak tersimpan.")
                    MenuUtama()
            elif len(kode_baru) != 4 and int(kode_baru) not in barang_toko.keys():
                print('''
    Kode barang baru yang anda input tidak valid.
    Kode barang harus berupa angka dan harus memiliki 4 karakter.
    ''')
                Menambahkan()
        else:
            print("\nKode barang harus berupa angka dan harus memiliki 4 karakter.")
            Menambahkan()
    elif pilih == 2:
        print('''
    Apakah anda yakin ingin keluar dari Menu Menambahkan Data?
    1. Ya
    2. Tidak
    ''')
        opsi = input("Masukan nomor yang ingin dijalankan: ")
        opsi = int(opsi)
        if opsi == 1:
            print("Kembali pada Menu Utama")
            MenuUtama()
        else:
            Menambahkan()
    else:
        print("Pilihan yang anda pilih tidak tersedia.")
        Menambahkan()


def Mengubah():
    print('''
    Anda berada dalam Menu Mengubah Data:

    1. Mengubah data
    2. Kembali ke Menu Utama
    ''')
    pilih = input("Masukkan nomor menu yang ingin dijalankan: ")
    pilih = int(pilih)
    if pilih == 1:
        if len(barang_toko) == 0:
            print("Database kosong.")
            Mengubah()
        else:
            kode = input("\nMasukkan kode barang data yang ingin anda ubah: ")
            if kode.isdigit():
                if len(kode) == 4 and int(kode) in barang_toko.keys():
                    print("Kode barang yang anda masukkan tersedia.\n")
                    print(" Kode\t| Nama\t\t\t| Merk\t\t| Stock\t\t| Harga\t\t|")
                    print(f'{int(kode)}\t|{barang_toko[int(kode)]["Nama"]}\t\t|{barang_toko[int(kode)]["Merk"]}\t\t|{barang_toko[int(kode)]["Stock"]}\t\t|{barang_toko[int(kode)]["Harga"]}\t\t|')
                    print("\nApakah benar data tersebut yang ingin anda ubah?\n1. Ya\n2. Tidak")
                    pilih_edit = input("Masukkan nomor yang ingin anda pilih: ")
                    pilih_edit = int(pilih_edit)
                    if pilih_edit == 1:
                        print('''
    Pilihan kolom yang dapat anda ubah:
    1. Nama
    2. Merk
    3. Stock
    4. Harga
                        ''')
                        pil_kolom = input("Masukkan angka pilihan kolom yang ingin diubah: ")
                        pil_kolom = int(pil_kolom)
                        if pil_kolom == 1:
                            nama_baru = input(f"Masukkan Nama barang yang baru untuk kode {kode}: ")
                        elif pil_kolom == 2:
                            merk_baru = input(f"Masukkan merk barang yang baru untuk kode {kode}: ")
                        elif pil_kolom == 3:
                            stock_baru = input(f"Masukkan stock barang yang baru untuk kode {kode}: ")
                        elif pil_kolom == 4:
                            harga_baru = input(f"Masukkan harga barang yang baru untuk kode {kode}: ")
                        else:
                            print("\nAngka yang anda masukkan salah.")
                            Mengubah()
                        print('''
    Apakah anda yakin ingin mengubah data?
    1. Ya
    2. Tidak
                            ''')
                        input_pil = input("Masukkan nomor yang ingin dijalankan: ")
                        input_pil = int(input_pil)
                        if input_pil == 1 and pil_kolom == 1:
                            print("\nData telah diubah.")
                            barang_toko[int(kode)] = {"Nama" : nama_baru, "Merk" : barang_toko[int(kode)]["Merk"], "Stock" : barang_toko[int(kode)]["Stock"], "Harga" : barang_toko[int(kode)]["Harga"]}
                            tabel()
                        elif input_pil == 1 and pil_kolom == 2:
                            print("\nData telah diubah.")
                            barang_toko[int(kode)] = {"Nama" : barang_toko[int(kode)]["Nama"], "Merk" : merk_baru, "Stock" : barang_toko[int(kode)]["Stock"], "Harga" : barang_toko[int(kode)]["Harga"]}
                            tabel()
                        elif input_pil == 1 and pil_kolom == 3:
                            if stock_baru.isdigit():
                                print("\nData telah diubah.")
                                barang_toko[int(kode)] = {"Nama" : barang_toko[int(kode)]["Nama"], "Merk" : barang_toko[int(kode)]["Merk"], "Stock" : stock_baru, "Harga" : barang_toko[int(kode)]["Harga"]}
                                tabel()
                            else:
                                print("\nData tidak ter-ubah.\nStock barang harus berupa angka.")
                                Mengubah()
                        elif input_pil == 1 and pil_kolom == 4:
                            if harga_baru.isdigit():
                                print("\nData telah diubah.")
                                barang_toko[int(kode)] = {"Nama" : barang_toko[int(kode)]["Nama"], "Merk" : barang_toko[int(kode)]["Merk"], "Stock" : barang_toko[int(kode)]["Stock"], "Harga" : harga_baru}
                                tabel()
                            else:
                                print("\nData tidak ter-ubah.\nHarga barang harus berupa angka.")
                                Mengubah()
                        else:
                            print("Data tidak jadi diubah.")
                            Mengubah()
                    else:
                        print("\nKembali ke Menu Mengubah Data.")
                        Mengubah()
                elif len(kode) == 4 and int(kode) not in barang_toko.keys():
                    print("\nKode barang yang anda masukkan tidak ada.")
                    Mengubah()
                elif len(kode) != 4:
                    print("\nKode barang harus berisi 4 angka.\nMasukan kode barang dengan benar.")
                    Mengubah()
            else:
                print("\nKode barang harus berupa angka dengan 4 karakter.")
                Mengubah()
    elif pilih == 2:
        print("\nApakah anda yakin ingin keluar dari Menu Mengubah Data?\n1. Ya\n2. Tidak")
        opsi = input("\nMasukan nomor yang ingin dijalankan: ")
        opsi = int(opsi)
        if opsi == 1:
            print("Kembali pada Menu Utama")
            MenuUtama()
        else:
            Mengubah()
    else:
        print("\nPilihan yang anda pilih tidak tersedia.")
        Mengubah()


def Menghapus():
    print('''
    Anda berada dalam Menu Menghapus Data:
    1. Menghapus Data
    2. Kembali ke Menu Utama
    ''')
    pilih = input("Masukkan nomor menu yang ingin anda pilih: ")
    pilih = int(pilih)
    if pilih == 1:
        if len(barang_toko) == 0:
            print("\nDatabase Kosong.")
            Menghapus()
        else:
            kode_hapus = input("\nMasukkan kode Barang yang ingin anda hapus: ")
            if kode_hapus.isdigit():
                if len(kode_hapus) == 4 and int(kode_hapus) in barang_toko.keys():
                    print(" Kode\t| Nama\t\t\t| Merk\t\t| Stock\t\t| Harga\t\t|")
                    print(f'{int(kode_hapus)}\t|{barang_toko[int(kode_hapus)]["Nama"]}\t\t|{barang_toko[int(kode_hapus)]["Merk"]}\t\t|{barang_toko[int(kode_hapus)]["Stock"]}\t\t|{barang_toko[int(kode_hapus)]["Harga"]}\t\t|')
                    print('''
    Apakah betul daftar tersebut yang ingin anda hapus?
    1. Ya
    2. Tidak
                        ''')
                    pilih = input("Masukan nomor yang ingin dijalankan: ")
                    if int(pilih) == 1:
                        barang_toko.pop(int(kode_hapus))
                        tabel()
                        print(f"Daftar barang dengan kode {kode_hapus} telah dihapus dari daftar.")
                        Menghapus()
                    else:
                        print(f"Daftar barang dengan kode {kode_hapus} tidak terhapus dalam daftar.")
                        Menghapus()
                elif len(kode_hapus) == 4 and int(kode_hapus) not in barang_toko.keys():
                    print("\nKode barang yang anda masukkan tidak tersedia.\nMasukkan kode barang dengan benar.")
                    Menghapus()
                elif len(kode_hapus) != 4:
                    print("\nKode barang memiliki 4 karakter.\nMasukkan kode barang dengan benar.")
                    Menghapus()
            else:
                print("Kode barang harus berupa angka dengan 4 karakter.")
                Menghapus()
    elif pilih == 2:
        print("\nApakah anda yakin ingin keluar dari Menu Menghapus Data?\n1. Ya\n2. Tidak")
        opsi = input("\nMasukan nomor yang ingin dijalankan: ")
        opsi = int(opsi)
        if opsi == 1:
            print("Kembali pada Menu Utama")
            MenuUtama()
        else:
            Menghapus()
    else:
        print("\nNomor yang anda pilih tidak tersedia.\nPilih Menu dengan benar.")
        Menghapus()


def MenuUtama():
    print('''
    \t==Selamat datang di Capstone Program Toko Alat Tulis Nanda==\t
    
    Menu Utama:

    1. Menampilkan Data Barang
    2. Menambahkan Data Barang
    3. Mengubah Data Barang
    4. Menghapus Data Barang
    5. Keluar
    ''')
    pilih = int(input("Masukkan nomor menu yang akan anda pilih: "))
    if pilih == 1:
        Menampilkan()
        MenuUtama()
    elif pilih == 2:
        Menambahkan()
        MenuUtama()
    elif pilih == 3:
        Mengubah()
        MenuUtama()
    elif pilih == 4:
        Menghapus()
        MenuUtama()
    elif pilih == 5:
        print('''
    Apakah anda yakin ingin keluar dari program:
    1. Ya
    2. Tidak''')
        opsi = int(input("Pilih opsi: "))
        if opsi == 2:
            print("\nKembali ke Menu Utama.")
            MenuUtama()
        elif opsi == 1:
            print("\nProgram Berakhir.")
            exit()
        else:
            print("\nNomor yang anda masukkan tidak tersedia.")
            MenuUtama()
    else:
        print("Menu tidak tersedia.")
        MenuUtama()

MenuUtama()