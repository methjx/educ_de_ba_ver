##Random Modülü;
import random 
# result = dir(random)
# result = help(random)
result = random.random() # 0.0 - 1.0
result = random.random()*100 
result = int(random.uniform(10,120)) ## Aralık belirtiyoruz--- Eğer tam sayı şeklinde istersek int içine alabiliriz.
result = random.randint(1,22) ##Aynı şekilde randitde kullanılabilir.

greeting = "Hello There"
names = ["Ali", "Yağmur", "Deniz", "Cenk"]
result = names[random.randint(0,len(names)-1)]
result = random.choice(names) ## Bir üsttekinin aynısı...!
result = random.choice(greeting)

liste = list(range(10))
random.shuffle(liste) ## Everyday m shuffling ....

result = liste
####
liste = range(100)
result = random.sample(liste,3) ## rastgele 3 tane istersem ....
result = random.sample(names,2)

print(result)
