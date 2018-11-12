import sympy
import random
import collections
# t = 3.5
# x = [1,2,3,4]
# y = [120,94,75,62]

def conseguirdeltas(list):
    delta = []
    list.reverse()
    delta.append(list[0])
    lista2=[]
    len2= len(lista2)
    len1= len(list)
    temp = 0
    temp1 = 0
    while len2 >1 or len1 >1:
        temp = 0
        temp1= 0
        for t in list:
            if temp == 0:
                cal= 1
                temp = t
            else:
                temp1= t
            if temp != 0 and temp1 != 0:
                valor = round((temp-temp1),2)
                if cal ==1:
                    delta.append(valor)
                    cal = 2
                lista2.append(valor)
                temp = temp1
                temp1= 0
        list.clear()
        len2 = len(lista2)
        temp= 0
        temp1=0
        cal = 1
        for t in lista2:
            if temp==0:
                temp= t
            else:
                temp1=t
            if temp != 0 and temp1 != 0:
                valor = round((temp-temp1),2)
                if cal ==1:
                    delta.append(valor)
                    cal = 2
                list.append(valor)
                temp = temp1
                temp1= 0
        lista2.clear()
        len1= len(list)
    return delta

def sacas(valor,list):
    print("Newton atras sacas")
    len1 = len(list)
    len1 -=1
    s = ((valor-list[len1])/(abs(list[1]-list[0])))
    return s


def metodo_newton_hacia_atras(t,x,y):
    s =sacas(t,x)
    deltas = conseguirdeltas(y)
    t =len(deltas)
    s1 = s+1
    s2 = s+2
    s3 = s+3
    s4 = s+4
    s5 = s+5
    if t==7:
        respuesta1= deltas[0]+deltas[1]*s+((deltas[2]*s*s1)/2)+((deltas[3]*s*s1*s2)/6)+((deltas[4]*s*s1*s2*s3)/24)+((deltas[5]*s*s1*s2*s3*s4)/120)+((deltas[6]*s*s1*s2*s3*s4*s5)/720)
    elif t==6:
        respuesta1= deltas[0]+deltas[1]*s+((deltas[2]*s*s1)/2)+((deltas[3]*s*s1*s2)/6)+((deltas[4]*s*s1*s2*s3)/24)+((deltas[5]*s*s1*s2*s3*s4)/120)
    elif t==5:
        respuesta1= deltas[0]+deltas[1]*s+((deltas[2]*s*s1)/2)+((deltas[3]*s*s1*s2)/6)+((deltas[4]*s*s1*s2*s3)/24)
    elif t==4:
        respuesta1= deltas[0]+deltas[1]*s+((deltas[2]*s*s1)/2)+((deltas[3]*s*s1*s2)/6)
    elif t==3:
        respuesta1= deltas[0]+deltas[1]*s+((deltas[2]*s*s1)/2)
    elif t==2:
        respuesta1= deltas[0]+deltas[1]*s
    else:
        respuesta1= deltas[0]
    return respuesta1

#print (sacas(t,x))
#print(conseguirdeltas(y))
print("Newton atras")
# print (f'Newton atras {metodo_newton_hacia_atras(t,x,y)}')
