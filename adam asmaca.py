agac0=(r'''        _________ 
        |       |
        |       
        |     
        |     
        |               
        |      
        |     
        |
     -------          ''')

agac1=(r'''        _________ 
        |       |
        |       O
        |     
        |     
        |             
        |     
        |     
        |
     -------          ''')

agac2=(r'''        _________ 
        |       |
        |       O
        |       |
        |       |
        |       |        
        |     
        |     
        |
     -------          ''')

agac3=(r'''        _________ 
        |       |
        |       O
        |      /|
        |     / |
        |       |        
        |      
        |     
        |
     -------          ''')

agac4=(r'''        _________ 
        |       |
        |       O
        |      /|\
        |     / | \
        |       |        
        |     
        |     
        |
     -------          ''')

agac5=(r'''        _________ 
        |       |
        |       O
        |      /|\
        |     / | \
        |       |        
        |      / 
        |     /   
        |
     -------          ''')

agac6=(r'''        _________ 
        |       |
        |       O
        |      /|\
        |     / | \
        |       |        
        |      / \
        |     /   \
        |
     -------          ''')

agac=[agac0,agac1,agac2,agac3,agac4,agac5,agac6] #daragacı listesi
anahtar=list(input('Bir kelime giriniz.\n').upper()) #sifre kelime girisi ve buyuk harf yapma
print('\n'*15)  #ekranı kaydırma
tabela=list('-' * len(anahtar))  #ekrana yazdırılan kelime degiskeni
topTahmin=[]  #tahminlerin biriktirildigi deisken
tahminHakki=6  #tahmin hakkı degiskeni
from time import sleep  #sleep fonksiyonunu dahil etme
print('''                           __________________________________________________
                          |                                                  |
                          |         Adam asmaca oyununa hoş geldiniz.        |
                          |      Bu oyunda toplam 6 tahmin hakkınız var.     |
                          |     Eğer kendinize güveniyorsanız kelimeyi de    |
                          |                tahmin edebilirsiniz.             |
                          ----------------------------------------------------''')
print('\n'*8)
while True:
    if tahminHakki==0: #tahmin hakkı bitmesi durumu
        print('BİLEMEDİNİZ\n','KELİME = ',*anahtar,sep='')
        break

    tahmin=input('Bir harf tahmin ediniz.\n\n'.center(100))  #oyuncu tahmin girisi ve ekran cıktısı ortalama
    tahmin=tahmin.upper()  #girdiyi buyuk harf yapma

    if tahmin.isalpha()==False:  #alfabe hatası yakalama
        print('Yanlış giriş yaptınız.\n\n'.center(100))
        sleep(2)  #2 sn uyutma

    elif tahmin in topTahmin:    #tekrar hatası yakalama
        print('Bu harfi söylemiştiniz.\n\n'.center(100))
        sleep(2)  #2 sn uyutma

    elif list(tahmin)==anahtar:  #kelimeyi tahmin etme durumu
        print('\n' * 15)
        print('TEBRİKLER, BİLDİNİZ.\n'.center(100))
        print(agac[6 - tahminHakki])  #daragacı ekran cıktısı
        print(*anahtar)  #kimeyi ekrana yazdırma
        break #donguyu kırma

    elif len(tahmin)>1:  #birden fazla harf giris hatası
        print('Yanlış giriş yaptınız.\n\n'.center(100))
        sleep(2)

    elif tahmin not in anahtar:  #tahmin edilen harfin kelimede olmaması durumu
        tahminHakki -= 1  # tahmin hakkı 1 azalır

    else:
        topTahmin+=[tahmin]    #tahminleri toplam tahminde biriktirir
        for i in range(len(anahtar)):  #anahtar uzunlugunca dongu
            if tahmin==anahtar[i]:   #tahmin edilen haraf anahtarda ise
                tabela[i]=tahmin     #tahmini tabelaya ekle

    if anahtar==tabela:  #ekrana yazdırılan kelımenin tamamlanması durumu
        print('\n' * 15)
        print('TEBRİKLER, BİLDİNİZ.\n'.center(100))
        print(agac[6 - tahminHakki])  #daragacı ekran cıktısı
        print(*anahtar)
        break

    print('\n' * 15)
    print(agac[6 - tahminHakki])  #daragacı ekran cıktısı
    print(*tabela)
    if tahminHakki>0:  #tahmin hakkını ekrana yazdırma
        print('{} HAKKINIZ KALDI.'.format(tahminHakki))












