from PIL import Image
"""
i = Image.open("Imagetest.bmp")

sortie = i.copy()
for y in range(i.size[1]):
    for x in range(i.size[0]):
        c = i.getpixel((x,y))
        sortie.putpixel((y,x),c)
        
sortie.save("Imageout.bmp")


j = Image.open("hall-mod_0.bmp")
sortie1 = j.copy()

for y in range(j.size[1]):
    for x in range(j.size[0]):
        c = j.getpixel((j.size[0]-x-1,y))
        sortie1.putpixel((x,y),c)

sortie1.save("Imageout2.bmp")

k = Image.open("IUT-Orleans.bmp")
sortie2 = k.copy()

for y in range(k.size[1]):
    for x in range(k.size[0]):
        R,V,B = k.getpixel((x,y))
        gris = int((R+V+B)/3)
        sortie2.putpixel((x,y),(gris,gris,gris))

sortie2.save("Imageout3.bmp")
"""

l = Image.open("IUT-Orleans.bmp")
sortie3 = l.copy()

for y in range(l.size[1]):
    for x in range(l.size[0]):
        R,V,B = l.getpixel((x,y))
        if (R*R+V*V+B*B)>255*255*3/2:

            sortie3.putpixel((x,y),(255,255,255))
        else:
            sortie3.putpixel((x,y),(0,0,0))
sortie3.save("Imageout4.bmp")





def cacher(i,b):
    return i-(i%2)+b


m1 = Image.open("hall-mod_0.bmp")
m2 = sortie3

sortie4 = m1.copy()
for y in range(m2.size[1]):
    for x in range(m2.size[0]):
        c1 = m1.getpixel((x,y))
        c2 = m2.getpixel((x,y))
        if c2 == (255,255,255):
            b = 1
        else:
            b = 0
        sortie4.putpixel((x,y),(cacher(c1[0],b),c1[1],c1[2]))

sortie4.save("Imageout5.bmp")


a = Image.open("Imageout5.bmp")
sortie5 = a.copy()

def trouver(i):
    return i%2

for y in range(a.size[1]):
    for x in range(a.size[0]):
        c = a.getpixel((x,y))
        b = trouver(c[0])
        sortie5.putpixel((x,y),(b*255,b*255,b*255))

sortie5.save("Imageout6.bmp")



