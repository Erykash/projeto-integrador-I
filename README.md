# projeto-integrador-I

COLETA DE DADOS:

Iniciando na coleta dos dados históricos das ações da Petrobras (PETR4.SA e PETR3.SA), do par de moedas USD/BRL e do índice BOVA11.SA, no período de 2020 a novembro de 2023, usando fontes de dados API´S, que são usadas para integrar novas aplicações com sistemas de software existentes, como Yahoo Finance de dados financeiros, utilizada para essa coleta de dados especifica.


ANÁLISE DESCRITIVA:

Uma análise descritiva dos dados coletados para entender as tendências passadas e a volatilidade de cada ativo.

Apresentando tais dados para inferir essas analises

Contagem ( count):
Representa o número total de observações (dias de negociação) no período. Todas as séries têm 954 observações.

Média ( mean):
Indica o valor médio dos preços de fechamento ao longo do período. Por exemplo, a média do PETR4.SA é aproximadamente 15,52.

Desvio Padrão ( std):
Mede a dispersão dos dados em torno da média. Quanto maior o desvio padrão, maior a volatilidade. Por exemplo, o desvio padrão do BOVA11.SA é cerca de 10,81, caindo uma volatilidade relativamente moderada.

Mínimo ( min) e Máximo ( max):
Representam os valores mínimos e máximos observados durante o período. Por exemplo, o preço mínimo de fechamento para o PETR4.SA foi cerca de 4,31, e o preço máximo foi 38,52.

Porcentagens ( 25%, 50%, 75%):
Representamos os valores abaixo dos quais uma determinada porcentagem dos dados está contida. Por exemplo, o valor do terceiro quartil (75%) para o BOVA11.SA é aproximadamente 112,80, indicando que 75% dos preços de fechamento estão abaixo desse valor.
Essas estatísticas fornecem uma visão geral da distribuição dos preços ao longo do tempo para cada ativo. Eles podem ser úteis para entender a variabilidade, tendência central e amplitude dos preços durante o período analisado.

COMPARAÇÃO ENTRE PETR4.SA, PETR3.SA e Dólar/Real:

Criação de gráficos de comparação que mostram como as ações da Petrobras (PETR4.SA e PETR3.SA) estão correlacionadas com o câmbio USD/BRL. 


Comparação de Tendências:
O gráfico permite comparar visualmente as tendências de preço de fechamento ao longo do período de tempo especificado para os três ativos. Cada linha representa um ativo diferente, facilitando a comparação de seu desempenho.

Padrões de Movimento:
Observando o padrão das linhas, você pode identificar possíveis padrões de movimento, como tendências de alta, baixa ou períodos de volatilidade.

Relações entre Ativos:
Você pode observar como os preços de PETR4.SA e PETR3.SA se comparam entre si, bem como como esses ativos se comparam ao BOVA11.SA, que é um ETF que replica o desempenho do Ibovespa.

PREVISÃO DAS OSCILAÇÕES DO BOVA11.SA:

Divisão dos dados do índice BOVA11.SA em conjuntos de treinamento e teste. Utilizando técnicas de previsão de séries temporais, como modelos ARIMA, que é um modelo auto-regressivo integrado de médias móveis é uma generalização de um modelo auto-regressivo de médias móveis, para prever as oscilações futuras desse índice.


Os valores de Mean Squared Error (MSE) que você obteve indicam o desempenho do modelo de regressão linear nos conjuntos de treinamento e teste. Vamos interpretar esses resultados:

MSE (Treinamento): 0,4106
Esse valor representa o MSE no conjunto de dados de treinamento. O MSE mede a média dos quadrados dos erros entre a variação do modelo e os valores reais no conjunto de treinamento. Nesse caso, um MSE de 0,4106 sugere que, em média, os quadrados dos erros no conjunto de treinamento são relativamente pequenos.

MSE (Teste): 0,2812
Esse valor representa o MSE no conjunto de dados de teste. O MSE no conjunto de teste é um indicador crucial do desempenho do modelo em dados não visíveis. Nesse caso, um MSE de 0.2812 sugere que o modelo está generalizando bem para novos dados, uma vez que o erro médio nos dados de teste também é relativamente pequeno.


