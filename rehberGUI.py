from tkinter import *
import sqlite3
import warnings


def  veritabaniAra(param):
    b = sqlite3.connect("kisilerdb.db")

    if not b:
        print("Bağlantı Hatası")
        exit()
    else:

        i = b.cursor()
        try:
            sqlAra=f"select * from kisi_listesi where tc={param}"
            i.execute(sqlAra)
            data=i.fetchall()
            b.commit()
            return data
        except:
            return False


def ekle(isim,soyisim,tc,dahili):
    b=sqlite3.connect("kisilerdb.db")
    if not b:
        print("Bağlantı Hatası")
        exit()
    else:
        b.row_factory=sqlite3.Row
        i=b.cursor()
        try:
            sql="insert into kisi_listesi (ad,soyad,tc,dahili) values (?,?,?,?)"
            i.execute(sql,(isim,soyisim,tc,dahili))
            b.commit()
            return True
        except:
            return False

def veritabaniGuncelle(id,isim,soyisim,tc,dahili):
    b=sqlite3.connect("kisilerdb.db")
    if not b:
        print("Bağlanalılamadı")
        exit()
    else:
        b.row_factory=sqlite3.Row
        i=b.cursor()
        try:
            sql="""update kisi_listesi set ad = ?, soyad = ?, tc = ?, dahili = ? where ID=?"""
            i.execute(sql,(isim,soyisim,tc,dahili,id))
            b.commit()
            return True
        except:
            warnings.warn("Veritabanı Guncellenemedi",DeprecationWarning)
            return False

def veritabaniSil(id):
    b = sqlite3.connect("kisilerdb.db")
    if not b:
        print("Bağlanalılamadı")
        exit()
    else:

        i = b.cursor()
        try:
            sql = f"DELETE from kisi_listesi where id={id}"
            i.execute(sql)
            b.commit()
            return True
        except:
            warnings.warn("Silme Başarısız", DeprecationWarning)
            return False

def eklePencere():
    p2 = Tk()
    def ekleClick():
        isim=entry_isim.get()
        soyisim=entry_soyisim.get()
        tc=entry_tc.get()
        dahili=entry_dahili.get()
        sonuc=ekle(isim,soyisim,tc,dahili)
        if sonuc==True:
            label_sonuc.config(text="Başarılı",foreground="green")
        else:
            label_sonuc.config(text="Başarısız",foreground="red")


    p2.geometry("500x400+300+200")
    label_isim = Label(p2, text="İsim Giriniz: ")
    label_isim.grid(row=1, column=1)
    entry_isim = Entry(p2)
    entry_isim.grid(row=1, column=2)
    label_soyisim = Label(p2, text="Soyisim Giriniz: ")
    label_soyisim.grid(row=2, column=1)
    entry_soyisim = Entry(p2)
    entry_soyisim.grid(row=2, column=2)
    label_tc = Label(p2, text="TC Giriniz: ")
    label_tc.grid(row=3, column=1)
    entry_tc = Entry(p2)
    entry_tc.grid(row=3, column=2)
    label_dahili = Label(p2, text="Dahili Giriniz: ")
    label_dahili.grid(row=4, column=1)
    entry_dahili = Entry(p2)
    entry_dahili.grid(row=4, column=2)
    buton_ekle=Button(p2,text="Ekle",bg="green",command=ekleClick)
    buton_ekle.grid(row=5,column=1)
    label_sonuc=Label(p2)
    label_sonuc.grid(row=5,column=2)
    mainloop()

def duzenlePencere():
    p3=Tk()

    def ara():
        global dbid

        datas=veritabaniAra(entry_kisiAra.get())

        label_sonuc.config(text="Bu TC numarası kayıt edilmemiş")
        try:
            dbid=datas[0][0]
            ad=datas[0][1]
            soyad=datas[0][2]
            tc=datas[0][3]
            dahili=datas[0][4]
            entry_isim.delete(0,END)
            entry_isim.insert(0,ad)

            entry_soyisim.delete(0, END)
            entry_soyisim.insert(0,soyad)

            entry_tc.delete(0, END)
            entry_tc.insert(0,tc)

            entry_dahili.delete(0, END)
            entry_dahili.insert(0,dahili)
            label_sonuc.config(text="")
        except:
            entry_soyisim.delete(0, END)
            entry_isim.delete(0, END)
            entry_dahili.delete(0, END)
            entry_tc.delete(0, END)
            label_sonuc.config(text="Bu TC kayıtlı değil")

    def guncelleClick():
        isim=entry_isim.get()
        soyisim=entry_soyisim.get()
        tc=entry_tc.get()
        dahili=entry_dahili.get()
        sonuc=veritabaniGuncelle(dbid,isim,soyisim,tc,dahili)
        if sonuc==True:
            label_sonuc.config(text="Güncelleme Başarılı",foreground="green")
        else:
            label_sonuc.config(text="Güncelleme Başarısız", foreground="red")

    p3.geometry("400x200+300+200")
    label_guncellenecek=Label(p3,text="Guncellenecek kişi TC")
    label_guncellenecek.grid(row=6,column=1)
    entry_kisiAra=Entry(p3)
    entry_kisiAra.grid(row=6,column=2)
    btn_ara=Button(p3,text="Ara",bg="pink", command=ara)
    btn_ara.grid(row=7,column=2)


    label_isim = Label(p3, text="İsim Giriniz: ")
    label_isim.grid(row=1, column=1)
    entry_isim = Entry(p3)
    entry_isim.grid(row=1, column=2)
    label_soyisim = Label(p3, text="Soyisim Giriniz: ")
    label_soyisim.grid(row=2, column=1)
    entry_soyisim = Entry(p3,textvariable="")
    entry_soyisim.grid(row=2, column=2)
    label_tc = Label(p3, text="TC Giriniz: ")
    label_tc.grid(row=3, column=1)
    entry_tc = Entry(p3)
    entry_tc.grid(row=3, column=2)
    label_dahili = Label(p3, text="Dahili Giriniz: ")
    label_dahili.grid(row=4, column=1)
    entry_dahili = Entry(p3)
    entry_dahili.grid(row=4, column=2)
    buton_ekle = Button(p3, text="Guncelle", bg="yellow",command=guncelleClick)
    buton_ekle.grid(row=5, column=1)
    label_sonuc=Label(p3)
    label_sonuc.grid(row=5,column=2)

    p3.mainloop()

def silPencere():
    def ara():
        global dbid
        datas = veritabaniAra(entry_silinecektc.get())
        dbid = datas[0][0]
        ad = datas[0][1]
        soyad = datas[0][2]
        tc = datas[0][3]
        dahili = datas[0][4]
        entry_isim.delete(0, END)
        entry_isim.insert(0, ad)

        entry_soyisim.delete(0, END)
        entry_soyisim.insert(0, soyad)

        entry_tc.delete(0, END)
        entry_tc.insert(0, tc)

        entry_dahili.delete(0, END)
        entry_dahili.insert(0, dahili)

        print(dbid)


    def silClick():

        sonuc=veritabaniSil(dbid)

        if sonuc == True:
            label_sonuc.config(text="Silmi Başarılı",foreground="green")
        else:
            label_sonuc.config(text="Silmi Başarısız", foreground="red")

    pSil=Tk()
    pSil.geometry("300x200+300+300")
    label_silinecek = Label(pSil, text="Silinecek kişi TC")
    label_silinecek.grid(row=1, column=1)
    entry_silinecektc=Entry(pSil)
    entry_silinecektc.grid(row=1,column=2)
    buton_ara=Button(pSil,text="Ara",bg="pink",command=ara)
    buton_ara.grid(row=1,column=3)

    label_isim = Label(pSil, text="İsim Giriniz: ")
    label_isim.grid(row=2, column=1)
    entry_isim = Entry(pSil)
    entry_isim.grid(row=2, column=2)
    label_soyisim = Label(pSil, text="Soyisim Giriniz: ")
    label_soyisim.grid(row=3, column=1)
    entry_soyisim = Entry(pSil, textvariable="")
    entry_soyisim.grid(row=3, column=2)
    label_tc = Label(pSil, text="TC Giriniz: ")
    label_tc.grid(row=4, column=1)
    entry_tc = Entry(pSil)
    entry_tc.grid(row=4, column=2)
    label_dahili = Label(pSil, text="Dahili Giriniz: ")
    label_dahili.grid(row=5, column=1)
    entry_dahili = Entry(pSil)
    entry_dahili.grid(row=5, column=2)
    buton_ekle = Button(pSil, text="Sil", bg="red",command=silClick)
    buton_ekle.grid(row=6, column=1)
    label_sonuc = Label(pSil)
    label_sonuc.grid(row=6, column=2)


    pSil.mainloop()


pencere=Tk()
pencere.geometry("500x400+300+200")
label_menu=Label(pencere,text="İşlem Seçiniz")
label_menu.grid(row=0,column=3)
buton_ekle=Button(pencere,text="Kişi Ekle",command=eklePencere)
buton_ekle.grid(row=1,column=1)
buton_sil=Button(pencere,text="Kişi Sil",command=silPencere)
buton_sil.grid(row=1,column=2)
buton_duzenle=Button(pencere,text="Kişi Düzenle",command=duzenlePencere)
buton_duzenle.grid(row=1,column=3)
buton_listele=Button(pencere,text="Kişi Listele")
buton_listele.grid(row=1,column=4)
buton_cikis=Button(pencere,text="Çıkış",bg="red",activebackground="yellow",command=exit)
buton_cikis.grid(row=1,column=5)
pencere.mainloop()




