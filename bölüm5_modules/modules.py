#Hazır modul kullanımı;
## Yöntem 1 ;
# import math
import math as islem
# value = dir(math)
# value = help(math)
# value = help(math.factorial)
# value = math.sqrt(25)
# value = math.factorial(5)
# value = math.floor(5.9) ## asagı yuvarlar sayıyı;
# value = math.ceil(5.9) ## yukarı yuvarlar sayiyi;

###---Takma isimle;
# value = islem.factorial(5)

## Yöntem 2;

# from math import * ### ^ * ^ ile herşeyi import etmiş oluyoruz;

from math import factorial,sqrt,ceil ### seklinde neyi kullanacağımızı yazarsak da import ettiklerimizi kullanabiliriz.
def sqrt(x):
    print("x : " + str(x))
# value = factorial(5) ## Aynı zamanda bu yöntemde direk işleme girebiliriz , anlamazsan karşılaştırabilirsin.
value = sqrt (9)
# value = ceil(5.4)








print(value)