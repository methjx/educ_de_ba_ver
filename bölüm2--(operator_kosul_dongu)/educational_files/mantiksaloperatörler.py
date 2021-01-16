x = 6 # ve 6 'deneyerek inceleyebilirim.
result = 5 < x < 10  ###    Sordugumuz 2 soru var 5den buyuk 10dan kucuk olması gerekir fakat herzaman matematiksel ifadeler kullanmayabiliriz o yüzden and or ve not
hak = 5
devam = "e"

#and
result = (x > 5 )and (x < 10 )  ## 2 soru sorduk Eğer ifade doğru ise (TRUE , TRUE ---> TRUE) şeklinde olacaktık ifadede iki koşuluda sağlaması gerekmektedir. Yani TRUE , FALSE ---> FALSE olacaktır.
result = (hak > 0) and (devam == "e") ##örneğin kullanıcı bir oyun oynuyor ve hakkı bitmiş ise kullanıcı devam etmek istese bile hakkı bittiğinden (hak=false olacaktır.)

#or
result = (x > 0) or (x % 2 == 0 )  ## True, False ==> True ## Yani sadece 1 tane true bilgisi almamız yeterli olacaktır ve true değeri gelecektir.

#not
result = not (x > 0)  ## not tam tersi değer verir bize

### x, 5-10 arasında olan bir çift sayımı ? diye bir örnek çözelim
result = ((x>5) and (x<10)) and (x%2==0)




print(result)