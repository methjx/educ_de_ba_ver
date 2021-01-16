# "Bmw , Mercede , Opel ,Mazda" elemanlarna sahip bir liste oluşturunuz.
modelList = ["BMW" , "Mercedes" , "Opel" ,"Mazda"]
result = modelList
# liste kaç elemanlıdır ?
result = len(modelList)
# listenin ilk ve son elemanı nedir? 
result = modelList[0]
result = modelList[3]
# mazda değerini toyota ile değiştiriniz.
modelList[3] = "Toyota"
result = modelList
# mercedes listenin bir elemanımıdır
result = "Mercedes" in modelList  # "in" komutu içinde bu var mı diyor.. 
# listenin -2 indeksindeki değer nedir ?
result = modelList[-2]
# listenin ilk 3 elemanını alın.
result = modelList[0:3]
# listenin son 2 elemanı yerine "toyota" ve " renault" değerlerini ekleyin.
modelList[-2:] = ["Toyota" , "Renault"]         # modelList[2] = "Toyota"
                                                # modelList[3] = "Renault"
result = modelList
# listenin üzerine "audi" ve "nissan" değerlerinin ekleyin.
result = modelList + ["Audi" , "Nissan"]

# listenin son elemanını silin
del modelList[-1]
result = modelList

# liste elemanlarını tersten yazdırınız.
result = modelList[::-1]
# aşağıdaki verileri bir liste içinde saklayınız

#     studentA: Mehmetcan Yılmaz 1996 ,(70,60,70)
#     studentB: Mert Yılmaz      2000 , (80,80,70)
#     studentC: Bilge Yılmaz     2027 , (80,70,90)
studentA = ["Mehmetcan Yılmaz",1996,[70,60,70]]
studentB = ["Mert Yılmaz",2000,[80,80,70]]
studentC = ["Bilge Yılmaz",2027,[80,70,90]]
clasRom = studentA + studentB + studentC
result = clasRom
#liste elemanlarını ekrana yazdırınız
result = studentA[1]
result = studentB[2][0]    #-----> studentB içerisinde not bilgilerini öğrenmek istedik [2] ve bu notlar içerisinde ilk notunu öğrenmek istedik [0]
result = studentC[0]
result = f"{studentA[0]} yaşı {2020-studentA[1]} ve not ortalaması {(studentA[2][0]+studentA[2][1]+studentA[2][2])//3} dır."
# result = f"{} yaşı {} ve not ortalaması {} dır."
# result = f"{} yaşı {} ve not ortalaması {} dır."

print(result)
