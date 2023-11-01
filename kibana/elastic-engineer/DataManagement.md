# [elastic-engineer](/kibana/elastic-engineer/README.md)

Plano de estudos para o [exame de certificação da Elastic](https://www.elastic.co/training/elastic-certified-engineer-exam).
- Versão utilizada 8.1
- Este material utiliza o Docker para rodar os comandos

## Data Management
- Define an index that satisfies a given set of requirements
- Define and use an index template for a given pattern that satisfies a given set of requirements
- Define and use a dynamic template that satisfies a given set of requirements
- Define an Index Lifecycle Management policy for a time-series index
- Define an index template that creates a new data stream

---

### Define an index that satisfies a given set of requirements

#### Criando indices no elasticsearch.

Documentação oficial:

- https://www.elastic.co/guide/en/elasticsearch/reference/8.1/indices-create-index.html


##### Da forma simples, com mapping, settings e ambos:

```kibana

PUT /some-index

PUT /some-index-mapping
{
  "mappings": {
    "properties": {
      "field1": { "type": "text" }
    }
  }
}

PUT /some-index-settings
{
  "settings": {
    "index": {
      "number_of_shards": 3,
      "number_of_replicas": 2
    }
  }
}

PUT /some-index-mappong-settings
{
  "mappings": {
    "properties": {
      "field1": { "type": "text" }
    }
  },
  "settings": {
    "index": {
      "number_of_shards": 3,
      "number_of_replicas": 2
    }
  }
}

GET /
```

##### Com aliases:

- https://www.elastic.co/guide/en/elasticsearch/reference/8.1/indices-add-alias.html

```kibana

PUT /some-index-aliases
{
  "aliases": {
    "aliases_1": {},
    "aliases_2": {
      "filter": {
        "term": { "user.id": "kimchy" }
      },
      "routing": "shard-1"
    }
  }
}


PUT /some-index-aliases-date-math
{
  "aliases": {
    "<logs_{now/M}>": {}
  }
}
```


### Com diferentes tipos de mapping

```kibana



```