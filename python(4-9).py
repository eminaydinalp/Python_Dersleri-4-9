# Veri Tipi Dönüşümü (4.Ders)
# int -> float
a = 5
b = float(a)

# float -> int

c = 2.5
d = int(c)
e = 15/4
f = int(e)

# str -> int

g = "145"
h = int(g)
#i = "54ad4"
#j = int(i)


# int -> str

k = 154
l = str(k)

# float -> str

m = 36,78
n = str(m)


# Print (5.Ders)

print(5)
print("ali")

print("Ali :",5)

yas = 18
isim = "Ali"
print("Ali'nin Yaşi :",yas)
print("İsmi :",isim)

sayi1 = 14
sayi2 = 25
toplam = sayi1 + sayi2
print("Toplamlari : ",toplam)

# \n , \t

print("Merhaba\nBenim ismim\nali")
print("Aydin\tAnkara\tBursa")

# sep 

print("15","03","2020",sep="/")
print("15","03","2020",sep=".")



# Format (6.Ders)

yas = 18
isim = "Ali"
print("Ali'nin Yaşi :",yas)
print("İsmi :",isim)

print("İsmi : {} ve Yaşi : {}".format(isim,yas))

a = 25
print("{}'ın karekoku : {}".format(a,int(a**0.5)))

b = 100
c = 5
print("{0}'ın {1} e bolumunden kalan : {2}'dır.".format(b,c,b%c))

b = 5
c = 100
print("{1}'ın {0} e bolumunden kalan : {2}'dır.".format(b,c,b%c))

print("{2} {0} {1}".format(5,"ahmet",5.8))


# Listeler (7.Ders)

liste = [1,2,3,4,5,6,7,8,9]
liste2 = ["ankara",5,7.8,"ist",7,15,9]
print(len(liste))
print(len(liste2))

print(liste[0])
print(liste[5])
print(liste[-1])

print(liste[1 : 5: 2])
print(liste[3:])
print(liste[:5])
print(liste[::])
print(liste[::-1])

string = "ahmet"
liste3 = list(string)

# Listeler2 (8.Ders)

liste1 = [1,5,8,65,"istanbul"]
liste2 = [1,55,82,65,"ankara"]
liste3 = liste1 + liste2

print(liste2*2)

liste1.append("ali")
liste1.append(89)
liste2.clear()
liste2.append(3.4)

a = liste2.copy()

liste4 = [2,2,2,3,3,4,4]
liste4.count(2)
liste4.count(3)

liste3.pop(2)
liste5 = ["ömer","osman","ali"]
liste5.sort()
liste5.sort(reverse = True)

liste6 = [1,52,84,65]
liste6.sort()
liste6.sort(reverse = True)

# İçiçe Liste Oluşturma (9.Ders)

liste = [[2,8,65],[7,6,42],[6,8,75]]

print(liste[1][1])
print(liste[2][1])

liste1 = [1,5,8,65,"istanbul"]
liste2 = [1,55,82,65,"ankara"]

liste3 = [liste1, liste2]
print(liste3[0][4])





