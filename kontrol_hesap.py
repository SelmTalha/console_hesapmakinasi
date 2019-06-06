
print("----Hesap Makinası Örneği----")
def topla(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b
def kontrol():
    deger = None
    secim=input("Programdan çıkmak istiyor musunuz ? Evet --> Q'ya basınız.")
    if secim == 'q' or secim == 'Q':
        print("Program sonlandırıldı !")
        deger = True
    else:
        deger = False
    return deger

while True:
    try:
        secim=int(input("1-Toplama İşlemi\n2-Çıkarma İşlemi\n3-Çarpma İşlemi\n4-Bölme İşlemi\nSeçiminiz : "))

        while (secim<1 or secim>4):
            secim =int(input("1-Toplama İşlemi\n2-Çıkarma İşlemi\n3-Çarpma İşlemi\n4-Bölme İşlemi\n"))
        if secim==1:
            isim="Toplama İşlemi Sonucu:"
            sayi1=float(input("Birinci sayiyi giriniz:"))
            sayi2=float(input("İkinci sayiyi giriniz:"))
            sonuc=topla(sayi1,sayi2)
        elif secim==2:
            isim="Çıkarma İşlemi Sonucu:"
            sayi1=float(input("Birinci sayiyi giriniz:"))
            sayi2=float(input("İkinci sayiyi giriniz:"))
            sonuc=cikarma(sayi1,sayi2)
        elif secim==3:
            isim="Çarpma İşlemi Sonucu:"
            sayi1=float(input("Birinci sayiyi giriniz:"))
            sayi2=float(input("İkinci sayiyi giriniz:"))
            sonuc=carpma(sayi1,sayi2)
        elif secim==4:
            isim="Bölme İşlemi Sonucu:"
            sayi1=float(input("Birinci sayiyi giriniz:"))
            sayi2=float(input("İkinci sayiyi giriniz:"))
            sonuc=bolme(sayi1,sayi2)
        print("{} {}".format(isim,sonuc))
        if kontrol():
            break
    except ValueError:
        print("Girilen değer hatalı ! Program yeniden çalıştırılıyor..")
