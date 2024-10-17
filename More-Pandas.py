import pandas as pd
url = 'https://gist.github.com/armgilles/194bcff35001e7eb53a2a8b441e8b2c6'
df = pd.read_html(url)[0]
df["Atb. Fisicos"]= df["Attack"]+df["Defense"]
df["Atb. Especiais"]= df["Sp. Atk"] + df["Sp. Def"]
df["Media de Atributos"]= (df["Atb. Especiais"]+df["Atb. Fisicos"]+df["Speed"]+df["HP"])/6
df = df.sort_values(by = 'Media de Atributos', ascending= True)
df.rename(columns={'HP':'Vida'}, inplace=True)
df.rename(columns={'Speed':'Velocidade'}, inplace=True)
df.drop(columns={'Attack','Defense','Sp. Atk', 'Sp. Def'})
tamanho = df.shape[0]
df.iloc[tamanho - int(tamanho/4) : tamanho]
