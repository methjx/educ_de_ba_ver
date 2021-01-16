message = "Hello there. My name is mehmetcan yilmaz"
# message = message.upper() # message değişkeni içindeki karakterleri büyük harfle yazdırır.
# message = message.lower() # message değişkeni içindeki karakterleri küçük harfle yazdırır.
# message = message.title() # her kelimenin baş harfi büyük yazılır.
# message = message.capitalize() # string ifadenin sadece ilk harif büyük yazılır.
# message = message.strip() # örneğin kullanıcı message içindeki ifadenin başında boşluk bırakmış olsun ve bu boşluk karakteri örneğin bir parola girerken boşluk olarak girdilenmiş olsun fakat normalde olmaması gerekiyor.bu durumda boşluğu aradan cıkarmak için strip kullanırız.
# message = message.split() # her bir karakteri ayırır ve bize ayrılmış şeklinde kelime kelime verir.karakter dizisi verir yani.
# ve bu .split()den sonra eğer [] ile 0 1 2 (farketmez) indeksine ulaşmak istersek parçalanmış  olan dizileri elde ederiz
# print(message[1]) #bkz.7 ve 8.satır
# message = message.split(".") # "." ile .'lardan itibaren ayır dedik yani bu örnekte hello there ve mynameis'kısmından itibaren 2 parça ayırdık.
#yine örneğin split kullandık ve parçaladık; bkz 12'den itibaren ;
# message = message.split()
# ve daha sonra birleştirmek istedik ;
# message = "*".join(message) # birleştirirken * koydugumuz yeri boş bırakırsak ilk elde ettiğimiz hali elde ederiz.
# index = message.find("mehmetcan") # örneğin burada istediğim cümle içerisinde bir kelimeyi arıyoruz o zaman biz bu işlemlerle index numarasını elde ederiz bu indeks numarasıda aradığımız kelimenin ilk harfinin indeksidir.
# print(index)
# isFound = message.startswith("H") #burada diyoruzki mesaj "H" harfi ile mi başlıyor? eğer öyleyse true bilgisi eğer değilse false bilgisi alırız.
# print(isFound)
# isFound = message.endswith("z") #eğer z ile bitiyorsa true aksi durum false
# print(isFound)

# message = message.replace("mehmetcan yilmaz" , "Mehmetcan Yilmaz") # verdiğimiz bilgideki kelime yerine başka bir kelime eklememizi sağlar
# message = message.replace("ç" , "c").replace(" ö " , " o ").replace("ı" , "i") #bunun genel kullanımı ingilizce makaledeki türkçe karakterler yerine ingilizce karakterleri yazdırabilmemizi sağlamasıdır.

message = message.center(50,"*") # bizim için bir konteynır oluşturur yani 50karakterlik alan içerisine mesajımızı ekler ve bunuda sağdan ve soldan tam ortalar.yıldız koyma sebebim boşluk bıraktıgım noktaları görmek istemem.bir web uygulamasında açıklama bilgisi oluştururken işe yarar.


print(message)
