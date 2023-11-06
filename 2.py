import math
k=100
sh=10
for x in range(-k,k+1,sh):
    for y in range(-k,k+1,sh):
        for a in range(-k,k+1,sh):
            for b in range(0,2):
                ok=True
                er=10
                m=[0.0]*4
                for n1 in range(2):
                    for n2 in range(2):
                        c=n1*x/k+n2*y/k+a*b/k
                        c=1/(1+2.718**(-c))
                        ok=ok and (round(c)==(n1 or n2))
                        m[n1*2+n2]=((n1 or n2)-c)**2
                if ok and (sum(m)/4)**0.5<er:
                    er=(sum(m)/4)**0.5
                    print(x/k,y/k,a/k,b,m)
                    for n1 in range(2):
                        for n2 in range(2):
                            c = n1 * x / k + n2 * y / k + a * b / k
                            c = 1 / (1 + 2.718 ** (-c))
                            print(round(c),n1,n2)