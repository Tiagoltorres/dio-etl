# Importação das bibliotecas que serão utilizadas
import yfinance as yf
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Definição das ações e transformação do arquivo baixado em um DataFrame
ticker=(input("Digite o código da ação, Por exemplo:PETR4.SA:\n"))
if not ticker.endswith(".SA"):
            ticker += ".SA"

data = yf.download(ticker, start='2022-10-01', end='2023-10-01')
df = pd.DataFrame(data)

df = pd.DataFrame(data)
# Criando a coluna Date que não tem no df original
df.reset_index(inplace=True)
df: object = df.rename(columns={"Date": "Date"})

# Digitação do valor de investimento que vai servir tanto para poupança qto ações
valor_inicial = float(input("Quanto você quer investir? "))

# Definição da função para retornar o investimento e retorno das ações
def calcular_investimento_acao(valor_inicial):
    valor_atual = valor_inicial  # Inicializa o valor atual
    cotas_ações_iniciais = valor_inicial / df["Close"].iloc[0]

    datas = []
    valores_investimento = []
# Iteração para definição mensal das ações, visto que o valor é mensal
    for data_mensal in df['Date'].dt.to_period('M').unique():
        df_mensal = df[df['Date'].dt.to_period('M') == data_mensal]
        preço_final = df_mensal["Close"].iloc[-1]

        valor_atual = cotas_ações_iniciais * preço_final

        datas.append(data_mensal.to_timestamp())
        valores_investimento.append(valor_atual)
# Criação do df de invehstimento baseado no retorno das ações
    df_investimento = pd.DataFrame({"Data Mensal": datas, "Valor do Investimento Ação": valores_investimento})
    return df_investimento
# Função para calcular o rendimento da poupança no período de 01 ano
def calcular_rendimento_poupanca(valor_inicial, taxas_mensais):
    rendimentos_mensais = []
    valor_atual = valor_inicial
#iteração para o calculo de taxas mensais
    for taxa_mensal in taxas_mensais:
        rendimento_mensal = valor_atual * (taxa_mensal / 100)
        valor_atual += rendimento_mensal
        rendimentos_mensais.append(valor_atual)

    return rendimentos_mensais

# Taxas de juros da poupança no período de outubro de 2022 a setembro de 2023
taxas_mensais = [0.65, 0.65, 0.71, 0.71, 0.58, 0.74, 0.61, 0.65, 0.65, 0.72, 0.68, 0.62]  # Exemplo de taxas mensais (em porcentagem)

df_acao = calcular_investimento_acao(valor_inicial)
rendimentos_poupanca = calcular_rendimento_poupanca(valor_inicial, taxas_mensais)

# Criar um DataFrame com os rendimentos da poupança
df_poupanca = pd.DataFrame({
    "Data Mensal": df_acao["Data Mensal"],
    "Rendimento Poupança": rendimentos_poupanca
})

# Criar um df combinado que para comparar os investimentos mensais da poupança e ações
df_combinado = pd.merge(df_acao, df_poupanca, on="Data Mensal")
df_combinado.to_excel("investimento_resultado.xlsx", index=False)

# Criação do gráfico de linha comparando as ações e poupança
plt.figure(figsize=(12, 6))
plt.plot(df_combinado["Data Mensal"], df_combinado["Valor do Investimento Ação"], label="Retorno da Ação", marker='o')
plt.plot(df_combinado["Data Mensal"], df_combinado["Rendimento Poupança"], label="Retorno da Poupança", marker='o')
plt.xlabel("Data Mensal")
plt.ylabel("Valor do Investimento")
plt.title("Comparação do Retorno da Ação com a Poupança")
plt.legend()
plt.grid(True)
#Salvando o gráfico em png para consulta
plt.savefig("investimento_plt.png")

plt.show()



