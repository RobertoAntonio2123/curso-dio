# agora vamos solicitar uma string e um numeor inteiro com entrada . depois teremos
'''
# Pede os dados para o usuário digitar uma string e um número inteiro
string=input("Digite uma string: ")
numero=int(input("Digite um numero inteiro: "))
escrever o que o usuario digitou multiplicando 
a string pelo numero inteiro usando o operador de multiplicação *

print((string+ ' ') * numero)

'''

# Abre um loop para o programa continuar rodando até dar certo
while True:
    try:
        # 1. Solicita a string e limpa espaços extras nas pontas
        texto = input("Digite uma string: ").strip()

        # Validação: não deixa o texto ficar em branco
        if texto == "":
            raise ValueError("O texto não pode ficar em branco!")

        # 2. Solicita o número inteiro
        # Se o usuário digitar letras aqui, o int() vai disparar um erro automaticamente
        numero = int(input("Digite um número inteiro: "))

        # Validação: o número não pode ser menor ou igual a zero
        if numero <= 0:
            raise ValueError("O número precisa ser maior que zero!")

        # 3. Processa e multiplica a string de forma otimizada
        # Adicionamos o espaço depois do texto e multiplicamos pelo número
        resultado_final = (texto + " ") * numero

        # 4. Mostra o resultado final tirando o último espaço que sobrou na ponta
        print("\n--- Resultado Final ---")
        print(resultado_final.strip())
        print("-----------------------")

        # Se chegou até aqui sem erros, encerra o programa
        break

    except ValueError as erro:
        # Se o erro foi por causa de letras no lugar do número, personalizamos a mensagem
        if "invalid literal for int()" in str(erro):
            print("\n Erro: Você precisa digitar um número inteiro válido (ex: 5, 10, 2).\n")
        else:
            # Mostra as outras mensagens que criamos (campo em branco ou número negativo)
            print(f"\n Erro: {erro} Tente novamente.\n")
