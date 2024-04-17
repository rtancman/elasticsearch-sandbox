# [ElasticBNU - Criando um buscador utilizando o Elasticsearch](/kibana/74-python-devops-floripa-na-rd/README.md)
74º Python + DevOps Floripa na RD
- Versão utilizada 8.13.2
- Este material utiliza o Docker para rodar os comandos

## RRF
- https://www.elastic.co/blog/whats-new-elastic-enterprise-search-8-9-0
- https://www.elastic.co/guide/en/elasticsearch/reference/current/rrf.html

### Sub searchs with RRF
```http
GET elastic-bnu-with-embeddings/_search
{
  "sub_searches": [
    {
      "query": {
        "query_string": {
          "default_field": "text",
          "query": "Ojitos"
        }
      }
    },
    {
      "query": {
        "query_string": {
          "default_field": "text",
          "query": "Colombia"
        }
      }
    },
    {
      "query": {
        "query_string": {
          "default_field": "text",
          "query": "Ella"
        }
      }
    }
  ],
  "rank": {
    "rrf": {
      "window_size": 50,
      "rank_constant": 20
    }
  },
  "_source": [
    "id",
    "text"
  ]
}
```

### Hybrid search with RRF
```http
GET elastic-bnu-with-embeddings/_search
{
  "query": {
    "term": {
      "text": "Lindos"
    }
  },
  "knn": {
    "field": "text_embedding.predicted_value",
    "query_vector_builder": {
      "text_embedding": {
        "model_id": "sentence-transformers__msmarco-minilm-l-12-v3",
        "model_text": "Ojitos Lindos Colombia"
      }
    },
    "k": 10,
    "num_candidates": 100
  },
  "rank": {
    "rrf": {
      "window_size": 50,
      "rank_constant": 20
    }
  },
  "_source": [
    "id",
    "text"
  ]
}
```