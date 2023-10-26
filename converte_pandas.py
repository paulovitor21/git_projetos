import pandas as pd

# Leia o arquivo CSV
df = pd.read_csv('seu_arquivo.csv')

# Especifique as colunas que deseja converter de vírgula para ponto
colunas_a_converter = ['coluna1', 'coluna2', 'coluna3']  # Substitua pelos nomes das suas colunas

# Realize a conversão nas colunas especificadas
df[colunas_a_converter] = df[colunas_a_converter].apply(lambda x: x.str.replace(',', '.'))

# Salve o DataFrame de volta em um arquivo CSV
df.to_csv('arquivo_saida.csv', index=False, sep=';')  # Substitua pelo novo separador desejado, se necessário

print("Conversão concluída. O arquivo de saída 'arquivo_saida.csv' agora tem pontos como separador nas colunas especificadas.")
