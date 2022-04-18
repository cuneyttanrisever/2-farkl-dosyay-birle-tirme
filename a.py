oku=open("a.txt","r", encoding="utf-8").readlines()
oku1=open("b.txt","r", encoding="utf-8").readlines()
yaz=open("birles.txt","a",encoding="utf-8")
for i in range(len(oku)):
    birlestir=oku[i].replace("\n","")+" = "+oku1[i]
    print (birlestir)
    yaz.write(str(birlestir))