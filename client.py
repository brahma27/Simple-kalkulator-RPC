import xmlrpc.client

def panggil_bil():
    bil1 = int(input('masukan bilangan 1 : '))
    bil2 = int(input('masukan bilangan 2 : '))
    return bil1,bil2

with xmlrpc.client.ServerProxy("http://192.168.1.5:8008/") as proxy:
    print ("==Operator operasi Matematika Dasar== \n")
    print ("1.Penjumlahan ")
    print ("2.Pengurangan ")
    print ("3.Perkalian ")
    print ("4.Pembagian ")
    print ("5.Modulo ")
    print ("6.Pangkat \n")
    pil = int (input("Pilih nomer : "))

    if pil==1:
        print ("="*30)
        hs1,hs2 = panggil_bil()
        print ('Hasil dari ',hs1,' + ',hs2,' = ',proxy.tambah(hs1,hs2))
    elif pil==2:
        print ("="*30)
        hs1,hs2 = panggil_bil()
        print ('Hasil dari ',hs1,' - ',hs2,' = ',proxy.kurang(hs1,hs2))
    elif pil==3:
        print ("="*30)
        hs1,hs2 = panggil_bil()
        print ('Hasil dari ',hs1,' x ',hs2,' = ',proxy.kali(hs1,hs2))
    elif pil==4:
        print ("="*30)
        hs1,hs2 = panggil_bil()
        print ('Hasil dari ',hs1,' : ',hs2,' = ',proxy.bagi(hs1,hs2))
    elif pil==5:
        print ("="*30)
        hs1,hs2 = panggil_bil()
        print ('Hasil dari ',hs1,' mod ',hs2,' = ',proxy.mod(hs1,hs2))
    elif pil==6:
        print ("="*30)
        hs1,hs2 = panggil_bil()
        print ('Hasil dari ',hs1,'^',hs2,' = ',proxy.pangkat(hs1,hs2))
    print('List method pada server : ',proxy.system.listMethods())
