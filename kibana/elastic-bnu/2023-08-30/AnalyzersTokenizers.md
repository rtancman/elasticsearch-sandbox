# [# ElasticBNU - Vamos falar de Elasticsearch?](/kibana/elastic-bnu/2023-08-30/README.md)
3º Encontro do Elastic Blumenau User Group - https://www.meetup.com/elastic-blumenau-user-group/events/294764876/
- Versão utilizada 8.9.1
- Este material utiliza o Docker para rodar os comandos

## Analyzers e tokenizers

```

POST /_analyze
{
  "tokenizer": "standard",
  "text": "Exemplo padrão de analise de texto"
}

POST /_analyze
{
  "tokenizer": "standard",
  "text": "rtancman@teste3.com https://www.elastic.co/pt/blog/elastic-stack-7-13-1-released"
}

POST /_analyze
{
  "tokenizer": "uax_url_email",
  "text": "rtancman@teste3.com https://www.elastic.co/pt/blog/elastic-stack-7-13-1-released"
}

GET /_analyze
{
  "tokenizer": "standard",
  "filter": [
    {
      "type": "condition",
      "filter": [ "lowercase" ],
      "script": {
        "source": "token.getTerm().length() < 7"
      }
    }
  ],
  "text": "EXEMPLO DE ANALYZE COM CONDICAO NO FILTRO"
}

GET /_analyze
{
  "tokenizer" : "standard",
  "filter" : [
    "lowercase",
    "asciifolding"
  ],
  "text" : "Texto com acentos e outros caracteres. Aqui: imprescindível, diligência, índices, ações"
}

```

### Stop words Analyzers e tokenizers

```

# removendo stop words https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-stop-tokenfilter.html

PUT /exemplo-stop-word
{
  "settings": {
    "index": {
      "analysis": {
        "filter": {
          "stop_words_brazilian": {
            "type": "stop",
            "stopwords": "_brazilian_"
          }
        },
        "analyzer": {
          "sem-stop-words": {
            "filter": [
              "asciifolding",
              "lowercase",
              "stop_words_brazilian"
            ],
            "tokenizer": "standard"
          }
        }
      }
    }
  }
}

POST /exemplo-stop-word/_analyze
{
  "analyzer": "sem-stop-words",
  "text": "Este é um exemplo de texto que eu gostaria de indexar."
}


```

### Sinônimos

```

# exemplo com sinonimos
PUT /exemplo-sinonimos
{
  "settings": {
    "index": {
      "analysis": {
        "analyzer": {
          "trando-sinonimos": {
            "tokenizer": "standard",
            "filter": [ "synonym" ]
          }
        },
        "filter": {
          "synonym": {
            "type": "synonym",
            "lenient": true,
            "synonyms": [ "tdc 2021, tdc, tdc connections => the developers conference" ]
          }
        }
      }
    }
  }
}

POST /exemplo-sinonimos/_analyze
{
  "analyzer": "trando-sinonimos",
  "text": "tdc 2021"
}

POST /exemplo-sinonimos/_analyze
{
  "analyzer": "trando-sinonimos",
  "text": "tdc"
}

POST /exemplo-sinonimos/_analyze
{
  "analyzer": "trando-sinonimos",
  "text": "tdc connections"
}

POST /exemplo-sinonimos/_analyze
{
  "analyzer": "trando-sinonimos",
  "text": "the developers conference"
}


```

### Stemmer

```

# exemplo com stemmer https://www.elastic.co/guide/en/elasticsearch/reference/current/analysis-stemmer-tokenfilter.html
GET /_analyze
{
  "tokenizer": "standard",
  "filter": [ "stemmer" ],
  "text": "the foxes jumping quickly"
}

PUT /exemplo-stemmer
{
  "settings": {
    "index": {
      "analysis": {
        "analyzer": {
          "exemplo-stemmer": {
            "tokenizer": "standard",
            "filter": [ "brazilian_stemmer" ]
          }
        },
        "filter": {
          "brazilian_stemmer": {
            "type": "stemmer",
            "language": "brazilian"
          }
        }
      }
    }
  }
}

POST /exemplo-stemmer/_analyze
{
  "analyzer": "exemplo-stemmer",
  "text": "Raffael, Raffaeis, Rafaela, Rafaelo"
}

```