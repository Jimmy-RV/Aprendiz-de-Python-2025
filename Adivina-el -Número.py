import random

def adivina_el_numero():
    print("¡Bienvenido a 'Adivina el Número'!")
    print("He pensado en un número entre 1 y 100. ¡A ver si puedes adivinarlo!")
    
    numero_secreto = random.randint(1, 100)
    intentos = 0
    adivinado = False
    
    while not adivinado:
        try:
            guess = int(input("Introduce tu suposición: "))
            intentos += 1
            
            if guess < numero_secreto:
                print("El número es mayor. ¡Sigue intentando!")
            elif guess > numero_secreto:
                print("El número es menor. ¡Sigue intentando!")
            else:
                adivinado = True
                print(f"¡Felicidades! ¡Has adivinado el número en {intentos} intentos!")
        except ValueError:
            print("Por favor, introduce un número válido.")
    
    print("¡Gracias por jugar!")

if __name__ == "__main__":
    adivina_el_numero()