# Sistema de Banco

def main():
    print("Banco Itaú")
    print("")
    nome = input("Digite seu nome: ")
    print("--------------------")
    print("Selecione uma opção:")
    print("--------------------")
    print("[1] Saldo")
    print("[2] Extrato (Últimos 5 dias)")
    print("[3] Empréstimos")
    print("--------------------")

    opcao = int(input())

    while opcao > 3 or opcao < 1:
        print("")
        print("Opção Inválida!")
        print("------------------------")
        print("Digite uma opção válida.")
        print("------------------------")
        opcao = int(input())

    match opcao:
        case 1:
            print("\n" * 25)  # Simula a função limpatela
            print("Seu saldo é: R$1.000,00")
        case 2:
            print("\n" * 25)  # Simula a função limpatela
            print("Pagamento de R$18,00 realizado - Cafeteria J&J (Via Pix)")
            print("Pagamento de R$26,00 realizado - Uber (Via Pix)")
            print("Pagamento de R$484,00 realizado - Supermercado Semar (Via Cartão)")
        case 3:
            print("\n" * 25)  # Simula a função limpatela
            print("Procure a sua agência para a liberação de empréstimos.")

if __name__ == "__main__":
    main()
