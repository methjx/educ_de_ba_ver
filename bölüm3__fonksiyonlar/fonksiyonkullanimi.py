## 
def sayWhat(name = ", boş bırakırsan böyle olur"):
    print("nerdesin def"+ name)

sayWhat(", görüpde baktığın her yerde moruk")
sayWhat(", 1 saat sonra halısahada")
sayWhat()

######
def sayHello(name = "user"):
    return "hello " + name
message = sayHello()
message = sayHello("Mehmet")
print(message)
#####
def total(num1 , num2):
    return num1 + num2

result = total(10,20)
print(result)
######
def yasHesap(dogumYili):
    return 2021 - dogumYili

ageMert  = yasHesap(2000)
ageBilge = yasHesap(1995)    
print(ageBilge,ageMert)

def emekliligeKacYildKaldi(dogumYili, isim):
    """
    DOCSTRING: Dogum yiliniza gore emekliliginize kac yil kaldi. 
    INPUT: Dogum yili
    OUTPUT: Emeklilik yili bilgisi
    """
    yas = yasHesap(dogumYili)
    emeklilik = 65 - yas
    if emeklilik > 0:
        print(f"{isim}in , Emekliliğe daha {emeklilik} kadar yiliniz var.")
    else:
        print(f"Emeklisin zaten. {isim} " )   

emekliligeKacYildKaldi(1983,"kemal")
emekliligeKacYildKaldi(1940,"suna")
print(help(emekliligeKacYildKaldi)) #### içinde neler oldugunu kullanım şekli vs. help()


#####
