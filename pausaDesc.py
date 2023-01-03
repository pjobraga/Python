import webbrowser
import time

intervalos = 2
contador = 0
print('O programa de controle de descanco foi iniciado')

while contador < intervalos:
    time.sleep(5)
    webbrowser.open(
        'https://open.spotify.com/track/33gwZOGJWEZ7dRWPqPxBEZ?si=f8f529ee598044e1')
    contador = contador + 1
