def toplama(a,b):
    return a+b
def cikarma(a,b):
    return a-b
def carpma(a,b):
    return a*b
def bolme(a,b):
    return a/b

def islem(f1,f2,f3,f4,islem_adi):
    if islem_adi == "Toplama":
        print(f1(2,3))
    elif islem_adi == "Cikarma":
        print(f2(5,3))
    elif islem_adi == "Carpma":
        print(f3(6,3))
    elif islem_adi == "Bölme":
        print(f4(12,3))    
    else:
        print("Gecersiz islem!!!")

islem(toplama,cikarma,carpma,bolme,"Toplama")
islem(toplama,cikarma,carpma,bolme,"Cikarma")
islem(toplama,cikarma,carpma,bolme,"Carpma")
islem(toplama,cikarma,carpma,bolme,"Bölme")
islem(toplama,cikarma,carpma,bolme,"Bölmasdae")