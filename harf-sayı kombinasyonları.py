# coding=utf-8
rakam=['1','2','3','4','5','6','7','8','9','10']
harf=['a','b','c','d','e','f','g','h','j','k']
kombinasyon1=[]  #kombinasyonların atanacagı
kombinasyon2=[]  #listeler
for i in rakam:  #rakam listesi icindeki verileri icin dongu
    for n in harf: #harf listesi icindeki verileri icin dongu
        kombinasyon1+=[i+n]  #olusan kombinasyonların listeye dahil edilmesi
        kombinasyon2+=[n+i]

print(kombinasyon1)
print(kombinasyon2)

