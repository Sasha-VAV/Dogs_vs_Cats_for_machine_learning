import time
from random import random

import numpy
from PIL import Image
from numpy import asarray

# load the image and convert into
# numpy array
createdataelearnfile=0
if createdataelearnfile==1:
    f = open("Dogs.txt", 'a')
    numofex=12500
    start_time=time.time()
    for iii in range(11702,numofex):
        for kk in range(2):
            """if iii/numofex==0.0112:
                print("")"""
            if iii%10==0:
                print(iii,iii/numofex,time.time()-start_time)
            if kk==0:
                sv="Dog"
            else:
                sv="Cat"
            sv=sv+"/"+str(iii)+".jpg"
            '''sv=sv.replace(" ","")'''
            "sv=sv[:sv.find(" ")]+sv[sv.find(" ")+1:]"
            try:
                img = Image.open(sv)
                numpydata = asarray(img)
            except:
                img = Image.open("corgi.jpg")
                numpydata = asarray(img)

            cm = 1 / 1  # масштабирование относительно разрешения 128
            razr = 4 / 3  # формат
            ci = int(128 * cm)
            cj = int(ci * razr)
            numofcolors = 4  # количество красных, синих, зеленых цветов по отдельности
            ck = 256 // (numofcolors)
            ii = len(numpydata)
            jj = len(numpydata[0])
            di = 0
            dj = 0
            if jj < (ii * razr):
                di = ii - jj / razr
                ii = jj / razr
            else:
                dj = jj - ii * razr
                jj = ii * razr
            ii = ii / ci
            jj = jj / cj


            a = numpy.zeros((ci, cj, 3))
            b = numpy.zeros((ci, cj))
            f.write(str(kk))
            f.write("\n")
            for i in range(ci):
                for j in range(cj):
                    s = ""
                    try:
                        for k in range(3):
                            a[i][j][k] = numpydata[int(i * ii) + int(di / 2)][int(j * jj) + int(dj / 2)][k] // ck * ck
                            s += str(((int(a[i][j][k]) // ck)))
                    except:
                        a[i][j][0] = numpydata[int(i * ii) + int(di / 2)][int(j * jj) + int(dj / 2)] // ck * ck
                        s += str(((int(a[i][j][0]) // ck)))
                    b[i][j] = int(s, numofcolors + 1)
                    f.write(str(int(s, numofcolors + 1)))
                    f.write(" ")
                f.write("\n")
            f.write('\n\n')


            # s=input("PRESS ANY BUTTON TO CONTINUE")

            """def cc(a, n):
                a = int(a)
                s = ""
                if (a == 0):
                    return "000"
                while (a > 0):
                    s = str(a % n) + s
                    a //= n
                if len(s) != 3:
                    s = "0" * (3 - len(s)) + s
                return s
            
            
            f = open("Dogs.txt")
            s = f.readlines()
            for i in range(ci):
                # s[i]=s[i][::-1].replace(str(int(random()*124)),str(int(random()*124)))#инверсия и добавление битых пикселей
                b[i] = list(map(int, s[i].split()))
            # Convert the pixels into an array using numpy
            f.close()
            array = numpy.array(a, dtype=numpy.uint8)
            new_image = Image.fromarray(array)
            new_image.save('new.png')
            for i in range(ci):
                for j in range(cj):
                    for k in range(3):
                        a[i][j][k] = int(cc(b[i][j], numofcolors + 1)[k]) * ck
            array1 = numpy.array(a, dtype=numpy.uint8)
            new_image1 = Image.fromarray(array1)
            new_image1.save('new1.png')"""
    f.close()
else:
    f = open("C:/Users/vav11/Git/Network2/Neuron2/ConsoleApplication1/Test.txt", 'w')
    img = Image.open("Dog/4206.jpg")
    numpydata = asarray(img)
    cm = 1 / 1  # масштабирование относительно разрешения 128
    razr = 4 / 3  # формат
    ci = int(128 * cm)
    cj = int(ci * razr)
    numofcolors = 4  # количество красных, синих, зеленых цветов по отдельности
    ck = 256 // (numofcolors)
    ii = len(numpydata)
    jj = len(numpydata[0])
    di = 0
    dj = 0
    if jj < (ii * razr):
        di = ii - jj / razr
        ii = jj / razr
    else:
        dj = jj - ii * razr
        jj = ii * razr
    ii = ii / ci
    jj = jj / cj

    a = numpy.zeros((ci, cj, 3))
    b = numpy.zeros((ci, cj))
    for i in range(ci):
        for j in range(cj):
            s = ""
            try:
                for k in range(3):
                    a[i][j][k] = numpydata[int(i * ii) + int(di / 2)][int(j * jj) + int(dj / 2)][k] // ck * ck
                    s += str(((int(a[i][j][k]) // ck)))
            except:
                a[i][j][0] = numpydata[int(i * ii) + int(di / 2)][int(j * jj) + int(dj / 2)] // ck * ck
                s += str(((int(a[i][j][0]) // ck)))
            b[i][j] = int(s, numofcolors + 1)
            f.write(str(int(s, numofcolors + 1)))
            f.write(" ")
        f.write("\n")
    f.write('\n\n')

    f.close()
    def cc(a, n):
        a = int(a)
        s = ""
        if (a == 0):
            return "000"
        while (a > 0):
            s = str(a % n) + s
            a //= n
        if len(s) != 3:
            s = "0" * (3 - len(s)) + s
        return s
    array = numpy.array(a, dtype=numpy.uint8)
    new_image = Image.fromarray(array)
    new_image.save('new.png')
    for i in range(ci):
        for j in range(cj):
            for k in range(3):
                a[i][j][k] = int(cc(b[i][j], numofcolors + 1)[k]) * ck
    array1 = numpy.array(a, dtype=numpy.uint8)
    new_image1 = Image.fromarray(array1)
    new_image1.save('new1.png')