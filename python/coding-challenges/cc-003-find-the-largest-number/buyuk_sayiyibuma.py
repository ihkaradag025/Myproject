a= int(input("Lütfen Giriş Yapacağınız Sayı Miktarını Giriniz : "))
b=[]
buyuk=0
for i in range(a):
    c =int(input("Bir Sayı Giriniz : "))
    b.append(c)
    if c > buyuk:
        buyuk=c
        print(b)
print ("Girdiğiniz Sayıların En Büyüğü :",buyuk)    
 