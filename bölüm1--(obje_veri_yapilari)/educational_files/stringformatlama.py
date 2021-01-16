name = "mehmet"
surname = "yilmaz"
age = "25"
# print("My name is {} {} " .format(name , surname)) #süslü parantez yerine .format içindeki değeri tanımlamış oluruz.
# print("My name is {1} {0} " .format(name , surname)) #indeks numaraları normalde 0 1 şeklinde sıralanıyor fakat yer değiştirirsek bu durum indeks numarasına göre sıralar bkz.bu satır
# print("My name is {s} {n} " .format(n=name , s=surname)) # değişken tanıyıp aynı numaralarda olduğu gibi aynı sistemi uygulayabiliriz.
#print("My name is {s} {n} and I am {a} years old.  " .format(n=name , s=surname , a=age))

result = 200/700
# print("the result is :" , result) #şeklinde yapmıştım daha önce fakat şu şekildede olur;;
# print("the result is {r:1.2}".format(r=result))  # string bilgide float olarak çok fazla sayı gelince daha kısa bir sayı istediğim için bunu formatlıyorum r=1.3 diyerek 3'ile virgülden sonra kaç sayı geleceğini ayarlıyorum, 1' ile se tam kısım için ne kadar boşluk olacağını ayarlıyor.
# print(f"My name is {name} {surname} and I am {age} years old.") # fstring ile değikenleri direk yazarakda aynı sonucu elde edebiliriz.

