# -*- coding: cp1254 -*-
tutulan = 123
while True :
    cevap = input("sayıyı tahmin ediniz: ")
    if(cevap == 0):break
    elif(cevap>tutulan):print "azalt"
    elif(cevap<tutulan):print "arttır"
    else:
        print "bildiğiniz sayı: " + str(tutulan)
        break
