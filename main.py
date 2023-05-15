idade = input("Digite um número: ")
idade = int(idade)

if idade < 0:
    print("Impossível!")

elif idade > 0 and idade < 18:
    print("Não precisa se alistar.")

elif idade == 18:
    print("Eita!")

elif idade > 18 and idade < 65:
    print("Não esqueça de votar na próxima eleição. ")

elif idade > 65:
    print("Vá descansar.")
else:
    print("Eita!")
    