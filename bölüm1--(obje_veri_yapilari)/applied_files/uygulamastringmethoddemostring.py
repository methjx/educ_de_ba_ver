website = "http://www.sadikturan.com"
course = "Python Kursu: Baştan Sına Python Programlama Rehberiniz (40 saat)"


# 1- " Hello World " karakter dizisinin baş ve sondaki boşluk karakterlerini silin.!
result = " Hello World ".strip()

# 2- "www.sadikturan.com" içindeki sadikturan bilgisi hariç her karakteri silin.
result = website.lstrip("htp:/.w") #.strip("bu kısımada sileceğimiz harfleri yazabiliyoruz.")
result = website.rstrip(".com")
result = website.strip("htp:./comw")

# # 3- "course" karakter dizisinin tüm karakterlerini küçük harf yapın.
result = course.lower()

# # 4- "website" içinde kaç tane a karakteri vardır? (count("a"))
result = website.count("a")
# website = website.count("a",0,10)----> şeklinde yazarsan 0 ve 10. karakterler arasında varmı diye sormus olursun

# 5- "website" www ile başlayıp com ile bitiyormu
result = website.startswith("www")                # isFound = website.endswith("com")  #######BURASI ALTERNATİF SEÇENEK
result = website.endswith(".com")                 # print(isFound)                     #######BURASI ALTERNATİF SEÇENEK
                                                  # isFound = website.startswith("www")#######BURASI ALTERNATİF SEÇENEK
                                                  # print(isFound)                     #######BURASI ALTERNATİF SEÇENEK
              
# # 6- "website içinde  ".com" ifadesi varmı
result = website.find(".com")            # index = website.find(".com")   ########BURASI ALTERNATİF
result = website.find(".com",0,11)       # print(index)                   ########BURASI ALTERNATİF                       
result = website.find(".com",0,28)       # print(website[21:])            ########BURASI ALTERNATİF    

# 7- "course" içindeki karakterlerin hepsi alfabetikmi (isAlpha , isdigit)
result = course.isalpha()
result = course.isdigit()
result = "123".isdigit()

# 8- "Contents" ifadesini satırda 50 karakter içine yerleştirip sağ ve soluna * ekleyiniz.
result = "Contents".center(50,"*")


# 9- "course" karakter dizisindeki tüm boşluk karakterlerini "-" ile değiştirin
result = course.replace(" ","-")
result = course.replace(" ","-",5) #5 koyarak 5 tanesinin arasına "-" koymuş oluruz.


# 10- "Hello World" karakter dizisinin "World" ifadesini "There" olarak değiştirin
result = "Hello World"
result = result.replace("World","There").replace("Hello","Hey")


# 11- "course" karakter dizisini boşluk karakterlerinden ayırın.
result = course.split(" ")

print(result)
