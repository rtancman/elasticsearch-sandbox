# [# ElasticBNU - Vamos falar de Elasticsearch?](/kibana/elastic-bnu/2023-08-30/README.md)
3º Encontro do Elastic Blumenau User Group - https://www.meetup.com/elastic-blumenau-user-group/events/294764876/
- Versão utilizada 8.9.1
- Este material utiliza o Docker para rodar os comandos

## Indices, mappings e settings

```

GET /_cat/indices
PUT /meu_primeiro_index
DELETE /meu_primeiro_index

```


#### Criando um indice

```

PUT /autores
{
  "settings": {
    "number_of_replicas": "1",
    "number_of_shards": "2",
    "analysis": {
      "analyzer": {
        "meu_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "asciifolding"
          ]
        }
      }
    }
  },
  "mappings": {
    "dynamic": "strict",
    "_source": {
      "excludes": [
        "todos"
      ]
    },
    "properties": {
      "todos": {
        "type": "text",
        "analyzer": "meu_analyzer"
      },
      "nome": {
        "type": "text",
        "copy_to": [
          "todos"
        ]
      },
      "descricao": {
        "type": "text",
        "copy_to": [
          "todos"
        ]
      },
      "email": {
        "type": "keyword",
        "copy_to": [
          "todos"
        ]
      },
      "site": {
        "type": "keyword",
        "copy_to": [
          "todos"
        ]
      },
      "especialidade": {
        "type": "text",

        "copy_to": [
          "todos"
        ]
      },
      "data_nascimento": {
        "type": "date",
        "copy_to": [
          "todos"
        ]
      }
    }
  }
}

PUT /livros
{
  "settings": {
    "number_of_replicas": "1",
    "number_of_shards": "2",
    "analysis": {
      "analyzer": {
        "meu_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": ["lowercase", "asciifolding"]
        }
      }
    }
  },
  "mappings": {
    "dynamic": "strict",
    "_source": {
      "excludes": [
        "todos"
      ]
    },
    "properties": {
      "todos": {
        "type": "text",
        "analyzer": "meu_analyzer"
      },
      "titulo": {
        "type": "text",
        "copy_to": [
          "todos"
        ]
      },
      "descricao": {
        "type": "text",
        "copy_to": [
          "todos"
        ]
      },
      "assunto": {
        "type": "text",
        "copy_to": [
          "todos"
        ]
      },
      "autores": {
        "type": "text",
        "copy_to": [
          "todos"
        ]
      },
      "avaliacao": {
        "type": "float"
      }
    }
  }
}

PUT /artigos
{
  "settings": {
    "number_of_replicas": "1",
    "number_of_shards": "2",
    "analysis": {
      "analyzer": {
        "meu_analyzer": {
          "type": "custom",
          "tokenizer": "standard",
          "filter": [
            "lowercase",
            "asciifolding"
          ]
        }
      }
    }
  },
  "mappings": {
    "dynamic": "strict",
    "_source": {
      "excludes": [
        "todos"
      ]
    },
    "properties": {
      "todos": {
        "type": "text",
        "analyzer": "meu_analyzer"
      },
      "titulo": {
        "type": "text",
        "copy_to": [
          "todos"
        ]
      },
      "descricao": {
        "type": "text",
        "copy_to": [
          "todos"
        ]
      },
      "conteudo": {
        "type": "text",
        "copy_to": [
          "todos"
        ]
      },
      "autores": {
        "type": "text",
        "copy_to": [
          "todos"
        ]
      },
      "avaliacao": {
        "type": "float"
      }
    }
  }
}

POST /_aliases
{
  "actions" : [
    { "add" : { "indices" : ["autores", "artigos", "livros"], "alias" : "busca-geral" } },
    { "add" : { "indices" : ["artigos", "livros"], "alias" : "busca-artigos-livros" } },
  ]
}

GET /_cat/indices?s=index

# verificando mappings e settings
GET /autores/_mapping
GET /autores/_settings

# verificando settings de todos os indices da busca geral
GET /busca-geral/_settings/index.*
GET /busca-geral/_settings
GET /busca-geral/_mapping
```