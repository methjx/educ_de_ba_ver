# try:
#     file = open("newfile3.txt","r")
#     print(file)
# except FileNotFoundError:
#     print("Dosya Okuma Hatası")
# finally:
#     print("Dosya kapandı")
#     file.close()
#///////////////////////////////////////////////////
file = open("newfile.txt","r",encoding="utf-8")
# #okuma işlemini for döngüsü ile yapabiliriz,
# for i in file:
#     print(i,end="") ## end="""" --->aralardaki boşlukları kaldırmak için yapılabilir.
#//////////////////////////////////////////////////
#*** read() fonksiyonu
# content1 = file.read()
# print("içerik 1")
# print(content1)
# # file = open("newfile.txt","r",encoding="utf-8")

# content2 = file.read()
# print("içerik2")
# print(content2)
# file.close()
# //////////////////////////////////
# content = file.read(5) # 5byte  oku 5 char
# print(content)
# ///////////////////////

# ****************** readline() fonksiyonu
# print(file.readline())
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline(),end="")
# print(file.readline())
# print(file.readline())
# file.close
# //////////////////////
# ********************** readlines() fonksiyonu 
liste = file.readlines()
print(liste)
file.close()