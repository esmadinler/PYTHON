print "___Dosyaya Kayıt Yaz işlemi yapan program___\n“
while True:
 print "___Öğrenci Bilgilerini Giriniz___ Numara sıfır girilince biter"
 nmr=input("Numara......:")
 if (nmr==0): break
 ads=raw_input("AdSoyad.....:")
 vnt=input("Vize Notu...:")
 fnt=input("Final Notu..:")
 ont=int(vnt*0.4 + fnt*0.6)
 print "\n Ortalama Not=",ont
onmr=str(nmr)
 oads=(ads)
 ovnt=str(vnt)
 ofnt=str(fnt)
 oont=str(ont)
 ogrdos=open("ogrblg.dat","a")
 ogrkay=(onmr + "\t" + oads + "\t" + ovnt + "\t" + ofnt + "\t" + oont
+ "\n")
 ogrdos.write(ogrkay)
 ogrdos.close()
 print "\n Kayıt Yazılmıştır. \n\n“
 cev=raw_input("Başka işlem yapılmayacaksa Çıkış(sıfır) giriniz : ")
 if (cev=="0"): break
else: print "\n Çıkıldı. “
print "\n ----- \n Program Bitti“
