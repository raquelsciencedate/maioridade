# Entrada de dados
nome = input('Informe seu nome: ')
idade = int(input('Informe sua idade: '))

# Verifica a idade do usuário
# (operador ternário)
print(f"{nome} é maior de idade." if idade > 18 else f"{nome} é menor de idade.")