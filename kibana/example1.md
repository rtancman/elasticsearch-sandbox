# elasticsearch-sandbox kibana example 1

Vamos seguir os passos do artigo https://www.rtancman.com.br/information-retrieval/elasticsearch-como-ferramenta-de-busca.html#executando-comandos-do-elasticsearch


### Executando comandos do elasticsearch

```

GET /_cat/indices

PUT /meu_primeiro_index


```


### Criando um indice

```
PUT /filmes
{
  "mappings": {
    "properties": {
      "nome": {
        "type": "text"
      },
      "descricao": {
        "type": "text"
      },
      "nota": {
        "type": "float"
      },
      "classificao": {
        "type": "text"
      },
      "data_lancamento": {
        "type": "date"
      }
    }
  }
}

GET /filmes/_mapping
GET /filmes/_settings
```


### Criando documentos 

```
POST /filmes/_doc/
{
  "nome": "Matrix",
  "descricao": "Melhor filme ever!",
  "classificao": "livre",
  "nota": 10,
  "data_lancamento": "1999-05-21T14:12:12"
}
```

### Editando documentos

```
POST filmes/_update/ID_DO_DOC
{
  "doc": {
    "classificao": "Não recomendado para menores de doze anos"
  }
}

```

### Lendo documentos

```

GET filmes/_doc/-DEY_XIBblRt4Ct0995B

```

### Removendo documentos

```

DELETE filmes/_doc/-DEY_XIBblRt4Ct0995B

```


### Criando varios documentos

```

POST /filmes/_bulk
{"index":{}}
{"nome":"Matrix","descricao":"Melhor filme ever!","classificao":"Não recomendado para menores de doze anos","nota":10,"data_lancamento":"1999-05-21T14:12:12"}
{"index":{}}
{"nome":"Matrix Reloaded","descricao":"Melhor filme ever!!!!","classificao":"Não recomendado para menores de doze anos","nota":8.5,"data_lancamento":"2003-05-15T11:30:00"}
{"index":{}}
{"nome":"Matrix Revolutions","descricao":"Melhor filme ever!!!!","classificao":"Não recomendado para menores de doze anos","nota":8.9,"data_lancamento":"2003-11-05T11:30:00"}
{"index":{}}
{"nome":"Matrix 4","descricao":"Melhor filme ever!!!!","classificao":"Não recomendado para menores de doze anos","nota":0,"data_lancamento":"2022-04-01T11:30:00"}


```


### Realizando queries

```
GET /filmes/_search

GET filmes/_search
{
  "query": {
    "match": {
      "nome": "Matrix"
    }
  }
}

GET filmes/_search
{
  "query": {
    "match": {
      "nome": "Matrix"
    }
  }
}


GET /filmes/_search
{
  "query": {
    "range": {
      "nota": {
        "gte": 2,
        "lte": 9
      }
    }
  }
}


GET /filmes/_search
{
  "query": {
    "query_string": {
        "query":"Matrix"
    }
  }
}

```