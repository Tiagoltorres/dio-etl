# dio-etl
Trabalho de Etl utilizando o Python, usando a biblioteca yfinance para baixar dados  de ações
Neste arquivo, foi feita a importação das bilbiotecas:
Pandas, Yfinance, Matplotlib.

O Objetivo deste trabalho é utilizar as ferramentas de ETL, com extração dos dados da biblioteca yfinance, com uma determinada ação que pode ser escolhida pelo usuário.

Depois a transformação dos dados em um DF e limpeza para utilizar apenas a coluna do fechamento do pregão no período de 01 ano e comparar os valores dos fechamentos mensais com a renda da poupança.

Neste script, o usuário tem a liberdade de escolher qual ação listada ele pode comparar. Como no yfinance é obrigatório colocar a terminação .SA, foi implantado uma condição de auto-preencher caso o usuário esqueça, para não ocorrer erro no programa.

As saídas que são as partes de carregamento, vai gerar uma planilha comparando com os valores que o usuário investiu e o retorno de ações e poupança, e um gráfico de linha em formato png, mostrando mês mês.

O período foi estipulado até o último fechamento de rendimento da poupança.
