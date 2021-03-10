# # Dosya açmak ve oluşturmak için open() fonksiyonu kullanılır
# # Kullanımı: oper(dosya_adi,dosya_erişme_modu)
# # dosya_erişme_modu => dosyayı hangi amaçla açtığımızı belirtir.
"""****************************************************"""
# #----- "w": (Write) yazmamodu. -----
# ***** Dosyayi konumda oluşturur.
# ***** Dosya içeriğini siler ve yeniden ekleme yapar.

# file = open("newfile.txt","w")
# file.close()

# file = open("C:/users/mehme/desktop/newfile.txt","w")

# file = open("newfile.txt","w",encoding="utf-8")  ##encoding?utf8 türkçe karakterler için
# file.write("Mehmetcan Yilmaz")
# file.close()
"""****************************************************"""
"""****************************************************"""
# # "a": (Append) ekleme.Dosya konumda yoksa oluşturur.
# file = open("newfile.txt","a",encoding="utf-8")
# file.write("Mehmetcan Yilmaz")
# file.write("Mehmetcan Yilmaz\n") ## Bir alta ekler ve altına bir satır oluşturur 
# file.close()
"""****************************************************"""
"""****************************************************"""
# # "x": (Create) oluşturma.Dosya zaten varsa hata verir.
file = open("newfile2.txt","x",encoding="utf-8")  ##encoding?utf8 türkçe karakterler için
file.write("Mehmetcan Yilmaz")
file.close()
"""****************************************************"""
"""****************************************************"""
# # "r": (Read) okuma. Dosya konumda yoksa hata verir.





