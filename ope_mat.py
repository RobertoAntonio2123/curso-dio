# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.
"""


# Pede o primeiro número, transforma o texto digitado em número decimal (float) e guarda na variável 'numero1'
numero1 = float(input("Digite o primeiro número: "))

# Pede o segundo número, também transforma em decimal e guarda na variável 'numero2'
numero2 = float(input("Digite o segundo número: "))

# Pede para o usuário escolher o símbolo da conta e guarda o texto na variável 'operacao'
operacao = input("Digite a operação que deseja realizar (+, -, *, /): ")

# SE a operação escolhida for o símbolo de mais (+)
if operacao == "+":
    resultado = numero1 + numero2  # Soma os dois números e guarda o total

# SENÃO, SE a operação escolhida for o símbolo de menos (-)
elif operacao == "-":
    resultado = numero1 - numero2  # Subtrai o segundo número do primeiro

# SENÃO, SE a operação escolhida for o símbolo de vezes (*)
elif operacao == "*":
    resultado = numero1 * numero2  # Multiplica os dois números

# SENÃO, SE a operação escolhida for o símbolo de dividir (/)
elif operacao == "/":
    resultado = numero1 / numero2  # Divide o primeiro número pelo segundo

# SENÃO (se o usuário digitou qualquer outra coisa diferente de +, -, * ou /)
else:
    print("Operação inválida!")  # Mostra um aviso de erro na tela
    resultado = None  # Define o resultado como 'None' (vazio/nada) para indicar que a conta falhou

# SE o resultado NÃO for vazio (ou seja, se a conta acima deu certo e gerou um número)
if resultado is not None:
    # Mostra a mensagem na tela exibindo o valor final formatado dentro do texto
    print(f"O resultado da operação é: {resultado}")


"""
    
while True:
    try:
        # 1. Entrada dos números com tratamento contra letras
        numero1 = float(input("Digite o primeiro número: "))
        numero2 = float(input("Digite o segundo número: "))
        
        # 2. Entrada da operação
        operacao = input("Digite a operação que deseja realizar (+, -, *, /): ").strip()

        # 3. Processamento das operações matemáticas
        if operacao == "+":
            resultado = numero1 + numero2
        elif operacao == "-":
            resultado = numero1 - numero2
        elif operacao == "*":
            resultado = numero1 * numero2
        elif operacao == "/":
            # Validação importante: impede a divisão por zero
            if numero2 == 0:
                raise ZeroDivisionError("Não é possível dividir um número por zero!")
            resultado = numero1 / numero2
        else:
            # Se a operação não for válida, gera um erro para ir ao bloco except
            raise ValueError("Operação inválida! Escolha apenas +, -, * ou /.")

        # 4. Exibe o resultado e fecha o programa se tudo deu certo
        print(f"\n O resultado da operação é: {resultado}\n")
        break

    except ValueError as erro:
        # Trata letras no input de número ou operação inválida
        if "could not convert string to float" in str(erro):
            print("\n Erro: Você precisa digitar números válidos (use ponto para decimais, ex: 5.5).\n")
        else:
            print(f"\n Erro: {erro}\n")
            
    except ZeroDivisionError as erro:
        # Trata especificamente a divisão por zero
        print(f"\n Erro: {erro} Tente com outros números.\n")
