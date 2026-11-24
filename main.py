import random
name = input("Hola, Bienvenido a mi juego de adivinanzas, cual es tu nombre?\n")

print("Buena Suerte !", name ,"la vas a necesitar")

words = ['Perro','Gato','Loro','Elefante','Leon','Tigre','Venado','Guepardo','Rata','Leandro']

word = random.choice (words)

print("Adivina la palabra")

guesses = ""

turns = 12

while turns > 0:

    failed = 0

    for char in word:
        if char in guesses:
            print(char, end=" ")
        else:
            print("_", end="")
            failed += 1
    print()
    if failed == 0:
        print("Ganaste" , name , "Bien Hecho")
        print("La Palabra es:", word)
        break
    guess = input("Adivina un caracter:")

    if len(guess) != 1:
        print("Por favor introduce un solo caracter")
        continue
    guesses += guess

    if guess not in word:
        turns -= 1
        print("Mal, prueba con otra letra mayuscula o minuscula")
        print("Tienes", turns, "turnos restantes")

        if turns == 0:
            print("Perdiste!")
            print("La palabra era:", word)