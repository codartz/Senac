lista = []
frutas = ["maça", "banana", "uva"]
numeros = [1, 2, 3, 4]

# Acessanco elementos
print("Primeira fruta:", frutas[0])  # "maça"
print("Ultima fruta:", frutas[-1])   # "uva"

# Alterando elementos
frutas[1] = "banana-nanica"
print("Após alterar:", frutas)

# Adicionando elementos
frutas.append("morango")             # adiciona no final
frutas.insert(1, "pera")             # adiciona na posição 1
print("Após adicionar:", frutas)

# Removendo elementos
frutas.remove("uva")                 # remove pelo valor
última = frutas.pop()                # remove e retorna o ultimo
print("Após remover 'uva' e pop():", frutas, "Última removida:", última)