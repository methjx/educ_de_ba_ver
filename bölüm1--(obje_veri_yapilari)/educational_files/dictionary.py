# #key-value sistemiyle çalışır 41-->kocaeliyi temsil eder ya da 34-->istanbulu bir bilgiye ulaşmak için key bilgisi kullanacagız.Öncelikle dictionary olmadan listeyle şu şekilde yapılır.;

# # sehirler = ["Kocaeli","Istanbul"]
# # plakalar = [41,34]
# # print(plakalar[sehirler.index("Istanbul")])

# ####################

# # plakalar = { "key" : "value" } #####----mantık bu dictionary
# plakalar = { "Kocaeli" : 41, "Istanbul" : 34 }  
# print(plakalar["Kocaeli"])
# print(plakalar["Istanbul"])

# plakalar["Ankara"] = 6 ##  listelere yeni bir şehir ve plaka eklemiş oluruz.
# plakalar["Kocaeli"] = "new value" ## ya da olan sehre yeni bir değer ata
# print(plakalar)

users = {
    "Mehmetcan Yilmaz" : {
        "Yaşı" : 24,
        "Rolü" : ["user"],
        "Emaili" : "mehmetcn_ylmz@hotmail.com",
        "Adresi" : "Istanbul" ,
        "Telefon no" : "12313121",
    } ,  
    "Mert Yilmaz" : {
        "Yaşı" : 20,
        "Rolü" : ["admin","user"],
        "Emaili" : "mrt.00.ylmz@hotmail.com",
        "Adresi" : "Istanbul" ,
        "Telefon no" : "145453121",
    } ,

}
# print(users["Mert Yilmaz"]["Yaşı"])
# print(users["Mert Yilmaz"]["Emaili"])
# print(users["Mert Yilmaz"]["Adresi"])
print(users["Mert Yilmaz"])