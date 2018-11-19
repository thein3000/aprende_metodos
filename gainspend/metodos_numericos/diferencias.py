
t = 7
x = [7.3,6.5,6.1,5.5]
y = [-.28,-1.35,-1.96,-2.74]

def manejo_diferencias(listax,listay,valor):
    temp = len(listay)
    deltas=[]
    if temp == 5:
        delta = resolverlistas5(listax,listay)
        respuesta = delta[0]+delta[1]*(valor-listax[0])+delta[2]*(valor-listax[0])*(valor-listax[1])+delta[3]*(valor-listax[0])*(valor-listax[1])*(valor-listax[2])+delta[4]*(valor-listax[0])*(valor-listax[1])*(valor-listax[2])*(valor-lista[3])
    elif temp ==4:
        delta = resolverlistas4(listax,listay)
        respuesta = delta[0]+delta[1]*(valor-listax[0])+delta[2]*(valor-listax[0])*(valor-listax[1])+delta[3]*(valor-listax[0])*(valor-listax[1])*(valor-listax[2])
    else :
        delta = resolverlistas3(listax,listay)
        respuesta = delta[0]+delta[1]*(valor-listax[0])+delta[2]*(valor-listax[0])*(valor-listax[1])
    return respuesta

def resolverlistas5(listax1,listay1):
    listay2 = []
    listay3 = []
    listay4 = []
    listay5 = []
    valor = round((listay1[1]-listay1[0])/(listax1[1]-listax1[0]),6)
    listay2.append(valor)
    valor = round((listay1[2]-listay1[1])/(listax1[2]-listax1[1]),6)
    listay2.append(valor)
    valor = round((listay1[3]-listay1[2])/(listax1[3]-listax1[2]),6)
    listay2.append(valor)
    valor = round((listay1[4]-listay1[3])/(listax1[4]-listax1[3]),6)
    listay2.append(valor)
    valor = round((listay2[1]-listay2[0])/(listax1[2]-listax1[0]),6)
    listay3.append(valor)
    valor = round((listay2[2]-listay2[1])/(listax1[3]-listax1[1]),6)
    listay3.append(valor)
    valor = round((listay2[3]-listay2[2])/(listax1[4]-listax1[2]),6)
    listay3.append(valor)
    valor = round((listay3[1]-listay3[0])/(listax1[3]-listax1[0]),6)
    listay4.append(valor)
    valor = round((listay3[2]-listay3[1])/(listax1[4]-listax1[1]),6)
    listay4.append(valor)
    valor = round((listay4[1]-listay4[0])/(listax1[4]-listax1[0]),6)
    listay5.append(valor)
    deltas.append(listay1[0])
    deltas.append(listay2[0])
    deltas.append(listay3[0])
    deltas.append(listay4[0])
    deltas.append(listay5[0])
    return deltas

def resolverlistas3(listax1,listay1):
    listay2 = []
    listay3 = []
    deltas = []
    valor = round((listay1[1]-listay1[0])/(listax1[1]-listax1[0]),6)
    listay2.append(valor)
    valor = round((listay1[2]-listay1[1])/(listax1[2]-listax1[1]),6)
    listay2.append(valor)
    valor = round((listay2[1]-listay2[0])/(listax1[2]-listax1[0]),6)
    listay3.append(valor)
    deltas.append(listay1[0])
    deltas.append(listay2[0])
    deltas.append(listay3[0])
    return deltas

def resolverlistas4(listax1,listay1):
    listay2 = []
    listay3 = []
    listay4 = []
    deltas = []
    valor = round((listay1[1]-listay1[0])/(listax1[1]-listax1[0]),6)
    listay2.append(valor)
    valor = round((listay1[2]-listay1[1])/(listax1[2]-listax1[1]),6)
    listay2.append(valor)
    valor = round((listay1[3]-listay1[2])/(listax1[3]-listax1[2]),6)
    listay2.append(valor)
    valor = round((listay2[1]-listay2[0])/(listax1[2]-listax1[0]),6)
    listay3.append(valor)
    valor = round((listay2[2]-listay2[1])/(listax1[3]-listax1[1]),6)
    listay3.append(valor)
    valor = round((listay3[1]-listay3[0])/(listax1[3]-listax1[0]),6)
    listay4.append(valor)
    deltas.append(listay1[0])
    deltas.append(listay2[0])
    deltas.append(listay3[0])
    deltas.append(listay4[0])
    return deltas

print(manejo_diferencias(x,y,t))
