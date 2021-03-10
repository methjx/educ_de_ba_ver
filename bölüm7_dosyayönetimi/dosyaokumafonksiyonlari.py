with open("newfile2.txt","r",encoding="utf-8") as file:
    content = file.read(10)
    print(content)      ### ilk satırdaki kodun yaşam süresi codun sonunda bitmektedir.
    file.seek(10)   ##kürsörü 10.konuma getirir content2 içerisinden 10.veriden itibaren devameder
    print(file.tell())
    content2 = file.read(5)
    print(content2)
