Solicite ao usuário que informe o saldo da sua conta e o valor que será depositado; ambos os valores devem ser do tipo FLOAT. Utilize atribuição += para adicionar o deposito ao saldo da conta e exiba o novo saldo na tela. 

saldo = float(input("Informe o saldo da sua conta: "))
deposito = float(input("Informe o valor que será depositado: "))

saldo += deposito         # acrescenta o depósito ao saldo
print(f"Novo saldo: {saldo:.2f}")