# fazer tratamento para separador numerico estilo anglo-saxão (Estados Unidos)




import pandas as pd
import locale
from datetime import datetime

# Configurar a formatação contábil para o local desejado (Brasil)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Ler o arquivo CSV
df = pd.read_csv(r'nota\notas_fiscais.csv', sep=';')

# Obter o mês atual
mes_atual = datetime.now().strftime("%b")

# Especificar a coluna que deseja converter e formatar
coluna_a_converter = 'valor do frete'  # Nome da coluna que deseja converter e formatar

# Limpar e formatar os valores monetários
df[coluna_a_converter] = df[coluna_a_converter].str.replace('R$', '').str.replace('.', '').str.replace(',', '.').astype(float)

# Formatar a coluna no estilo contábil
df[coluna_a_converter] = df[coluna_a_converter].apply(lambda x: locale.currency(x, symbol=True, grouping=True))

# Salvar o DataFrame de volta em um novo arquivo CSV com o nome incluindo o mês atual
nome_do_arquivo = f'TMS_{mes_atual}.csv'
df.to_csv(nome_do_arquivo, sep=';', index=False)
