import openpyxl

# Abra o arquivo Excel
workbook = openpyxl.load_workbook('seu_arquivo.xlsx')

# Selecione a planilha desejada (substitua 'Planilha1' pelo nome da sua planilha)
sheet = workbook['Planilha1']

# Itere pelas células da planilha e substitua vírgulas por pontos nas células que desejar
for row in sheet.iter_rows():
    for cell in row:
        if isinstance(cell.value, str) and ',' in cell.value:
            cell.value = cell.value.replace(',', '.')

# Salve o arquivo Excel de volta
workbook.save('arquivo_saida.xlsx')

print("Conversão concluída. O arquivo de saída 'arquivo_saida.xlsx' agora tem pontos como separador nas células desejadas.")
