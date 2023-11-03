f=open("Dogs.txt")
s=f.readlines()
for x in s:
    x=x.replace("35","11")
    x=x.replace("94","25")
    print(x,end='')