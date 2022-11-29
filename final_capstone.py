#Data Mobil 
data_rental = [
    {'NoPol':'B 1936 QQ', 'Jenis Mobil':'Agya', 'Transmisi':'Matic', 'Harga':250000,'Status':'Available'},
    {'NoPol':'D 7833 HI', 'Jenis Mobil':'Avanza', 'Transmisi':'Manual', 'Harga':350000,'Status':'Available'},
    {'NoPol':'B 8733 KL', 'Jenis Mobil':'Xenia', 'Transmisi':'Manual', 'Harga':400000,'Status':'Available'},
    {'NoPol':'B 5523 NK', 'Jenis Mobil':'Jazz', 'Transmisi':'Matic', 'Harga':300000,'Status':'Available'}
]

#Fungsi Untuk Menu Utama
def list_menu():
    print(f'''\033[94m
    ---------------------------        
              Hallo
    Welcome to Rijan Rent Car!
    ---------------------------
    Menu Utama:
    1. Report Data Mobil
    2. Menambahkan Data Mobil
    3. Mengubah Data Mobil
    4. Menghapus Data Mobil
    5. Data Sewa dan Pengembalian
    9. Exit 
    ''')

#Fungsi Untuk Menu 1
def menu1():
    while True:
        print(f'''
            Pilihan Menu 1
        ------------------------
        1. Report Seluruh Mobil
        2. Report Mobil Tertentu
        9. Kembali ke Menu Utama 
        ''')
        pilih_menu1 = int(input('*Masukkan Pilihan Anda* \n'))
        if pilih_menu1 == 1:
            daftar_mobil()
            break
        elif pilih_menu1 == 2:
            while True:
                menu1_2()
                pilih_menu1_2 = int(input('Masukkan Pilihan Anda: \n'))
                if pilih_menu1_2 == 1:
                    lihat_mobil()
                elif pilih_menu1_2 == 2:
                    lihat_transmisi()
                elif pilih_menu1_2 == 3 :
                    status()
                elif pilih_menu1_2 == 9:
                    break
                else:
                    print('-----------------------------------\nMenu yang dimasukkan tidak tersedia\n-----------------------------------')
                    continue
        elif pilih_menu1 == 9:
            break
        else:
            print('Menu yang dimasukkan tidak tersedia')
            continue

#List Untuk Menu 1.2
def menu1_2():
    print(f'''
              Pilihan Menu 1.2
    ----------------------------------
    1. Cari 1 Mobil Tertentu 
    2. Lihat Daftar Mobil Matic/Manual 
    3. Daftar Mobil Available 
    9. Kembali Ke Menu Sebelumnya 
    ''')

#Fungsi Untuk Menu 2
def menu2():
    while True:
        print(f'''
            Pilihan Menu 2
        ------------------------
        1. Tambah Data Mobil
        9. Kembali ke Menu Utama
        ''')
        pilih_menu2 = int(input('**Masukkan Pilihan Anda** \n'))
        if pilih_menu2 ==1:
            tambah_mobil()
        elif pilih_menu2 == 9:
            break
        else:
            print('Menu yang dimasukkan tidak tersedia')
            continue

#Fungsi Untuk Menu 3
def menu3():
    while True:
        print(f'''
            Pilihan Menu 3
        ------------------------
        1. Ubah Data Mobil
        9. Kembali ke Menu Utama 
        ''')
        pilih_menu3 = int(input('***Masukkan Pilihan Anda*** \n'))
        if pilih_menu3 == 1:
            edit_mobil()
        elif pilih_menu3 == 9:
            break
        else:
            print('Menu yang dimasukkan tidak tersedia')
            continue

#List Untuk Menu 4
def menu4():
    while True:
        print(f'''
            Pilihan Menu 4
        ------------------------
        1. Hapus Data Mobil
        9. Kembali ke Menu Utama 
        ''')
        pilih_menu4 = int(input('****Masukkan Pilihan Anda**** \n'))
        if pilih_menu4 ==1:
            hapus_mobil()
        elif pilih_menu4 ==9:             
            break
        else:
            print('Menu yang dimasukkan tidak tersedia')
            continue

#List Untuk Menu 5
def menu5():
    while True:
        print(f'''
            Pilihan Menu 5
        ------------------------
        1. Sewa Mobil
        2. Pengembalian Mobil
        9. Kembali ke Menu Utama 
        ''')
        pilih_menu5 = int(input('*****Masukkan Pilihan Anda***** \n'))
        if pilih_menu5 ==1:
            sewa_mobil()
            detail_sewa()
            data_sewa.clear()
        elif pilih_menu5 == 2:
            pengembalian(list_penyewa)
        elif pilih_menu5 ==9:             
            break
        else:
            print('Menu yang dimasukkan tidak tersedia')
            continue

#List untuk bagian yang ingin di edit Menu 3
def list_edit():
    print(f'''-----------------------------
Data mana yang ingin di edit?
-----------------------------
1. No. Polisi
2. Jenis Mobil
3. Transmisi
4. Harga Sewa Harian 
5. Status Mobil 
9. Kembali
-----------------------------''')
        
#Untuk data yang berhasil di edit 
def berhasil():
    daftar_mobil()
    print('\n---------------------\nData berhasil di edit\n---------------------')

#Untuk hasil print data tidak jadi di edit
def gagal():
    print('\n----------------------\nData tidak jadi diedit\n----------------------')
    
#Memunculkan Data Mobil Keseluruhan 
def daftar_mobil():
    print('\n                 Daftar Mobil Rijan Rent Car \n-------------------------------------------------------------')
    print(f'{"No":<3}| {"No.Polisi":<10}| {"Jenis Mobil":<12}| {"Transmisi":<10}| {"Harga":<7}| {"Status":<9}')
    No = 1
    for i in data_rental:
        print(f"{No:<3}| {i['NoPol']:<10}| {i['Jenis Mobil']:<12}| {i['Transmisi']:<10}| {i['Harga']:<7}| {i['Status']:<9}")
        No = No+1

#Memunculkan Data Mobil Tertentu 
def lihat_mobil():
    NoPol_user = input('Masukkan Plat Mobil: \n').upper()
    for i in data_rental :
        if (i['NoPol']) == NoPol_user:
            # Print Header 
            No = 1
            print('\n                       Rijan Rent Car \n-------------------------------------------------------------')
            print(f'{"No":<3}| {"No.Polisi":<10}| {"Jenis Mobil":<12}| {"Transmisi":<10}| {"Harga":<7}| {"Status":<9}')
            print(f"{No:<3}| {i['NoPol']:<10}| {i['Jenis Mobil']:<12}| {i['Transmisi']:<10}| {i['Harga']:<7}| {i['Status']:<9}")

    if NoPol_user not in [i['NoPol'] for i in data_rental]:
        print ('--------------------\nMobil Belum Tersedia\n')

#Memunculkan Data Mobil Matic atau Manual
def lihat_transmisi():
    transmisi_user = input('Masukkan Transmisi Mobil: \n').capitalize()
    if transmisi_user not in [i['Transmisi'] for i in data_rental]:
        print ('Mobil Belum Tersedia')
    else:
        No = 1
        print('\n                       Rijan Rent Car \n-------------------------------------------------------------')
        print(f'{"No":<3}| {"No.Polisi":<10}| {"Jenis Mobil":<12}| {"Transmisi":<10}| {"Harga":<7}| {"Status":<9}')
        for i in data_rental :
            if (i['Transmisi']) == transmisi_user:
                # Print Header 
                print(f"{No:<3}| {i['NoPol']:<10}| {i['Jenis Mobil']:<12}| {i['Transmisi']:<10}| {i['Harga']:<7}| {i['Status']:<9}")
                No = No+1

#Memunculkan Data Mobil yang Tersedia 
def status():
    status_user = 'Available'
    No = 1
    print('\n                       Rijan Rent Car \n-------------------------------------------------------------')
    print(f'{"No":<3}| {"No.Polisi":<10}| {"Jenis Mobil":<12}| {"Transmisi":<10}| {"Harga":<7}| {"Status":<9}')
    for i in data_rental :
        if (i['Status']) == status_user:
            # Print Header 
            print(f"{No:<3}| {i['NoPol']:<10}| {i['Jenis Mobil']:<12}| {i['Transmisi']:<10}| {i['Harga']:<7}| {i['Status']:<9}")
            No = No+1

#Menambahkan Data Mobil yang Belum Ada 
def tambah_mobil():
    add_NoPol_user = input('Masukkan Plat Mobil: \n').upper()
    for i in data_rental:
        if (i['NoPol']) == add_NoPol_user:
            print(f''' 
            -----------------------------
                  Mobil sudah ada
            Silahkan cek pada data mobil!
            -----------------------------
            ''')
        else:
            nopol = input('Masukkan plat mobil yang ingin ditambahkan: \n').upper()
            jenis = input('Masukkan jenis mobil: \n').capitalize()
            transmisi = input('Masukkan type transmisi mobil: \n').capitalize()
            harga = int(input('Masukkan tarif sewa harian: \n'))
            status = input('Masukkan status mobil: \n').capitalize()
            cek = input('Apakah Anda yakin ingin menambahkan data ini? (Y/N)').upper()
            if cek == 'Y':
                tambahan_daftar_mobil = {'NoPol':nopol,'Jenis Mobil':jenis,'Transmisi':transmisi, 'Harga':harga, 'Status':status}
                data_rental.append(tambahan_daftar_mobil)
                daftar_mobil()
                break
            else:
                print(f'''
    ---------------------------
    Data Tidak Jadi Ditambahkan
    ---------------------------''')
                break

#Mengedit Data Mobil yang Sudah Ada 
def edit_mobil():
    daftar_mobil()
    while True:
        baris_edit = int(input('\n Masukkan No.Baris yang ingin di edit: \n'))
        if baris_edit not in range(1, len(data_rental)+1):
            print('Tidak ada data pada baris tersebut')
            continue
        else:
            cek2 = input('Apakah Anda yakin ingin edit data ini? (Y/N)').upper()
            if cek2== 'Y':
                list_edit()
                data_edit = int(input('Pilih data yang ingin diedit: \n'))
                if data_edit == 1:
                    nopol_edit = input('Masukkan No.Polisi Baru: \n').upper()
                    cek3 = input('Apakah Anda yakin ingin edit data ini? (Y/N)').upper()
                    if cek3== 'Y':
                        data_rental[baris_edit-1]['NoPol'] = nopol_edit
                        berhasil()
                        break
                    else:
                        gagal()
                        continue 
                elif data_edit == 2:
                    jenis_edit = input('Masukkan Jenis Mobil Baru: \n').capitalize()
                    cek3 = input('Apakah Anda yakin ingin edit data ini? (Y/N)').upper()
                    if cek3== 'Y':
                        data_rental[baris_edit-1]['Jenis Mobil'] = jenis_edit
                        berhasil()
                        break
                    else:
                        gagal()
                        continue 
                elif data_edit == 3:
                    transmisi_edit = input('Masukkan Transmisi Mobil Baru: \n').capitalize()
                    cek3 = input('Apakah Anda yakin ingin edit data ini? (Y/N)').upper()
                    if cek3== 'Y':
                        data_rental[baris_edit-1]['Transmisi'] = transmisi_edit
                        berhasil()
                        break
                    else:
                        gagal()
                        continue
                elif data_edit == 4:
                    harga_edit = int(input('Masukkan Harga Sewa Mobil Baru: \n'))
                    cek3 = input('Apakah Anda yakin ingin edit data ini? (Y/N)').upper()
                    if cek3== 'Y':
                        data_rental[baris_edit-1]['Harga'] = harga_edit
                        berhasil()
                        break
                    else:
                        gagal()
                        continue
                elif data_edit == 5:
                    status_edit = input('Masukkan Status Mobil Saat Ini: ').title()
                    cek3 = input('Apakah Anda yakin ingin edit data ini? (Y/N)').upper()
                    if cek3== 'Y':
                        data_rental[baris_edit-1]['Status'] = status_edit
                        berhasil()
                        break
                    else:
                        gagal()
                        continue
                elif data_edit == 9:
                    break
                else:
                    print('Menu yang dimasukkan tidak tersedia')
                    continue
            else :
                print('Data tidak jadi diedit')
                break 

#Menghapus Data Mobil 
def hapus_mobil():
    daftar_mobil()
    while True:
        hapus_baris = int(input('\n Masukkan baris yang ingin dihapus: '))
        if hapus_baris not in range(1, len(data_rental)+1):
            print('Tidak ada data pada baris tersebut')
            continue
        else:
            cek = str(input('\n Apakah Anda yakin ingin menghapus data? (Y/N) ')).capitalize()
            if (cek == 'Y'):
                del data_rental[hapus_baris-1]
                daftar_mobil()
                print('Data berhasil dihapus')
                break
            else:
                print('Data tidak jadi dihapus')
                break

list_penyewa =[]
data_sewa = []

def lihat_report(list):
    No = 1
    print(f'\n{"No":<3}| {"Nama Penyewa":<10}| {"No.Polisi":<10}| {"Jenis Mobil":<12}| {"Harga":<10}| {"Durasi":<7}| {"Total Bayar":<9}')
    for i in range(len(list)) :
        print(f"{No:<3}| {list[i][0]:<10}| {list[i][1]:<10}| {list[i][2]:<12}| {list[i][3]:<10}| {list[i][4]:<7}| {list[i][5]:<9}")
        No = No+1

def sewa_mobil():
    daftar_mobil() 
    nama = input('Masukkan Nama Penyewa: ')
    while True:
        i  = int(input('Masukkan pilihan mobil yang ingin disewa: '))
        if i in range(len(data_rental)+1) and data_rental[i-1]['Status'] == 'Available':
            sewa = int(input('Berapa lama mobil di sewa? ... Hari :  '))
            total = sewa * data_rental[i-1]['Harga']
            status = 'Rented by ' + nama
            data_rental[i-1]['Status'] = status
            data_sewa.append([nama, data_rental[i-1]['NoPol'], data_rental[i-1]['Jenis Mobil'],data_rental[i-1]['Harga'], sewa, total])
            list_penyewa.append([nama, data_rental[i-1]['NoPol'], data_rental[i-1]['Jenis Mobil'],data_rental[i-1]['Harga'], sewa, total])
            
            cek = input('Apakah ada tambahan mobil yang ingin disewa? (Y/N): ').capitalize()
            if cek == 'Y':
                daftar_mobil()
                continue
            else:
                break
        else:
            print(f"Mobil tidak tersedia/ mobil telah disewa")
            continue

    print(f'\n{"No":<3}| {"Nama Penyewa":<14}| {"No.Polisi":<10}| {"Jenis Mobil":<12}| {"Harga":<10}| {"Durasi":<7}| {"Total Bayar":<9}')
    No = 1
    for item in data_sewa:
        print(f"{No:<3}| {item[0]:<14}| {item[1]:<10}| {item[2]:<12}| {item[3]:<10}| {item[4]:<7}| {item[5]:<9}")
        No = No+1

def detail_sewa():
    print('\nDetail sewa')
    total = []
    for j in data_sewa:
        print(f'{j[2]} : {j[4]} hari x {j[3]} = {j[5]}')
        total.append(j[5])
    total_harga = sum(total)
    print(f'Total yang harus dibayar penyewa = {total_harga}')

    while True:
        uang = int(input('\nMasukkan Jumlah Uang Penyewa: '))
        selisih = abs(uang - total_harga)
        if uang < total_harga:
            print('Uang penyewa kurang, minta lagi')
            continue
        elif uang > total_harga:
            print(f'Uang penyewa kembali sebesar {selisih:.0f}')
            break
        else:
            print('Tidak ada kembalian')
            break

def pengembalian(list_penyewa): 
    lihat_report(list_penyewa)
    baris_kembali = int(input('Masukkan pilihan mobil yang ingin dikembalikan: '))
    if baris_kembali not in range(len(list_penyewa)+1):
        print('Tidak ada data pada mobil tersebut,\nPengembalian gagal')
        pengembalian(list_penyewa)
    else:
        plat_penyewa = list_penyewa[baris_kembali-1][1]
        for i in range(len(data_rental)):
            if data_rental[i]['NoPol'] == plat_penyewa:
                status = 'Available'
                cek = input('Apakah penyewa mengembalikan mobil rental? (Y/N) ').capitalize()
                if cek == 'Y':
                    data_rental[i]['Status'] = status
                    del list_penyewa[baris_kembali-1]
                    daftar_mobil()
                    continue
                else:
                    print('Mobil tidak jadi dikembalikan')
                    break  
    if list_penyewa == []:
        print('\nSemua mobil rental sudah dikembalikan')

#Codingan Utama 
while True:
    list_menu()
    menu_utama = int(input ('Masukkan Pilihan Anda: \n'))
    if menu_utama == 1:
        menu1()    
    elif menu_utama == 2:
        menu2()
    elif menu_utama == 3:
        menu3()
    elif menu_utama == 4:
        menu4()
    elif menu_utama ==5:
        menu5()
    elif menu_utama == 9:
        keluar = input('\n Apakah Anda yakin ingin keluar? (Y/N) ').capitalize()
        if keluar == 'Y':
            print('Thankyou and Have a Nice Day')
            break
        else:
            continue
    else:
        print('Menu yang dimasukkan tidak tersedia')
        continue                                                                                                                                                                     