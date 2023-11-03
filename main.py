import time

import numpy
from PIL import Image
from numpy import asarray

# load the image and convert into
# numpy array
img = Image.open('corgi.jpg')
numpydata = asarray(img)

cm=1#масштабирование относительно разрешения 128
razr=4/3#формат
ci=int(128*cm)
cj=int(ci*razr)
numofcolors=4#количество красных, синих, зеленых цветов по отдельности
ck=256//(numofcolors)
ii=len(numpydata)
jj=len(numpydata[0])
di=0
dj=0
if jj<(ii*razr):
    di=ii-jj/razr
    ii=jj/razr
else:
    dj=jj-ii*razr
    jj=ii*razr
ii=ii/ci
jj=jj/cj
f=open("Dogs.txt",'w')

a=numpy.zeros((ci,cj,3))
b=numpy.zeros((ci,cj))
for i in range(ci):
    for j in range(cj):
        s=""
        for k in range(3):
            a[i][j][k]=numpydata[int(i*ii)+int(di/2)][int(j*jj)+int(dj/2)][k]//ck*ck
            s+=str(((int(a[i][j][k])//ck)))
        b[i][j]=int(s,numofcolors+1)
        f.write(str(int(s,numofcolors+1)))
        f.write(" ")
    f.write("\n")
f.close()



#s=input("PRESS ANY BUTTON TO CONTINUE")

def cc(a,n):
    a=int(a)
    s=""
    if (a==0):
        return "000"
    while (a>0):
        s=str(a%n)+s
        a//=n
    if len(s)!=3:
        s="0"*(3-len(s))+s
    return s


f=open("Dogs.txt")
s=f.readlines()
for i in range(ci):
    b[i]=list(map(int,s[i].split()))
# Convert the pixels into an array using numpy
array = numpy.array(a, dtype=numpy.uint8)

# Use PIL to create an image from the new array of pixels
new_image = Image.fromarray(array)
new_image.save('new.png')
for i in range(ci):
    for j in range(cj):
        for k in range(3):
            a[i][j][k]=int(cc(b[i][j],numofcolors+1)[k])*ck

array1 = numpy.array(a, dtype=numpy.uint8)

# Use PIL to create an image from the new array of pixels
new_image1 = Image.fromarray(array1)
new_image1.save('new1.png')
# data
'''print(len(numpydata),len(numpydata[0]))
time.sleep(10000)
for i in range(len(numpydata)):
    for j in range(len(numpydata[i])):
        print(hex(numpydata[i][j][0])[2:]+hex(numpydata[i][j][1])[2:]+hex(numpydata[i][j][2])[2:],end="||")
    print("")'''