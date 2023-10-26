import csv

# Especifique o separador atual (vírgula) e o novo separador (ponto)
separador_atual = ','
novo_separador = '.'

# Abra o arquivo CSV de entrada e crie um arquivo de saída
with open('seu_arquivo.csv', 'r', newline='') as arquivo_entrada, open('arquivo_saida.csv', 'w', newline='') as arquivo_saida:
    leitor_csv = csv.reader(arquivo_entrada, delimiter=separador_atual)
    escritor_csv = csv.writer(arquivo_saida, delimiter=novo_separador)

    # Leia cada linha do arquivo de entrada, substitua as vírgulas por pontos e escreva no arquivo de saída
    for linha in leitor_csv:
        nova_linha = [valor.replace(separador_atual, novo_separador) for valor in linha]
        escritor_csv.writerow(nova_linha)

print("Conversão concluída. O arquivo de saída 'arquivo_saida.csv' agora tem pontos como separador.")
