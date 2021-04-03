from time import sleep
from threading import Thread
def car(velocidade, piloto):
    trajeto = 0
    colocação = 0

    while trajeto <= 100:
        print(f'piloto: {piloto};\nKM: {trajeto} \n')
        trajeto += velocidade
        sleep(0.5)
        if trajeto >= 100:
            colocação += 1
            print(f'Parabéns {piloto} chegou em: {colocação}º lugar!!')
            break
        if colocação > 1:
            print(f'Não foi o primeiro, mas chegou em {colocação}º lugar!')
            break
t_c1 = Thread(target=car, args=[5, 'André'])
t_c2 = Thread(target=car, args=[10, 'José'])

t_c1.start()
t_c2.start()