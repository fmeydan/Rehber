sozluk = dict()


while True:

    print("MENÜ")
    print("İşlem seçin")
    print("1- Ekle")
    print("2- Sil")
    print("3- Listele")
    print("4- Guncelle")
    print("5- Çıkış")
    secim = input("Seçim yapınız: ")
    if secim == "5":
        print("Çıkış yapıldı")
        break
    elif secim == "1":
        ad = input("Ad giriniz: ")
        soyad = input("Soyad giriniz:")
        while True:
            try:
                tc = int(input("Tc giriniz: "))
                break
            except:
                print("Sayısasal bir değer girin")
        dahili = input("Dahili giriniz:")

        if not sozluk:
            id = 1
        else:
            id = max(sozluk.keys()) + 1

        sozluk[id] = {
            "Ad": ad,
            "Soyad": soyad,
            "TC": tc,
            "Dahili": dahili
        }
        print("Kişi eklendi!")
        print(sozluk)

    elif secim == "2":
        while True:
            try:
                silinecek = int(input("TC girin"))
                break
            except:
                print("Sayısal değer girin")


        i=1
        while i <= len(sozluk):
            if sozluk[i]['TC'] == silinecek:
                sozluk.pop(i)
                print("Kişi silindi")
                break
            else:
                print("Aradığınız TC kayıtlı değil")


    elif secim=="3":
        print("AD --- Soyad --- TC --- Dahili" )
        i=1
        while i <= len(sozluk):
            print(sozluk[i]['Ad'],"-",sozluk[i]["Soyad"],"-",sozluk[i]["TC"],"-",sozluk[i]["Dahili"])
            i+=1



    elif secim=="4":
        tc=int(input("Güncellemek istediğiniz TC yi yazınız: "))
        i=1
        while i <=len(sozluk):
            if sozluk[i]["TC"]==tc:
                print("AD --- Soyad --- TC --- Dahili")
                print(sozluk[i]['Ad'], "-", sozluk[i]["Soyad"], "-", sozluk[i]["TC"], "-", sozluk[i]["Dahili"])

                print("Güncellemek istediğiniz seçiniz: ")
                print("1-Ad")
                print("2-Soyad")
                print("3-TC")
                print("4-Dahili")
                secim=input("Seçiminiz: ")
                if secim=="1":
                    ad=input("Ad giriniz: ")
                    sozluk[i]["Ad"]=ad
                elif secim=="2":
                    soyad=input("Soyad giriniz: ")
                    sozluk[i]["Soyad"]=soyad
                elif secim=="3":
                    tc=input("TC giriniz: ")
                    sozluk[i]["TC"]=tc
                elif secim=="4":
                    dahili=input("Dahili giriniz: ")
                    sozluk[i]["Dahili"]=dahili

                print("Güncelleme başarılı.")
                print("AD --- Soyad --- TC --- Dahili")
                print(sozluk[i]['Ad'], "-", sozluk[i]["Soyad"], "-", sozluk[i]["TC"], "-", sozluk[i]["Dahili"])


            else:
                print("Bu TC kayıtlı değil")


            i+=1










