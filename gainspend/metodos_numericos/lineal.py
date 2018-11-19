x = [2,4]
y = [.69314718,1.386294361]
t = 3

def controllineal(listax,listay,valor):
    respuesta = ((listay[1]-listay[0])/(listax[1]-listax[0]))*(valor-listax[0])+listay[0]
    return respuesta

print(controllineal(x,y,t))
