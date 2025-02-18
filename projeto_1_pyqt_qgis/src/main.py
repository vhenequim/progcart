import polars as pl


data = {
    "nome": ["João", "Maria", "Pedro", "Ana", "Carlos"],
    "idade": [25, 30, 35, 40, 45],
    "cidade": ["São Paulo", "Rio de Janeiro", "Brasília", "Salvador", "Fortaleza"]
}

df = pl.DataFrame(data)



print(df.melt())


