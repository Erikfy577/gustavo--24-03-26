#Contagem Regressiva: Imprima os números de 10 a 0, com uma pausa de 1 segundo(use a biblioteca time), terminando com "FOGO!".
import time
for c in range(10, -1, -1):
    print(c)
    time.sleep(1)
print("FOGO!")