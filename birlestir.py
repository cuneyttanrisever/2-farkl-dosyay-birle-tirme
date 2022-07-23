oku=open("a.txt","r", encoding="utf-8")
dex=oku.readlines()
oku1=open("b.txt","r", encoding="utf-8")
dex2=oku1.readlines()
yaz=open("birles.txt","w",encoding="utf-8")
for i in range(len(dex)):
    birlestir=dex[i].replace("\n","")+" = "+dex2[i]
    print (birlestir)
    yaz.write(str(birlestir))

oku.close()
oku1.close()
yaz.close()
