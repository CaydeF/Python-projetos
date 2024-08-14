def contar_caracteres(frase):
    # Inicializa um dicionário vazio para armazenar as contagens
    contagem = {}

    # Itera sobre cada caractere na frase
    for caractere in frase:
        # Se o caractere já está no dicionário, incrementa sua contagem
        if caractere in contagem:
            contagem[caractere] += 1
        # Caso contrário, adiciona o caractere ao dicionário com contagem 1
        else:
            contagem[caractere] = 1

    return contagem


# Solicita ao usuário que insira uma frase
frase = input("Digite uma frase: ")

# Conta os caracteres na frase
resultado = contar_caracteres(frase)

# Exibe o dicionário com a contagem de caracteres
print("Contagem de caracteres:")
for caractere, quantidade in resultado.items():
    print(f"'{caractere}': {quantidade}")
