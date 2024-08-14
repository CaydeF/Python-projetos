import re
from datetime import datetime

# Função para converter a data para o formato por extenso
def data_por_extenso(dia, mes, ano):
    meses = [
        "Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho",
        "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"
    ]
    
    return f"{dia} de {meses[mes - 1]} de {ano}"

# Função para validar e ler a data
def ler_data():
    while True:
        data_str = input("Digite a data no formato DD/MM/AAAA: ")
        if re.match(r'^\d{2}/\d{2}/\d{4}$', data_str):
            try:
                dia, mes, ano = map(int, data_str.split('/'))
                datetime(ano, mes, dia)  # Isso vai levantar um ValueError se a data for inválida
                return dia, mes, ano
            except ValueError:
                print("Data inválida. Por favor, digite uma data válida.")
        else:
            print("Formato inválido. Por favor, digite a data no formato DD/MM/AAAA.")

# Função para salvar datas convertidas em um arquivo
def salvar_datas_em_arquivo(datas_convertidas, arquivo='datas_convertidas.txt'):
    with open(arquivo, 'a') as file:
        for data in datas_convertidas:
            file.write(data + '\n')

# Função principal com o menu de opções
def main():
    datas_convertidas = []
    
    while True:
        print("\nMenu:")
        print("1 – Converter Data")
        print("2 – Listar Datas por extenso")
        print("3 – Sair")
        
        escolha = input("Escolha uma opção: ")
        
        if escolha == '1':
            dia, mes, ano = ler_data()
            data_extenso = data_por_extenso(dia, mes, ano)
            print(f"Data por extenso: {data_extenso}")
            datas_convertidas.append(data_extenso)
            salvar_datas_em_arquivo([data_extenso])
        
        elif escolha == '2':
            if datas_convertidas:
                print("\nDatas convertidas por extenso:")
                for data in datas_convertidas:
                    print(data)
            else:
                print("Nenhuma data convertida ainda.")
        
        elif escolha == '3':
            print("Saindo do programa...")
            break
        
        else:
            print("Opção inválida. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    main()
