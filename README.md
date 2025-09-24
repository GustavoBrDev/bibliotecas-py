# Pandas

O Pandas é uma biblioteca amplamente utilizado para **Data Science**. Ele consta com operações otimizadas utilizando entre muitas coisas o **numpy**.

Sua principal funcionalidade gira em torno dos chamados **Data Frames** permitindo a analise de planilhas excel, arquivos csv, outros conectores de dados em insights valiosos. Em poucos comandos como **info, head, tail, describe** você poderá identificar a qualidade e estrutura de seus dados.

Abaixo segue um breve descritivo das aulas e o que foi visto em cada.

## Primeira Aula - 22/09/2025

Nessa aula foi introduzido o Pandas e sua "integração" com os gráficos do **Matplot**. Para isso foram criado dois arquivos:

* **pandas**: Analise exploratória do Pandas, utilização das primeiras funções (head, shape, tail, info, etc) e explicações inicias.
* **pandas-titanic**: Analise de dados do banco de dados da tragédia do titanic, aplicação prática das funções do pandas.

### Pandas

No arquivo de pandas foram vistos as seguintes funções/conceitos:

* **Agrupamento**: Realizado agrupamento de dados utilizando **groupBy**;
* **Colunas**: Manipulado colunas utilizando **rename** e outras operações de inserções dados;
* **Informações**: Visualizado as informações do dataset utilizando **shape** e **info**;
* **Visualização**: Visualizado dados utilizando funções como **head** e **tail**;
* **Seleção de Dados**: Selecionando dados utilizando **loc** e **iloc**;
* **Manipulação**: Manipulação de dados, seja através de **drop**, **dropna** (valores nulos) e outrem.

Além disso, foram abordados os conceitos de Data Frame e introduzido o conceito de analise de dados.

### Pandas Titanic

Neste arquivo foram aplicados os conceitos previamente definidos. Para isso realizou-se uma analise exploratório do data set do titanic e alguns gráficos foram elaborados utilizando o **Mat plot**. Algumas das informações obtidas são:

* Quantidade de crianças (menores que 18 anos)
* Quantidade de passageiros de primeira classe
* Quantidade de crianças (menores que 18 anos) da primeira classe
* Relação de sobreviventes e não sobreviventes [Gráfico]
* Taxa de sobrevivência entre homens e mulheres [Gráfico]
* Passageiros por classe [Gráfico]
* Idade média por classe [Gráfico]
* Média de idade dos sobreviventes
* Passagem mais cara
* Porcentagem de homens e mulheres na primeira classe [Gráfico]
* Distribuição de tarifa média por classe [Gráfico]
* Sobreviventes por classe no Titanic [Gráfico]
* Sobreviventes por faixa etária [Gráfico]
* Taxa de sobrevivência por porto de embarque [Gráfico]
* Idade média dos passageiros por título (Mr, Mrs, Miss) [Gráfico]
* Sobreviventes adultos e crianças na terceira classe [Gráfico]
* Nomes mais comuns [Gráfico]

Com isso foram possíveis obter os seguintes insights:

* A taxa de sobrevivência é maior entre as mulheres, apesar da quantidade proporcional ser menor;
* A maioria dos sobreviventes eram 'jovens';
* A maioria dos sobreviventes eram da primeira classe;
* A tarifa média da terceira classe se tornou maior que a segunda.