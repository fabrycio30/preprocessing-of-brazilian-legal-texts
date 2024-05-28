import pandas as pd

#p1 = pd.read_csv("/projetos/ctcca/nlp/data/all-data/p1.csv")
#p2 = pd.read_csv("/projetos/ctcca/nlp/data/all-data/p2.csv")
#p3 = pd.read_csv("/projetos/ctcca/nlp/data/all-data/p3.csv")
#p4 = pd.read_csv("/projetos/ctcca/nlp/data/all-data/p4.csv")
#p5 = pd.read_csv("/projetos/ctcca/nlp/data/all-data/p5.csv")
#p6 = pd.read_csv("/projetos/ctcca/nlp/data/all-data/p6.csv")

#df_jur = pd.DataFrame()

#df_jur['text'] = pd.concat([p1.text,p2.text,p3.text,p4.text,p5.text,p6.text], ignore_index=True, sort=False)

#df_jur.to_csv('/projetos/ctcca/nlp/data/all-data/alldata.csv', index=False)


# Carregue os arquivos .csv
print('p1 carregando!')
p1 = pd.read_csv(r"C:\Users\fabry\Documents\data\p1.csv")
print('p1 carregado!')
print('p2 carregando!')
p2 = pd.read_csv(r"C:\Users\fabry\Documents\data\p2.csv")
print('p2 carregado!')
print('p3 carregando!')
p3 = pd.read_csv(r"C:\Users\fabry\Documents\data\p3.csv")
print('p3 carregado!')
print('p4 carregando!')
p4 = pd.read_csv(r"C:\Users\fabry\Documents\data\p4.csv")
print('p4 carregado!')
print('p5 carregando!')
p5 = pd.read_csv(r"C:\Users\fabry\Documents\data\p5.csv")
print('p5 carregado!')
print('p6 carregando!')
p6 = pd.read_csv(r"C:\Users\fabry\Documents\data\p6.csv")
print('p6 carregado!')
# Concatene as colunas 'text' de todos os dataframes
df_jur = pd.concat([p1['text'], p2['text'], p3['text'], p4['text'], p5['text'], p6['text']], ignore_index=True)

# Salve os textos em um arquivo .txt
with open(r"C:\Users\fabry\Documents\data\alldata.txt", 'w', encoding='utf-8') as arquivo_txt:
    for texto in df_jur:
        arquivo_txt.write(texto + '\n')

print("Arquivo 'alldata.txt' criado com sucesso!")

