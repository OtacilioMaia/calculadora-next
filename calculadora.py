# Equpes de 4 pessoas, uma pessoa cria o branch develop, faz git push. 
# A partir de então a equipe se alinha qual função cada membro vai implementar
# Cada pessoa criará um branch com "feature/nome-da-operacao" e irá implementar a respectiva funcao
# Depois cada membro irá abrir um Pull Request para o branch develop 

numero_a = int(input("Digite o primeiro numero: "))
operacao = input("Digite a operacao (+, -, * ou /): ")
numero_b = int(input("Digite o segundo numero: "))

if operacao == "+":
    print(soma(numero_a, numero_b))
if operacao == "-":
    print(subtracao(numero_a, numero_b))
if operacao == "*":
    print(multiplicacao(numero_a, numero_b))
if operacao == "/":
    print(divisao(numero_a, numero_b))