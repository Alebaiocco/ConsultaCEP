import requests

print('####################')
print('## CONSULTAS CEP ###')
print('####################')

def main():
    cep_input = input("Digite o CEP para a consulta : ")

    if len(cep_input) != 8:
        print("Quantidade de digitos inválida!")
        print("Tente novamente")
        main()

    request = requests.get("https://viacep.com.br/ws/{}/json/".format(cep_input))

    adress_data = request.json()

    if "erro" not in adress_data:
        print(" ==> CEP ENCONTRADO <==")
        
        print("CEP : {}".format(adress_data['cep']))
        print("Logradouro : {}".format(adress_data['logradouro']))
        print("Bairro : {}".format(adress_data['bairro']))
        print("Cidade : {}".format(adress_data['localidade']))
        print("Estado : {}".format(adress_data['uf']))
        
    else:
        print("CEP inválido")
        
        
    option = int(input("Deseja realizar uma nova consulta? \n 1. Sim\n 2. Sair\n"))

    if option == 1:
        main()
        
    else:
        print("Finalizado")
        exit()
        
if __name__ == "__main__":
    main()