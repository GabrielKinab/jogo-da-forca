import random

# Lista de frases relacionadas ao desenvolvimento de sistemas com suas respectivas dicas
frases_e_dicas = [
    ("PROGRAMACAO", "É a atividade de escrever códigos."),
    ("ALGORITMO", "Sequência de passos para resolver um problema."),
    ("DEBUG", "Processo de encontrar e corrigir erros."),
    ("COMPILADOR", "Transforma código em linguagem de máquina."),
    ("FRAMEWORK", "Conjunto de ferramentas e bibliotecas para desenvolvimento."),
    ("BANCODEDADOS", "Local onde as informações são armazenadas."),
    ("INTERFACE", "Ponto de interação entre componentes de software."),
    ("BACKEND", "Parte do sistema que funciona nos bastidores."),
    ("FRONTEND", "Parte do sistema que o usuário vê."),
    ("OBJETO", "Instância de uma classe em programação orientada a objetos."),
    ("VARIAVEL", "Armazena um valor que pode mudar durante a execução do programa."),
    ("FUNCAO", "Bloco de código que pode ser chamado para realizar uma tarefa."),
    ("CLASSE", "Modelo ou molde a partir do qual objetos são criados."),
    ("METODO", "Função que pertence a uma classe."),
    ("API", "Interface que permite a comunicação entre diferentes sistemas.")
]

# Boneco da forca para cada erro que der
boneco_forca = [
    """
    ____
    |  |
    |  
    | 
    | 
    | 
    """,
    """
    ____
    |  |
    |  O
    | 
    | 
    | 
    """,
    """
    ____
    |  |
    |  O
    |  |
    | 
    | 
    """,
    """
    ____
    |  |
    |  O
    | /|
    | 
    | 
    """,
    """
    ____
    |  |
    |  O
    | /|\\
    | 
    | 
    """,
    """
    ____
    |  |
    |  O
    | /|\\
    | / 
    | 
    """,
    """
    ____
    |  |
    |  O
    | /|\\
    | / \\
    | 
    """
]

# Escolher aleatoriamente uma frase e sua dica
frase, dica = random.choice(frases_e_dicas)
frase = frase.upper()  # É para ter certeza que a frase esteja em maiúsculo

# Começo do jogo
chances = 6
letras_acertadas = ["_" for _ in frase]  # Lista que guarda as letras certas e erradas
letras_erradas = []

# Início do jogo
print("Bem-vindo ao jogo da Forca!")
print("Dica:", dica)
print(boneco_forca[0])  # Exibe a forca inicial
print("Palavra:", " ".join(letras_acertadas))

# Loop do jogo
while chances > 0 and "_" in letras_acertadas:
    letra = input("Digite uma letra: ").upper()
    
    if len(letra) != 1 or not letra.isalpha():
        print("Entrada inválida! Por favor, digite apenas uma letra.")
        continue
    
    if letra in letras_acertadas or letra in letras_erradas:
        print("Você já tentou essa letra. Tente outra.")
        continue

    if letra in frase:
        print("Você acertou uma letra!")
        for i, l in enumerate(frase):
            if l == letra:
                letras_acertadas[i] = letra
    else:
        print("Letra errada!")
        chances -= 1
        letras_erradas.append(letra)
    
    print(boneco_forca[6 - chances])  # Exibe o estágio atual da forca
    print("Palavra:", " ".join(letras_acertadas))
    print(f"Chances restantes: {chances}")
    print(f"Letras erradas: {', '.join(letras_erradas)}")

# Fim do jogo
if "_" not in letras_acertadas:
    print("Parabéns você conseguiu completar a palavra da forca!")
else:
    print("VOCÊ MORREU")
