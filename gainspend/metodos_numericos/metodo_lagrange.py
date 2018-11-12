
t = 7
x = [7.3,6.5,6.1,5.5]
y = [-.28,-1.35,-1.96,-2.74]


def metodolagrange(valor,xs,ys):
    i = 0
    px = 0
    temp =len(ys)
    while i < temp:
        divisor = 1
        dividendo=1
        l = ys[i]
        temp1=len(xs)
        cal=1
        j=0
        temp2= 1
        while j < temp1:
            if j != i:
                divisor=round((divisor*(valor - xs[j])),5)
                dividendo =round((dividendo*(xs[i] - xs[j])),5)
                cal=2
            j+=1
        px = px+(l*(divisor/dividendo))
        i+=1
    return px


#print(diferenciasvalor(t,x))
print (f'lagrange {metodolagrange(t,x,y)}')
