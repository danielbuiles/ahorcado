import sys
import time
import requests
from dibujos import dib

def palabra():
    url = "https://palabras-aleatorias-public-api.herokuapp.com/random"
    response = requests.request("GET", url).json()
    return response["body"]["Word"]

def juego():
    v=5
    p=palabra().lower()
    pl="_"*len(p)
    while(v>0):
        if p==pl:
            print("Felizidades ganador.")
            break;
        res=input(f"palabra oculta: {pl} Escribe Tu letra:\n").lower()
        if len(res)!=1 or type(res)!=str:
            print("\n entrada de dato INVALIDA, intenta de nuevo\n")
        else:
            if res in p:
                indx=[]
                for i,l in enumerate(p):
                    if l==res:
                        indx.append(i)
                for i in indx:
                    pl=pl[:i]+res+pl[i+1:]
            else:
                print(dib[v])
                v-=1
                print(f"la letra {res} no esta, Vidas={v}")
    if pl!=p:
        print(f"has perdido la palabra era: {p}\n")
    repetir()
    
def repetir():
    res=input("quieres volver a jugar? s:si n:no \n")
    if res=="n":
        print("Gracias por jugar")
        sys.exit()
    elif res=="s":
        juego()
    else:
        repetir()

def main():
    print("Hola bienvenido al Ahoracado por CmdData.\n")
    nombre=input("ingrese su nombre: ")
    print(f"Hola {nombre}! Mucha suerte!")
    time.sleep(1)
    print("el juego esta a punto de empezar!")
    print(" Vamos a jugar Ahorcado\n")
    time.sleep(3)
    juego()
    
if __name__ == '__main__':
    main()