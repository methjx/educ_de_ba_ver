x, y, z = 5, 10, 20

#x,y = y,x # değişken yerini değiştirdik.

# x += 5 ## mean is ----> x = x + 5
# x -= 5 ## mean is ----> x = x - 5
# x *= 5
# x /= 5
# x %= 5

# print(x,y,z)

values = (1, 2, 3, 4, 5 ) ## paranteze almasakda type tuple!!
print(values)
print(type(values))

x, y, *z = values     # z 'nin önüne yıldız koydugumuzda listede boşta kalan değerlerin hepsini z içerisinde gruplar (listeler)
                        # bunu gidip y nin onüne koyarsan bu sefer 1 = x , 5= z [2,3,4] = y olur yaniiii

print(x,y,z)
print(x,y,z[1])        ### z listesi içindeki verilere indeksle ulaşmak için ...
