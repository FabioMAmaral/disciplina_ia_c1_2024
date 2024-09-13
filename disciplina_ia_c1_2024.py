import pandas as pd

# Carregar o CSV
df = pd.read_csv('https://raw.githubusercontent.com/FabioMAmaral/disciplina_ia_c1_2024/main/urls_phishing_checkpoint1.csv')

amostra_df = df.sample(4000, random_state=101)

# Dividir o DataFrame em dois subconjuntos
df1 = amostra_df[df['phishing'] == 1]  # phishing
df0 = amostra_df[df['phishing'] == 0]  # legítima

# Média de todas as observações da base
mean_value = round(df['length_url'].mean(), 2)
print(f"A média da coluna 'length_url' é: {mean_value} (Todas URLs)")

# Média das URLs - Phishing
mean_value1 = round(df1['length_url'].mean(), 2)
print(f"{mean_value1} (URLs Phishing)")

# Média das URLs - Legítima
mean_value0 = round(df0['length_url'].mean(), 2)
print(f"{mean_value0} (URLs Legítima)")

# Mediana de todas as observações da base
median_value = df['length_url'].median()
print(f"A mediana da coluna 'length_url' é: {median_value} (Todas URLs)")

# Mediana das URLs - Phishing
median_value1 = df1['length_url'].median()
print(f"{median_value1} (URLs Phishing)")

# Mediana das URLs - Legítima
median_value0 = df0['length_url'].median()
print(f"{median_value0} (URLs Legítima)")

# Desvio padrão de todas as observações da base
std_value = round(df['length_url'].std(), 2)
print(f"O desvio padrão da coluna 'length_url' é: {std_value} (Todas URLs)")

# Desvio padrão das URLs - Phishing
std_value1 = round(df1['length_url'].std(), 2)
print(f"{std_value1}(URLs Phishing)")

# Desvio padrão das URLs - Legítima
std_value0 = round(df0['length_url'].std(), 2)
print(f"{std_value0} (URLs Legítima)")
