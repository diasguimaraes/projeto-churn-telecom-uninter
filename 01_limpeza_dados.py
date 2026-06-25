import pandas as pd
import numpy as np

print("--- Semana 1: Executando a Limpeza dos Dados (Data Wrangling) ---")

# 1. Carregar a base de dados
df = pd.read_csv("data/telco_customer_churn.csv")

# 2. Corrigir os espaços em branco na coluna TotalCharges substituindo por 0
print("\nSubstituindo espaços em branco por '0'...")
df['TotalCharges'] = df['TotalCharges'].replace(' ', '0')

# 3. Converter a coluna de texto para numérico (float)
print("Convertendo a coluna TotalCharges para o tipo numérico...")
df['TotalCharges'] = pd.to_numeric(df['TotalCharges'])

# 4. Verificação de Segurança
print("\n--- Verificação após a Limpeza ---")
media_total = df['TotalCharges'].mean()
print(f"Média das cobranças totais calculada com sucesso: R$ {media_total:.2f}")

# 5. Salvar a base de dados limpa por cima da antiga
df.to_csv("data/telco_customer_churn.csv", index=False)
print("\n✅ Base de dados limpa e salva com sucesso!")
