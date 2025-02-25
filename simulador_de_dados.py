import random

def lanzar_dado():
    return random.randint(1, 6)

print("¡Simulador de Dados!")

while True:
    input("Presiona Enter para lanzar el dado...")
    resultado = lanzar_dado()
    print(f"El dado cayó en: {resultado}")

    jugar_de_nuevo = input("¿Lanzar de nuevo? (s/n): ").lower()
    if jugar_de_nuevo != 's':
        break