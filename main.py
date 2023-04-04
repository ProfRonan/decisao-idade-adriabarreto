idade = input("Digite um número: ")
idade = int(idade)

if idade < 0:
    print("impossível!")

elif idade > 0 and idade < 18:
    print("não precisa se alistar.")

elif idade == 18:
    print("eita!")

elif idade > 18 and idade < 65:
    print("não esqueça de votar na próxima eleição. ")

elif idade > 65:
    print("Vá descansar.")
else:
    print("eita!")
    