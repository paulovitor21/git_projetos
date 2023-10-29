# fazer tratamento para separador numerico estilo anglo-saxão (Estados Unidos)

import pandas as pd
import locale
from datetime import datetime

# Configurar a formatação contábil para o local desejado (EUA)
#locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')

# Configurar a formatação contábil para o local desejado (Brasil)
locale.setlocale(locale.LC_ALL, 'pt_BR.UTF-8')

# Ler o arquivo CSV
df = pd.read_csv(r'nota\notas_fiscais.csv', sep=';')

# Obter o mês vigente
#mes_vigente = datetime.now().strftime("%B")

# Obter o mês atual
mes_atual = datetime.now().strftime("%b")

# Especificar a coluna que deseja converter
coluna_a_converter = 'valor do frete'  # Nome da coluna que deseja converter

# Aplicar a conversão para o formato anglo-saxão
#df[coluna_a_converter] = df[coluna_a_converter].str.replace('.', '').str.replace(',', '.')

# Aplicar o separador brasileiro no estilo contábil
df[coluna_a_converter] = df[coluna_a_converter].str.replace('.', '').str.replace(',', '.')

# Converter a coluna para tipo numérico
df[coluna_a_converter] = pd.to_numeric(df[coluna_a_converter], errors='coerce')

# Especificar a coluna que deseja formatar
coluna_a_formatar = 'valor do frete'  # Nome da coluna que deseja formatar

# Formatar a coluna no estilo contábil
df[coluna_a_formatar] = df[coluna_a_formatar].apply(lambda x: locale.currency(x, symbol=True, grouping=True))

# Salvar o DataFrame de volta em um novo arquivo CSV com o nome incluindo o mês vigente
nome_do_arquivo = f'TMS_{mes_atual}.csv'
df.to_csv(nome_do_arquivo, index=False)


