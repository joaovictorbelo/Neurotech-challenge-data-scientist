# Neurotech-monitoring-api
Repositório com a API para o desafio de ciência de dados do processo seletivo da Neurotech.

## Rodando o projeto
A aplicação API foi desenvolvida utilizando Python3 com uvicorn como ferramenta para servidor e fastAPI como biblioteca para realizar roteamento e requisições.
Para rodar em desenvolvimento foi usado o comando:

```
uvicorn main:app --reload
```
### Ferramentas adicionais:
- Foi utilizado o programa Imsomnia como client de api para teste de requisições

## Diretorios
- As funções com lógica estão junto das rotas na pasta de [endpoints](https://github.com/joaovictorbelo/Neurotech-challenge-data-scientist/tree/main/app/api/endpoints) nos arquivos de cada funcionalidade. </br>
- Além disso, os modelos basicos de request usando pydantic estão na pasta de [models](https://github.com/joaovictorbelo/Neurotech-challenge-data-scientist/tree/main/app/api/models) </br>
- O modelo pickle pré-treinado fornecido no desafio esta na pasta [ml_models](https://github.com/joaovictorbelo/Neurotech-challenge-data-scientist/tree/main/ml_models)

## Documentação API
### Volumetria e Performance
- <b>ROTA:</b> `http://localhost:8001/v1/performance`
- <b>MÉTODO:</b> `POST`
- <b>BODY REQUISIÇÃO:</b> Exatamente como os dados estão dispostos no arquivo: [batch_records](https://github.com/joaovictorbelo/Neurotech-challenge-data-scientist/blob/main/batch_records.json):
```
[
    {
        VAR2: [str]
        IDADE: [float]
        ⋮
        REF_DATE: [str]
        TARGET: [int]
    },
    {
        VAR2: [str]
        IDADE: [float]
        ⋮
        REF_DATE: [str]
        TARGET: [int]
    },
    ⋮
]
```
- <b>RESPOSTA</b>: JSON contendo os dados de volumetria e performance, distribuidos da seguinte maneira:
```
{
    "volumetria": 
    {
        "ANO-MES": quantidade
        ⋮ 
        "ANO-MES": quantidade
    },
    "performance": valor medido da área sob a curva ROC
}
```
