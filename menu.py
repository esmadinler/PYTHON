# -*- coding: cp1254 -*-
def Pmenu():
  print "____Menu____"
  print "0.Çıkış"
  print "1.Kayıt yaz"
  print "2.Kayıt oku-göster"
  print "3.Kayıt listele"
  print "4.Kayıt Düzelt"
  print "5.Kayıt sil"
  s=input("\n Lütfen bir seçenek giriniz: ")
  return s
def DKYaz():
  print "\n Dosyaya kayıt yaz bölümü \n"
def DKOkuGos():
  print "\n Dosyaya kayıt oku-göster bölümü \n"
def DKLst():
  print "\n Dosyaya kayıt listeleme bölümü \n"
def DKDuz():
  print "\n Dosyaya kayıt düzeltme bölümü \n"
def DKSil():
  print "\n Dosyaya kayıt sil bölümü \n"
#başla
while True:
  sec=Pmenu()
  if (sec==0): break
  if (sec==1): DKYaz()
  if (sec==2): DKOkuGos()
  if (sec==3): DKLst()
  if (sec==4): DKDuz()
  if (sec==5): DKSil()
  elif (sec<0 or sec>5):
    print "\n hatalı seçim yaptınız, tekrar giriniz \n"
print "\n BİTTİ"
#bitti
