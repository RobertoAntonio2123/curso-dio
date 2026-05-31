#vamos receber dois dados diferentes do usuario e concatena-los em um unico stringl

# Exemplo do codigo que foi usando na aula para concatenar


"""

# Pede os dados para o usuário
info1 = input("Digite o primeiro resultado: ")

info2 = input("Digite o segundo resultado: ")
# junta os textos usando 
info_concatenada = info1 + " " + info2

print("as informações concatenadas são: " + info_concatenada)

"""
"""
 Abre um loop infinito para o programa não fechar se houver erro
 esse codigo é para garantir que o usuário digite algo 
 e não deixe em branco, caso contrário, o programa vai pedir 
 para ele tentar de novoa assim melhorando o codigo mostrado na aula.

   
"""

while True:
    try:
        # Pede os dados para o usuário e remove espaços vazios com o .strip()
        resultado1 = input("Digite o primeiro resultado: ").strip()
        resultado2 = input("Digite o segundo resultado: ").strip()

        # Verifica se o usuário deixou algum campo em branco
        if resultado1 == "" or resultado2 == "":
            # Cria um erro proposital para ir direto para o bloco 'except'
            raise ValueError("Você não pode deixar nenhum campo em branco!")

        # Se tudo estiver correto, junta os textos usando f-string
        resultado_final = f"{resultado1}{resultado2}"

        # Mostra o resultado na tela
        print("\n--- Resultados Juntados com Sucesso! ---")
        print(resultado_final)
        print("---------------------------------------")

        # Fecha o loop e encerra o programa já que deu tudo certo
        break

    except ValueError as erro:
        # Mostra a mensagem de erro na tela e o loop 'while' recomeça
        print(f"\n Erro: {erro} Por favor, tente de novo.\n")
