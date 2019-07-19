password=list(input('Şifre giriniz = '))  #oyun için şifre girisi
print('\n'*15)
tahminSayısı=1
print('''                ________________________________________________________________________________________
                |                                                                                        |
                |                         SAYI TAHMİN-2 OYUNUNA HOŞ GELDİNİZ.                            |
                |                                                                                        |
                |    Rakamları sıfırdan ve biribirinden farklı dört basmaklı bir sayıyı bulmaya          |
                |    çalışacaksınız. Yaptığınız tahminde bir rakamı, basmaktaki yeri ile beraber doğru   |
                |    bilirseniz '+1', basmak yerini yanlış tahmin ettiğiniz her doğru rakam için ise     |
                |    '-1' alacaksınız. Yanlış tahmin edilen  rakamlar  için ise herhangi bir             |
                |    değerlendirme yapılmayacktır.                                                       |
                |                                                                                        |
                |    Örneğin; sayı= 1234, yapilan tahmin = 9231 olsun.                                   |
                |    Burada 9 rakamı yanlış olduğu için çıktıya etkisi yoktur. 2 ve 3 rakamları yeleri   |
                |    de doğru olduğu için +2, 1 rakamının yeri yanlış tahmin edildiği için -1 ile        |
                |    belirtilecektir. O halde örnek çıktı +2 -1 olacaktır.                               |
                |                                                                                        |
                ------------------------------------------------------------------------------------------\n\n\n''')

while True:
    tahmin=input('{}. tahmininizi yapınız = \n'.format(tahminSayısı).center(100))  #oyuncunun tahmini
    puanlama = []   # puanlama degiskeni
    kontrol=[]    #tekrarlı rakam kontrolu icin degisken

    if tahmin.isdecimal()==False:  # yanlıs girdi yakalama
        print('Yanlış giriş yaptınız. Lütfen 4 basmaklı bir sayı tahmin ediniz.')

    else:
        tahminSayısı+=1     #tahmin sayısının 1 atırılması
        tahmin=list(tahmin)  #tahminin listeye donusturlmesi
        for i in range(4): # dort basamaklı sayı icin 4 defa dongu

            if tahmin[i] not in password:  #basamaktaki rakam password icinde yoksa dongude basa donme
                continue

            else: #tahmin edilen sayının her bir rakamının password icinde olması durumu

                if tahmin[i] in kontrol: #tekrarlı rakam olamsı durumunda uyarı ve donguyu kırma
                    print('Rakamları farklı bir sayı girmelisiniz.')
                    break

                elif tahmin[i]==password[i]:  #basamagın dogru tahmin edilip-edilmediginin kontrolu
                    puanlama+=['+1']  #basamagın da dogru tahmini icin puanlamaya +1 eklenmesi

                else:
                    puanlama+=['-1']  #dogru tahmin edilen rakamın basamagının yanlıs tahmin
                                      # edilmesi durumunda puanlamaya -1 eklenmesi
            kontrol += tahmin[i]

        print('Tahmininiz = ',*tahmin)
        print(*puanlama)

    if tahmin==password: #passwordun tahmin edilmesinin kotrolu
        print('TEBRİKLER, BİLDİNİZ.'.center(100))
        break















