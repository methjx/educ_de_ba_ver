# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     file.seek(20)
#     file.write("Deneme")

# with open("newfile.txt","r+",encoding="utf-8") as file:
#     print(file.read())

# ---------------------SAYFA SONUNDA GÜNCELLEME**************
# with open("newfile.txt","a",encoding="utf-8") as file:
#     file.write("\nBuse")
    
# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())

# ---------------------SAYFA BAŞINDA GÜNCELLEME**************
# with open("newfile.txt","r+",encoding="utf-8") as file:     ##Güncelleme yaptık dosyaya yazdırmadık !
#     content = file.read()
#     content = "Efecik\n" + content
#     file.seek(0)
#     file.write(content)         # Şimdi güncelledik ve yazdırdık.
#     print(content)

# with open("newfile.txt","r",encoding="utf-8") as file:
#     print(file.read())

# ---------------------SAYFA ORTASINDA GÜNCELLEME**************   

with open("newfile.txt","r+",encoding="utf-8") as file:
    list = file.readlines()
    # print(list)
    list.insert(1,"Ayşe Genç\n")
    print(list)
    file.seek(0)
    # for i in list:              #{for metodu yerine file.writelines()Kullanılabilir
        # file.write(i)               #}
    file.writelines(list)

with open("newfile.txt","r",encoding="utf-8") as file:
    print(file.read())

              