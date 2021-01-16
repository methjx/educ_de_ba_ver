
# username = input("Nick: ")
# password = int(input("Sifre: "))
username = "memocan"
password = "1234"                     


if (username == "memocan"):                ####iç içe if kullandık neden? :çünkü 2 koşul sağlamak istedim ilk "if ve else"'miz username'in doğruluğu için eğer yanlışsa direk else gider.eğerdoğruysa devam eder ve 2."if"e gelir o kısımda şifre için eğer şifre doğruysa açılır değilse 2.else'e gider.
    if (password == "1234"):
        print("Hoşgeldiniz")
    else:
        print("Şifre yanlış!")    
else:
    print("Username yanlış!")
