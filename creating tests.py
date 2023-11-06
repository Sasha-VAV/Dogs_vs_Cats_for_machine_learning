f=open("learn.txt","w")
for a in range(2):
    for b in range(2):
        if (a!=b):
            f.writelines("1")
        else:
            f.writelines("0")
        f.writelines("\n")
        f.writelines(str(a)+" "+str(b))
        f.writelines("\n")
f.close()