while 1:
print "...MENÜ İŞLEMLERİ..."
print "1.kayıt Yaz"
print "2.kayıt Listele"
print "3.kayıt AraBulGöster"
print "4.kayıt Sil "
print "5.kayıt Düzelt"
print "6.veri dosyasını yedekle"
print "0.ÇIKIŞ"
sec=input("\n Lütfen bir şeçenek giriniz :")
if(sec==1): 
 kism=raw_input("isim :")
 ksfr=raw_input("şifre :")
 kads=raw_input("Adınız ve soyadınız :")
 kyg=raw_input("Kayıt grubu :")
 keml=raw_input("kullanıcı email :")
 kgyg=raw_input("Giriş yapacağı gün rakamı :")
 AbkbDos=open("kul.Dat","a")
 print "\n Kayıt YAZILDI \n"
 
kayit=(kism+"\t"+ksfr+"\t"+kads+"\t"+kyg+"\t"+keml+"\t"+kgyg+"\n")
 AbkbDos.write(kayit)
 AbkbDos.close()
if(sec==2):
 os.getcwd()
 AbkbDos=open("kul.dat","r")
 print AbkbDos.read()
 AbkbDos.close()
if(sec==3):
 print "Hazır Değil“
if(sec==4):
 print "Hazır Değil"
if(sec==5):
 print "Hazır Değil" 
if(sec==6):
 print "Hazır Değil"
 
if (sec==0): break
print "\n ----- \n Program Bitti"
