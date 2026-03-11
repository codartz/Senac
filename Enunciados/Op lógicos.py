# Exercícios com operadores lógicos
# Os exercícios serão para validar uma condição, então, o que ficar dentro dos parenteses em print(CONDICAO) precisa ser verdade pro resultado ser exibido na tela. 
# O resultado sempre será TRUE ou FALSE

# Exemplo 1 
# Número POSITIVO e maior que 10
n = float(input("Número: "))
print(n > 0 and n > 10)

1) # Idade entre 18 e 30
2) # Pelo menos um número maior que 50
3) # Número NÃO é zero
4) # Senha correta
5) # Ambos os números são pares
6) # Não é menor de idade (usar not)
7) # temperatura fora da faixa 20-30 graus
8) # Número negativo ou maior que 100
9) # Primeiro > 10 e segundo < 5

# Respostas

# Idade entre 18 e 30

idade = int(input("Digite a idade: "))
print(18 <= idade <= 30)

# Pelo menos um número maior que 50

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
print((a > 50) or (b > 50))

# Número NÃO é zero

n = float(input("Digite um número: "))
print(n != 0)


# Senha correta

senha_definida = "Python123"  # você pode trocarsenha
senha_digitada = input("Digite a senha: ")
print(senha_definida == senha_digitada)


# Ambos os números são pares
 
x = int(input("Digite o primeiro inteiro: "))
y = int(input("Digite o segundo inteiro: "))
print((x % 2 == 0) and (y % 2 == 0))

# Não é menor de idade (usar not)

# Afirmativa: “é menor de idade”. Se quiser a lógica inversa, troque o print por print(not (idade < 18)).

idade = float(input("Digite sua idade: "))
print(idade < 18)           # True se menor de idade

# print(not (idade >= 18))  # alternativa equivalente usando NOT


#temperatura fora da faixa 20-30 graus

t = float(input("Digite a temperatura (°C): "))
print((t < 20) or (t > 30))

#Número negativo ou maior que 100

n = float(input("Digite um número: "))
print((n < 0) or (n > 100))

# Primeiro > 10 e segundo < 5

a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))
print((a > 10) and (b < 5))