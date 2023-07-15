#Pembuka Program
def menuUtama():
    print("**********Selamat Datang di Program kelompok 1**********")
    print("*****************Selamat menggunakannya*****************")
    print(" ")
    print("program apa yang ingin anda pilih?")
    print("1. Prichillia Poluan")
    print("2. Isabelita Ombuh")
    print("3. Roma Mantiri")
    print("4. Albani Boutje")
    print("5. Stefandy Momongan")
    print("Masukkan 'No' apabila ingin keluar dari program")

#Pemilihan Program
#Prichillia Poluan
def program_prichillia():
    print ("<Layar input>")
    print ("===========================================================")
    print ("                     Toko Buku Grameaku                    ")
    print ("                         Jln. Jalan                        ")
    print ("===========================================================")
    print("\n")

    print ("|List Buku|")
    print ("===========================================================")

    print ("  ~~ KODE ~~  |   ~~ JUDUL BUKU ~~    |   ~~~ HARGA ~~~   |")
    print ("     DP       |   Dasar Pemograman    |   Rp. 150.000     |")
    print ("     VB       |   Visual Basic        |   Rp. 160.000     |")
    print ("     WP       |   Web Programming     |   Rp. 200.000     |")

    print ("===========================================================")
    print("\n")

    def mengulang():
        kode_buku=[]
        jumlah_beli=[]
        judul_buku=[]
        harga=[]
        jumlah=[]
        banyak_jenis=int(input("banyak jenis :"))
        i=0

        for i in range(banyak_jenis):
            print("beli ke-", i+1)
            kode_buku.append(input("Masukan kode buku [DP/VB/WP] :"))
            jumlah_beli.append(int(input("Masukan jumlah beli :")))

            if kode_buku[i]=="DP":
                judul_buku.append("Dasar Pemograman ")
                harga.append("150000")
                jumlah.append(jumlah_beli[i]*int("150000"))
            elif kode_buku[i]=="VB":
                judul_buku.append("Visual Basic     ")
                harga.append("160000")
                jumlah.append(jumlah_beli[i]*int("160000"))
            elif kode_buku[i]=="WP":
                judul_buku.append("Web Programing   ")
                harga.append("200000")
                jumlah.append(jumlah_beli[i]*int("200000"))
            else :
                judul_buku.append("kode buku salah")
                harga.append("0")
                jumlah.append(jumlah_beli[i]*int("0"))

        print ("<Layar output>")

        print ("===========================================================")
        print ("               Toko Buku Grameaku                 ")
        print ("                Jln. Jalan                   ")
        print ("===========================================================")

        print ("|NO.    Judul Buku       Banyak Beli  Harga  Total Harga  |")
        print ("===========================================================")

        jumlah_bayar=0
        a=0
        while a<banyak_jenis:
            jumlah_bayar=jumlah_bayar+jumlah[a]
            print(" %i   %s     %s       %i       %i" % (a+1, judul_buku[a], harga[a], jumlah_beli[a], jumlah[a]))
            a=a + 1

            print ("===========================================================")

        disc=jumlah_bayar*0.05
        total_bayar=jumlah_bayar-disc

        print("                  Jumlah Bayar    : Rp.",jumlah_bayar)
        print("                  Diskon 5%       : Rp.",disc)
        print("                  Total Bayar     : Rp.",total_bayar)
        uang_bayar=int(input("                  Uang bayar      : Rp."))
        print("                  Kembalian       : Rp.",uang_bayar-total_bayar)
    mengulang()
    def exit() :
        print("=======+ BACALAH BUKU AGAR PENGETAHUAN MU MENINGKAT +=======")
        print("==============+ BUKU ADALAH JENDELA DUNIA +=================")
        print("======================= TERIMA KASIH =======================")
    exit()

    def rerun():
        print("Mau Pesan Lagi ?")
        print("1.Ya")
        print("2.Tidak")
        klik = int(input("Masukan [1 atau 2] :"))
        if klik == 1:
            mengulang()
        elif klik == 2 :
            exit()
        else :
            print("Masukan Hanya Kode 1 Atau 2 !!")
            rerun()
    rerun()

    
#Program Roma Mantiri
def program_roma():
    def konversi (kvs:int) -> int:
            print ("1. Konversi meter ke kilometer")
            print ("2. Konversi detik ke jam")
            kvs = input("Masukkan perhitungan konversi (sesuai angka): ")
            if kvs == "1":
                a = 1000 #1 kilometer = 1000 meter
                nilai = float(input("Masukkan nilai meter: "))
                print ("Jika dikonversi ke kilometer = ", (nilai/a),"km")
            elif kvs == "2":
                b = 3600 #1 jam = 3600 detik
                nilai = float(input("Masukkan nilai detik: "))
                print ("Jika dikonversi ke detik = ", (nilai/b),"jam")
            else:
                print ("Maaf, pilihan anda tidak tersedia. Anda kembali ke menu utama")
    print ()
    def menghitung_kecepatan (s, t:int)-> int: #masukkan perintah '1' untuk memanggil program ini
        print ("Jadi, Kecepatannya adalah",(s/t),"km/jam") #m/s adalah satuan kecepatan
        print ()
    def jika_s_tidak_diketahui (t, v:int)-> int: #masukkan perintah '2' untuk memanggil program ini
        print ("Jadi, Jarak yang ditempuh adalah", (t*v),"kilometer")
        print ()
    def jika_t_tidak_diketahui (s, v:int)-> int: #masukkan perintah '3' untuk memanggil program ini
        print ("Jadi, Waktu tempuh adalah", (s/v),"jam")
        print ()
    def konversi_km_per_jam_ke_meter_per_detik(km, jam:int)-> int: #masukkan perintah '4' untuk memanggil program ini
        print ("Jika di konversi ke m/s =", (round((km*1000)/jam)),"m/s")
    print ()

    print ('            Selamat datang di program perhitungan           ')
    print ('                  Kecepatan, jarak, dan waktu               ')
    order = ""
    print ()
    print ("Apakah anda ingin melakukan konversi terlebih dahulu?")
    print ("Y, untuk melakukan konversi")
    print ("N, untuk tidak melakukan konversi dan kembali ke menu utama")
    pilihan = input("Y/N: ")
    if pilihan == "Y":
        konversi(kvs=int)
    elif pilihan == "N":
        print ("Terima kasih, silahkan kembali ke menu utama")
        
    print()
    print ('1. Menghitung Kecepatan')
    print ('2. Menghitung Jarak')
    print ('3. Menghitung Waktu')
    print ('4. Konversi km/jam ke m/s')
    while order != "keluar":
        order = input('Masukkan perhitungan (sesuai angka) yang anda mau (atau ketik "keluar" jika ingin keluar dari program) : ')
        if order == "keluar":
            print ("---------------------------------------------------")
            print ("Terima Kasih")
            print ("anda keluar dari program")
        elif order == "1": #menghitung kecepatan
            s = float(input("Masukkan nilai jarak : ")) #s adalah jarak
            t = float(input("Masukkan nilai waktu : ")) #t adalah waktu
            menghitung_kecepatan(s, t) 
        elif order == "2": #menghitung jarak
            t = float(input("Masukkan nilai waktu : ")) #t adalah waktu
            v = float(input("Masukkan nilai kecepatan : ")) #v adalah kecepatan
            jika_s_tidak_diketahui(t, v)
        elif order == "3": #menghitung waktu
            s = float(input("Masukkan nilai jarak : ")) #s adalah jarak
            v = float(input("Masukkan nilai kecepatan : ")) #v adalah kecepatan
            jika_t_tidak_diketahui(s, v)
        elif order == "4": #konversi 
            km = float(input("Masukkan nilai yang ingin di konversi : "))
            jam = 3600
            konversi_km_per_jam_ke_meter_per_detik(km, jam)
        else:
            print ("Contoh program tidak tersedia")
            print ("Mohon masukkan program yang tersedia")



#Program Albani Boutje
def program_albani():
    print("---------------------------")
    print("Menghitung Nilai Rata-rata")
    print("---------------------------")

    def IdentitasGuru():
        Nama_Pengguna = input("Nama : ")
        NIP_Pengguna = int(input("NIP : "))
        Umur_Pengguna = int(input("Umur : "))
        if Umur_Pengguna <= 18:
            print("Masih dibawha umur")
        else:
            print("selamat bertugas")
        print("Hallo Petugas : ", Nama_Pengguna)
        print("NIP anda : ", NIP_Pengguna)
        print("Petugas Berumur : ", Umur_Pengguna)

    IdentitasGuru()

    print("========================")
    print("Pengaturan untuk sistem ")
    print("========================")
    print("1. Silakan mengisi data yang ingin dumasukkan")
    print("2. Apabila selesai menggunakan silakan ketik 'ya'")
    print("3. Mengisi nilai gunakan koma.")
    print("4. Masukkan NIM mahasiswa yang dituju")
    print("5. Selamat Mengerjakan")
    print("------------------------")

    def DataMahasiswa():
        D = {}
        while True:
            NIMpeserta = input("Masukkan NIM murid : ")
            Nilai = input("Masukkan Nilai : ")
            Exit = input("Ketik 'YA' apabila ingin berhenti? ")
            if NIMpeserta in D:
                print(NIMpeserta, "Sudah dimasukkan")
            else:
                D[NIMpeserta] = Nilai.split(",")
            if Exit.upper() == "YA":
                return D

    Mahasiswa = DataMahasiswa()
    Mahasiswa

    def NilaiRata2(D):
        Rata2 = {}
        for x in D:
            L = D[x]
            s = 0
            for nilai in L:
                s += float(nilai)
                Rata2[x] = s/len(L)
        return Rata2

    RataN = NilaiRata2(Mahasiswa)
    RataN

    for x in RataN:
        print("Mahasiswa: ", x," Mendapatkan rata rata: ", round(RataN[x]))

#Program Isabelita Ombuh
def program_isabelita():
    user_id = 0
    loop = "n"
    user =  [
                {   
                    "id":"0101",
                    "no_rekening":"1234567890",
                    "username":"Dika",
                    "pin":"1212",
                    "saldo":10000
                },
                {   
                    "id":"0202",
                    "no_rekening":"0987654321",
                    "username":"Mahar",
                    "pin":"2121",
                    "saldo":25000000
                }
            ]
    status_login = False
    pakai_atm = "y"
    
    def cek_login(p):
        for us in user:
            if us['pin'] == p:
                return us
        return False       
        
    def cek_user(id):
        for i in range(len(user)):
            if user[i]['id'] == str(id):
                return int(i)
        return -1
    
    def cek_rekening(no):
        for i in range(len(user)):
            if str(user[i]['no_rekening']) == str(no):
                return int(i)
        return -1
    
    def tranfer_uang(uang,no_rekening):
        index1 = cek_user(user_id)
        index2 = cek_rekening(no_rekening)
        if index1 >= 0:
            if user[index1]['saldo'] >= int(uang):
                user[index1]['saldo'] =user[index1]['saldo'] - int(uang)
                user[index2]['saldo'] =user[index2]['saldo'] + int(uang)
                print("Anda berhasil mentransfer uang Rp."+str(uang)+" ke Rekening "+no_rekening)
                print("sisa saldo anda adalah Rp.",user[index1]['saldo'])
            else:
                print("Ops saldo anda tidak cukup")
                
    def ambil_uang(uang):
        index1 = cek_user(user_id)
        if index1 >= 0:
            if user[index1]['saldo'] >= int(uang):
                user[index1]['saldo'] =user[index1]['saldo'] - int(uang) 
                print("Anda berhasil menarik uang Rp."+str(uang))
                print("sisa saldo anda adalah Rp.",user[index1]['saldo'])
            else:
                print("Ops saldo anda tidak cukup")
    
    
    while pakai_atm == "y":
        while status_login == False:
            print("SELAMAT DATANG DI ATM BANK UNSRAT")
            print("Silahkan masukan pin anda")
            pin = input("Masukan PIN : ")
        
            cl = cek_login(pin)
            if cl != False:
                print("selamat datang" +cl['username'])
                user_id = cl['id']
                status_login = True
                loop = "y"
            else:
                print("")
                print("Ops PIN anda salah")
                print("")
                print("")
        
        while loop == "y" and status_login == True:
            u = user[cek_user(user_id)]
            print("SELAMAT DATANG DI ATM BANK UNSRAT")
            print("1.Cek Saldo")
            print("2.Transfer Uang")
            print("3.Tarik Uang")
            print("4.Logout")
            print("5.Keluar ATM")
            a = int(input("Silahkan pilih menu : "))
            if a == 1:
                print("")
                print("Sisa Saldo anda adalah Rp.",u['saldo'])
                print("")
                print("")
                loop = "n"
            elif a == 2:
                print("Untuk Mentransfer Uang Silahkan Masukan No Rekening Tujuan")
                no_rek = input("Masukan No Rekening Tujuan : ")
                cnk = cek_rekening(no_rek)
                
                if cnk >= 0:
                    print("Nomor rekening ditemukan,silahkan masukan nominal yang yang akan di transfer")
                    nominal = input("Nominal Yang Akan Di Transfer : ")
                    tranfer_uang(nominal,no_rek)
                    print("")
                    loop = "n"
                else:
                    print("")
                    print("Nomor Rekening Tujuan Tidak ditemukan atau tidak terdaftar")
                    print("")
                    loop = "n"
                    
            elif a == 3:
                nominal = input("Nominal Yang Akan Di Tarik : ")
                ambil_uang(nominal)
                print("")
                loop = "n"
            elif a == 4:
                status_login = False
                
            elif a == 5:
                status_login = False
                loop = "n"
                pakai_atm = "n"
            else:
                print("pilihan tidak tersedia")
            if status_login == True:
                
                input("kembali Ke menu (Enter) ")
                print("")
                loop = "y"

#Program Stefandy Momongan
def program_stefandy():
    def menu():
        print ("========================================= MENU UTAMA ===========================================")
        print (" ")
        print ("Di WONDERFUL SULUT atau yang kita kenal dengan Provinsi Sulawesi Utara, terdapat banyak KOTA dan KABUPATEN,")
        print ("  Sekarang Kamu ingin mengunjungi KOTA atau KABUPATEN yang ada di Sulawesi Utara ?  ")
        print (" ")
        print ("1 Untuk mengunjungi KOTA")
        print ("2 Untuk mengunjungi KABUPATEN")
        print (" ")      
    
    print ("------------------------------------------------")
    print ("======  Kamu Mau Masuk WONDERFUL SULUT ?  ======")
    print ("======  Isikan Data Diri Kamu Dulu Ya !!  ======")
    print ("------------------------------------------------")
    print (" ")
    print ("Tuliskan Nama Kamu :")
    nama = input()
    print (" ")
    print ("1000-1")
    print ("Berapakah Hasil dari Pengurangan Tersebut ?")
    print ("Jawaban Kamu :")
    sandi = input()
    if sandi == ("999"):
        print (" ")
        print ("Nice! Jawaban Kamu Benar")
        print (" ")
        print ("Selamat Datang di Program WONDERFUL SULUT", nama)
        print (" ")
        menu()
    else:
        print ("Sayang sekali, jawaban kamu salah!")
        print ("Kamu dilarang masuk:')")
        print ("BYE !!")
        print (" ")
        print (" ")
        print (" ")
        print (" ")
        exit()

    def kota():
        print (" ")
        print ("----Daftar pilihan KOTA yang dapat kamu kunjungi di Sulawesi Utara----")
        print ("\n1.Bitung \n2.Kotamobagu \n3.Manado \n4.Tomohon")
    
    def kabupaten():
        print (" ")
        print ("---Daftar pilihan KABUPATEN yang dapat kamu kunjungi di Sulawesi Utara---")
        print ("\n1.Bolaang Mongondow \n2.Bolaang Mongondow Selatan \n3.Bolaang Mongondow Timur \n4.Bolaang Mongondow Utara \n5.Kepulauan Sangihe \n6.Kepulauan Siau Tagulandang Biaro \n7.Kepulauan Talaud \n8.Minahasa \n9.Minahasa Selatan \n10.Minahasa Tenggara \n11.Minahasa Utara")
    
    def out():
        print ("Apakah kamu sudah selesai dan ingin keluar dari program ?")
        print ("Y untuk Menutup Program")
        print ("N untuk Kembali ke Menu Utama")
        print (" ")
        out = input("Y/N = ")
        if out.upper() == "Y":
            exit()
        elif out.upper() == "N":
            menu()
        else :
            print ("Salah input bos, Program akan segera tertutup:')")
            print (" ")
            print (" ")
            print (" ")
            print (" ")
            print (" ")
            print (" ")
            exit()
        
    def keluar():
        print ("Tidak ada di pilihan bos, coba lagi dari awal? [Y/N]")
        print ("Y = Menu Utama")
        print ("N = Tutup Program")
        coba = input()
        if coba.upper() == "N":
            exit()
        elif coba.upper() == "Y":
            menu()
        else :
            print ("Salah input bos, Program akan segera tertutup")
            print (" ")
            print (" ")
            print (" ")
            print (" ")
            print (" ")
            print (" ")
            print (" ")
            print (" ")
            exit()
        
    #Objek Wisata
    Bitung = ("\n=> Pantai Batu Putih (Kec.Ranowulu) \n=> Pantai Batu Angus (Kec.Aertembaga) \n=> Hutan Mangrove Lirang (Kec.Lembeh Utara) \n=> Pantai Tanjung Merah (Kec.Matuari) \n=> Selat Lembeh (Kec.Lembeh Selatan) \n=> Taman Nasional Tangkoko (Kec.Aertembaga) \n=> Taman Margasatwa Tandurusa (Kec.Aertembaga) \n=> Monumen Trikora Mandala Sakti (Kec.Lembeh Selatan) \n=> Gunung Dua Saudara (Kec.Madidir) ")
    Kotamobagu = ("\n=> Air Terjun Mongkonai (Kec.Kotamobagu Barat) \n=> Taman Nasional Bogani Nani Wartabone (Kec.Kotamobagu Barat) \n=> Air Terjun Molipungan (Kec.Kotamobagu Timur) \n=> Rumah Adat Bobakidan (Kec.Kotamabagu Barat) \n=> Hutan Kawasan Kota Bonawang (Kec.Kotamobagu Barat) \n=> Pemandian Air Panas Banyu anget (Kec.Kotamobagu Selatan) ")
    Manado = ("\n=> Taman Nasional Bunaken \n=> Pulau Siladen (Kec.Malalayang) \n=> Pantai Tatiala (Kec.Bunaken) \n=> Pulau Manado Tua \n=> Pulau Lihaga \n=> Citraland Waterpark Manado \n=> God Bless Park (Kec.Sario) \n=> Yesus Memberkati Statue (Kec.Malalayang) \n=> Monumen HV Worang (Kec.Wenang) \n=> Museum Negeri Sulawesi Utara (Kec.Wenang) \n=> Monumen Boboca \n=> Monumen Lilin (Kec.Wenang) \n=> Kampung Cina \n=> Rumah Alam Manado (Kec.Mapanget) ")
    Tomohon = ("\n=> Puncak Temboan (Kec.Tomohon Timur) \n=> Valentine Hils (Kec.Tomohon Barat) \n=> We'lu Cafe & Resto (Kec.Tomohon Barat) \n=> Danau Lonow (Kec.Tomohon Selatan) \n=> Bukit Doa Mahawu (Kec.Tomohon Utara) \n=> Pagoya Ekayana (Kec.Tomohon Utara) \n=> Amphithearter Woloan (Kec.Tomohon Barat) \n=> Alfa Omega Tower (Kec.Tomohon Timur) \n=> Puncak Kai'Santi (Kec.Tomohon Barat) \n=> Gunung Lokon ")
    Bolaang_Mongondow = ("\n=> Air Terju Lolan (Kec.Bolaang Timur) \n=> Patai Losari (Kec.Lolak) \n=> Pemandian Air Panas Bakan (Kec.Lolayan) \n=> Tanjung Ompu (Kec.Lolak) \n=> Pantai Bungin (Kec.Lolak) \n=> Pulau Tiga (Kec.Sangtombolang) \n=> Pulau Molosing (Kec.Lolak) \n=> Pulau Babo Moonow (Kec.Sangtombolang) ")
    Bolaang_Mongondow_Selatan = ("\n=> Pantai Tanjung Panango (Kec.Bolaang Uki) \n=> Pantai Salongo (Kec.Bolaang Uki) \n=> Pelabuhan Alam Dodepo (Kec.Bolaang Uki) \n=> Goa Paniki Lion (Kec.Bolaang Uki) \n=> Air Terjun Buniha (Kec.Bolaang Uki) \n=> Pantai Dami (Kec.Pinolosian) \n=> Pantai Torosik (Kec.Pinolosian) \n=> Penangkaran Burung Maleo (Kec.Pinolosian) ")
    Bolaang_Mongondow_Timur = ("\n=> Pantai Cimoki (Kec.Nuangan) \n=> Pulau Nenas (Kec.Kotabunan) \n=> Tanjung Silar dan Pantai Patokan (Kec.Motongkad) \n=> Air Terjun Dodandian (Kec.Nuangan) \n=> Danau Mooat (Kec.Modayag) \n=> Wisata River View Atoga (Kec.Motongkad) \n=> Tanjung Layar Pulau Kumeke (Kec.Kotabunan) ")
    Bolaang_Mongondow_Utara = ("\n=> Pantai Tanjung Buaya (Kec.Bintauna) \n=> Air terjun Batunangan (Kec.Sangkub) \n=> Tanjung Labuo (Kec.Bolang Itang Timur) \n=> Vatu Pinagut Beach (Kec.Kaidipang) \n=> Air Terjun Permai (Kec.Kaidipang) \n=> Objek Wisata Air Belanda (Kec.Kaidipang) \n=> Pemandian Air Panas Pangi (Kec.Sangtombolang) ")
    Kepulauan_Sangihe = ("\n=> Air Terjun Nguralawo (Kec.Tamako) \n=> Pantai Embuhanga (Kec.Tabukan Utara) \n=> Maselihe (Kec.Manganitu) \n=> Air TerjunSura Kakewang (Kec.Kendahe) \n=> Boulevard Tahuna (Kec.Tahuna) \n=> Pulau Mendaku (Kec.Manganitu Selatan) \n=> Puncak Pusunge (Kec.Tabukan Utara) \n=> Gunung Api Bawah Laut Mahangetang (Kec.Tatoareng) \n=> Gunung Api Bawah Laut Kawio (Kec.Nusa Tabukan) \n=> Pantai Pananuareng (Kec.Tabukan Tengah) ")
    Kepulauan_Siau_Tagulandang_Biaro = ("\n=> Monumen Yesus Memberkati (Kec.Siau Timur) \n=> Pulau Makelehi (Kec.Siau Barat) \n=> Danau Cinta Makalehi (Kec.Siau Barat) \n=> Puncak Maleheki (Kec.Siau Barat) \n=> Pemandian Air Panas Temboko (Kec.Siau Barat) \n=> Pulau Mahoro ")
    Kepulauan_Talaud = ("\n=> Pulau Kabaruan (Kec.Damau) \n=> Gua Batu Kapal (Kec.Melonguane) \n=> Air Terjun Ampadoap (Kec.Beo) \n=> Goa Weta (Kec.Talaud) \n=> Pantai Karakelong (Kec.Kalongan) \n=> Pantai Lobbo (Kec.Beo Utara) \n=> Danau Lotah Talaud (Kec.Moronge) \n=> Pulau Sara (Kec.Moronge) \n=> Desa Adat Bannada (Kec.Gemeh) ")
    Minahasa = ("\n=> Bukit Kasih (Kec.Kawangkoan Barat) \n=> Benteng Moraya (Kec.Tondano Barat) \n=> Danau Tondano (Kec.Tondano Selatan) \n=> Arung Jeram Timbukar (Kec.Sonder) \n=> Desa Pulutan (Kec.Remboken) \n=> Museum Pinawetengan (Kec.Tompaso Barat) \n=> Pantai Mahembang (Kec.Kakas) \n=> Gunung Empung (Kec.Mandolang) ")
    Minahasa_Selatan =  ("\n=> Spot Diving Pantai Blongko (Kec.Sinonsayang) \n=> Taman Nasional Bunaken Bagian Selatan (Kec.Tatapaan) \n=> Gunung Payung (Kec.Ranoyapo) \n=> Pantai Moinit Tewasen (Kec.Amurang Barat) \n=> Pantai Teletabis (Kec.Sinonsayang) \n=> Batu Dinding Amurang (Kec.Amurang) \n=> Pantai Alar Minahasa Selatan (Kec.Amurang Timur) \n=> Air Terjun Tumpaan Park Amurang (Kec.Tumpaan) \n=> Agrowosata Modoinding (Kec.Modoinding) ")
    Minahasa_Tenggara = ("\n=> Perahu Bagan (Kec.Ratatotok) \n=> Aer Konde Ratahan (Kec.Ratahan) \n=> Pantai Lakban (Kec.Ratatotok) \n=> Air Terjun Poniki (Kec.Pasan) \n=> Danau Lumpias dan Kolam Kinawa (Kec.Ratahan) \n=> Pantai Bentenan (Kec.Pusomaen) \n=> Batu Pasak Wanua (Kec.Ratahan) ")

    while True:
        pilih = input("Masukan Angka pilihan Kamu, kemudian tekan enter : ")
        if pilih == "1":
            kota()
            print ("\n")
            print ("KOTA mana yang ingin kamu kunjungi ?")
            print ("Masukkan angka 1 sampai 4 sesuai keinginan kamu ya!")
            print (" ")
            pilih = input("KOTA Pilihanku : ")
            if pilih == "1":
                print (" ")
                print ("**************************** BITUNG ***************************")
                print ("Berikut tempat wisata paling hits yang dapat kamu kunjungi di Kota Bitung :")
                print (Bitung)
                print (" ")
                print ("SELAMAT BERLIBUR DI KOTA BITUNG YA!")
                print ("\n")
                out()
            elif pilih == "2":
                print (" ")
                print ("**************************** KOTAMOBAGU **************************")
                print ("Berikut tempat wisata yang paling hits dapat kamu kunjungi di Kota Kotamobagu :")
                print (Kotamobagu)
                print (" ")
                print ("SELAMAT BERLIBUR DI KOTA KOTAMOBAGU YA!")
                print ("\n")
                out()
            elif pilih == "3":
                print (" ")
                print ("**************************** MANADO ***************************")
                print ("Berikut tempat wisata yang paling hits dapat kamu kunjungi di Kota Manado :")
                print (Manado)
                print (" ")
                print ("SELAMAT BERLIBUR DI KOTA BEKASI YA")
                print ("\n")
                out()
            elif pilih == "4":
                print (" ")
                print ("**************************** TOMOHON ***************************")
                print ("Berikut tempat wisata paling hits yang dapat kamu kunjungi di Kota Tomohon :")
                print (Tomohon)
                print (" ")
                print ("SELAMAT BERLIBUR DI KOTA MANADO YA")
                print ("\n")
                out()
            elif pilih > "4":
                keluar()
            
        elif pilih == "2":
            kabupaten()
            print ("\n")
            print ("KABUPATEN mana yang ingin kamu kunjungi ?")
            print ("Masukkan angka 1 sampai 11 sesuai keinginan kamu ya!")
            print (" ")
            pilih = input("KABUPATEN Pilihanku : ")
            if pilih == "1":
                print (" ")
                print ("***************************** BOLAANG MONGONDOW *******************************")
                print ("Berikut tempat wisata paling hits yang dapat kamu kunjungi di Kabupaten Bolaang Mongondow :")
                print (Bolaang_Mongondow)
                print (" ")
                print ("SELAMAT BERLIBUR DI KABUPATEN BOLAANG MONGONDOW YA!")
                print ("\n")
                out()
            elif pilih == "2":
                print (" ")
                print ("******************************BOLAANG MONGONDOW SELATAN********************************")
                print ("Berikut tempat wisata paling hits yang dapat kamu kunjungi di Kabupaten Bolaang Mongondow Selatan :")
                print (Bolaang_Mongondow_Selatan)
                print (" ")
                print ("SELAMAT BERLIBUR DI KABUPATEN BOLAANG MONGONDOW SELATAN YA!")
                print ("\n")
                out()
            elif pilih == "3":
                print (" ")
                print ("***************************** BOLAANG MONGONDOW TIMUR *******************************")
                print ("Berikut tempat wisata paling hits yang dapat kamu kunjungi di Kabupaten Bolaang Mongondow Timur :")
                print (Bolaang_Mongondow_Timur)
                print (" ")
                print ("SELAMAT BERLIBUR DI KABUPATEN BOLAANG MONGONDOW TIMUR YA!")
                print ("\n")
                out()
            elif pilih == "4":
                print (" ")
                print ("***************************** BOLAANG MONGONDOW UTARA *******************************")
                print ("Berikut tempat wisata paling hits yang dapat kamu kunjungi di Kabupaten Bolaang Mongondow Utara :")
                print (Bolaang_Mongondow_Utara)
                print (" ")
                print ("SELAMAT BERLIBUR DI KABUPATEN BOLAANG MONGONDOW UTARA YA!")
                print ("\n")
                out()
            elif pilih == "5":
                print (" ")
                print ("***************************** KEPULAUAN SANGIHE *******************************")
                print ("Berikut tempat wisata paling hits yang dapat kamu kunjungi di Kabupaten Kepulauan Sangihe :")
                print (Kepulauan_Sangihe)
                print (" ")
                print ("SELAMAT BERLIBUR DI KABUPATEN KEPULAUAN SANGIHE YA!")
                print ("\n")
                out()
            elif pilih == "6":
                print (" ")
                print ("***************************** KEPULAUAN SIAU TAGULANDANG BIARO *******************************")
                print ("Berikut tempat wisata paling hits yang dapat kamu kunjungi di Kabupaten Kepulauan Siau Tagulandang Biaro :")
                print (Kepulauan_Siau_Tagulandang_Biaro)
                print (" ")
                print ("SELAMAT BERLIBUR DI KABUPATEN KEPULAUAN SIAU TAGULANDANG BIARO YA!")
                print ("\n")
                out()
            elif pilih == "7":
                print (" ")
                print ("******************************KEPULAUAN TALAUD********************************")
                print ("Berikut tempat wisata paling hits yang dapat kamu kunjungi di Kabupaten Kepulauan Talaud :")
                print (Kepulauan_Talaud)
                print (" ")
                print ("SELAMAT BERLIBUR DI KABUPATEN KEPULAUAN TALAUD YA!")
                print ("\n")
                out()
            elif pilih == "8":
                print (" ")
                print ("***************************** MINAHASA *******************************")
                print ("Berikut tempat wisata paling hits yang dapat kamu kunjungi di Kabupaten Minahasa :")
                print (Minahasa)
                print (" ")
                print ("SELAMAT BERLIBUR DI KABUPATEN MINAHASA YA!")
                print ("\n")
                out()
            elif pilih == "9":
                print (" ")
                print ("***************************** MINAHASA SELATAN *******************************")
                print ("Berikut tempat wisata paling hits yang dapat kamu kunjungi di Kabupaten Minahasa Selatan :")
                print (Minahasa_Selatan)
                print (" ")
                print ("SELAMAT BERLIBUR DI KABUPATEN MINAHASA SELATAN YA!")
                print ("\n")
                out()
            elif pilih == "10":
                print (" ")
                print ("***************************** MINAHASA TENGGARA *******************************")
                print ("Berikut tempat wisata paling hits yang dapat kamu kunjungi di Kabupaten Minahasa Tenggara :")
                print (Minahasa_Tenggara)
                print (" ")
                print ("SELAMAT BERLIBUR DI KABUPATEN MINAHASA TENGGARA YA!")
                print ("\n")
                out()
            elif pilih == "11":
                print (" ")
                print ("***************************** MINAHASA UTARA *******************************")
                print ("Berikut tempat wisata paling hits yang dapat kamu kunjungi di Kabupaten Minahasa Utara :")
                print ("Minahasa_Utara")
                print (" ")
                print ("SELAMAT BERLIBUR DI KABUPATEN MINAHASA UTARA YA!")
                print ("\n")
                out()
        
            elif pilih > "11":
                keluar()
    
    
        else:
            print (" ")
            print ("Maaf bos, pilihan yang dimasukkan tidak terdaftar")
            print ("Ingin coba Lagi [Y/N] ? ")
            print ("Y = Kembali ke Menu Utama")
            print ("N = Tutup Program")
            coba = input()
            if coba.upper() == "Y":
                menu()
            elif coba.upper() == "N":
                exit()
            else:
                print ("Input Salah bos, Program akan segera tertutup")
                print (" ")
                print (" ")
                print (" ")
                print (" ")
                exit()
                
true = True
while true:
    menuUtama()
    Memilih = input("Masukkan Nomor yang anda ingin masukkan? ")
    if Memilih == "1":
        print(program_prichillia())
    elif Memilih == "2":
        print(program_isabelita())
    elif Memilih == "3":
        print(program_roma())
    elif Memilih == "4":
        print(program_albani())
    elif Memilih == "5":
        print(program_stefandy())
    else:
        print("Terima Kasih telah menggunakan program kami")
        break
4
