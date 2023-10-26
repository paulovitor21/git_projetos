import os

pasta_destino = 'caminho/para/sua/pasta'  # Substitua pelo caminho da pasta onde os arquivos são baixados

# Liste os arquivos na pasta de destino e obtenha o arquivo mais recente
arquivos_na_pasta = os.listdir(pasta_destino)
arquivos_na_pasta = [os.path.join(pasta_destino, arquivo) for arquivo in arquivos_na_pasta]
arquivos_na_pasta = [arquivo for arquivo in arquivos_na_pasta if os.path.isfile(arquivo)]
arquivo_mais_recente = max(arquivos_na_pasta, key=os.path.getmtime)

# Agora você tem o nome do arquivo mais recente, pode renomeá-lo
novo_nome = 'novo_nome.csv'  # Substitua pelo novo nome desejado

# Renomeie o arquivo
os.rename(arquivo_mais_recente, os.path.join(pasta_destino, novo_nome))
print(f"O arquivo mais recente foi renomeado para '{novo_nome}'.")
