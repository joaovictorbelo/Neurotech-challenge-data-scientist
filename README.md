# Neurotech-monitoring-api
Repositório com a API para o desafio de ciência de dados do processo seletivo da Neurotech.

## 1. Rodando o projeto
A aplicação API foi desenvolvida utilizando Python3 com uvicorn como ferramenta para servidor e fastAPI como biblioteca para realizar roteamento e requisições.
Para rodar em desenvolvimento foi usado o comando:

```
uvicorn main:app --reload
```
### 1.1 Ferramentas adicionais:
- Foi utilizado o programa Imsomnia como client de api para teste de requisições

## 2. Diretorios
- As funções com lógica estão junto das rotas na pasta de [endpoints](https://github.com/joaovictorbelo/Neurotech-challenge-data-scientist/tree/main/app/api/endpoints) nos arquivos de cada funcionalidade. </br>
- As funções reutilizadas foram colocadas na pasta de [utils](https://github.com/joaovictorbelo/Neurotech-challenge-data-scientist/tree/main/app/utils)
- Os modelos basicos de request usando pydantic estão na pasta de [models](https://github.com/joaovictorbelo/Neurotech-challenge-data-scientist/tree/main/app/api/models) </br>
- O modelo pickle pré-treinado fornecido no desafio esta na pasta [ml_models](https://github.com/joaovictorbelo/Neurotech-challenge-data-scientist/tree/main/ml_models)

## 3. Documentação API
### 3.1 Volumetria e Performance
- <b>ROTA:</b> `http://localhost:8001/v1/performance`
- <b>MÉTODO:</b> `POST`
- <b>BODY REQUISIÇÃO:</b> Exatamente como os dados estão dispostos no arquivo: [batch_records](https://github.com/joaovictorbelo/Neurotech-challenge-data-scientist/blob/main/batch_records.json):
```js
[
    {
        "VAR2": [str]
        "IDADE": [float]
        ⋮
        "REF_DATE": [str]
        "TARGET": [int]
    },
    {
        "VAR2": [str]
        "IDADE": [float]
        ⋮
        "REF_DATE": [str]
        "TARGET": [int]
    },
    ⋮
]
```
- <b>RESPOSTA</b>: JSON contendo os dados de volumetria e performance, distribuidos da seguinte maneira:
```js
{
    "volumetria": 
    {
        "ANO-MES": [quantidade]
        ⋮ 
        "ANO-MES": [quantidade]
    },
    "performance": [area_sob_a_curva_ROC]
}
```

### 3.2 Aderência
- <b>ROTA:</b> `http://localhost:8001/v1/aderencia`
- <b>MÉTODO:</b> `POST`
- <b>BODY REQUISIÇÃO:</b> JSON com uma variavel nomeada 'path' contendo o caminho local do arquivo de dataset:
```js
{
    "path": [path_to_local_dataset]
}
```
- <b>RESPOSTA</b>: JSON contendo os dados de volumetria e performance, distribuidos da seguinte maneira:
```js
{
    "aderencia": [stat_do_teste_kolmogorov_smirnov]
}
```

## 4. Resultados
Os resultados das requisições da API estão no arquivo do jupyter [notebook](https://github.com/joaovictorbelo/Neurotech-challenge-data-scientist/blob/main/tests.ipynb) que se encontra nesse repositorio
