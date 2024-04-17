# [ElasticBNU - Criando um buscador utilizando o Elasticsearch](/kibana/74-python-devops-floripa-na-rd/README.md)
74º Python + DevOps Floripa na RD
- Versão utilizada 8.13.2
- Este material utiliza o Docker para rodar os comandos

## Busca vetorial


### install msmarco with eland


```bash
git clone https://github.com/elastic/eland

docker build -t elastic/eland .

docker run -it --rm --network host elastic/eland \
    eland_import_hub_model \
      --url http://localhost:9200 \
      --hub-model-id sentence-transformers/msmarco-MiniLM-L-12-v3 \
      --task-type text_embedding \
      --start
```

```http
POST _ml/trained_models/sentence-transformers__msmarco-minilm-l-12-v3/deployment/_start


POST _ml/trained_models/sentence-transformers__msmarco-minilm-l-12-v3/deployment/_infer
{
  "docs": [
    {
      "text_field": "Elastic meetup blumenau"
    }
  ]
}
```


### text embedding
```http

POST _ml/trained_models/sentence-transformers__msmarco-minilm-l-12-v3/_infer
{
  "docs": [
    {
      "text_field": "Criando um buscador utilizando o Elasticsearch na 74º Python + DevOps Floripa na RD"
    }
  ]
}

```


### ingestion pipeline

```http

PUT _ingest/pipeline/text-embeddings
{
  "description": "Text embedding pipeline",
  "processors": [
    {
      "inference": {
        "model_id": "sentence-transformers__msmarco-minilm-l-12-v3",
        "target_field": "text_embedding",
        "field_map": {
          "text": "text_field"
        }
      }
    }
  ],
  "on_failure": [
    {
      "set": {
        "description": "Index document to 'failed-<index>'",
        "field": "_index",
        "value": "failed-{{{_index}}}"
      }
    },
    {
      "set": {
        "description": "Set error message",
        "field": "ingest.failure",
        "value": "{{_ingest.on_failure_message}}"
      }
    }
  ]
}

PUT elastic-bnu
{
  "mappings": {
    "properties": {
      "text": {
        "type": "text"
      }
    }
  }
}

PUT elastic-bnu-with-embeddings
{
  "mappings": {
    "properties": {
      "text_embedding.predicted_value": {
        "type": "dense_vector",
        "dims": 384,
        "index": true,
        "similarity": "cosine"
      },
      "text": {
        "type": "text"
      }
    }
  }
}

POST /elastic-bnu/_bulk
{"index":{}}
{"text":"Lana Del Rey Summertime Sadness United States"}
{"index":{}}
{"text":"Eliza Rose, Interplanetary Criminal B.O.T.A. (Baddest Of Them All) - Edit United Kingdom"}
{"index":{}}
{"text":"Eliza Rose, Interplanetary Criminal B.O.T.A. (Baddest Of Them All) - Edit United Kingdom"}
{"index":{}}
{"text":"Lost Frequencies, Calum Scott Where Are You Now Belgium"}
{"index":{}}
{"text":"Lost Frequencies, Calum Scott Where Are You Now United Kingdom"}
{"index":{}}
{"text":"Paulo Londra, Feid A Veces (feat. Feid) Argentina"}
{"index":{}}
{"text":"Paulo Londra, Feid A Veces (feat. Feid) Colombia"}
{"index":{}}
{"text":"Jhayco, Feid, Sech En La De Ella Puerto Rico"}
{"index":{}}
{"text":"Jhayco, Feid, Sech En La De Ella Colombia"}
{"index":{}}
{"text":"Jhayco, Feid, Sech En La De Ella Panama"}
{"index":{}}
{"text":"Maroon 5, Wiz Khalifa Payphone United States"}
{"index":{}}
{"text":"Maroon 5, Wiz Khalifa Payphone United States"}
{"index":{}}
{"text":"Lewis Capaldi Forget Me United Kingdom"}
{"index":{}}
{"text":"Måneskin THE LONELIEST Italy"}
{"index":{}}
{"text":"Olivia Rodrigo drivers license United States"}
{"index":{}}
{"text":"OneRepublic Counting Stars United States"}
{"index":{}}
{"text":"Olivia Rodrigo traitor United States"}
{"index":{}}
{"text":"Burna Boy Alone Nigeria"}
{"index":{}}
{"text":"(G)I-DLE Nxde South Korea"}
{"index":{}}
{"text":"Vance Joy Riptide Australia"}
{"index":{}}
{"text":"BTS Run BTS South Korea"}
{"index":{}}
{"text":"Sam Smith, Kim Petras Unholy (feat. Kim Petras) United Kingdom"}
{"index":{}}
{"text":"Sam Smith, Kim Petras Unholy (feat. Kim Petras) Germany"}
{"index":{}}
{"text":"Taylor Swift Anti-Hero United States"}
{"index":{}}
{"text":"Drake, 21 Savage Rich Flex Canada"}
{"index":{}}
{"text":"Drake, 21 Savage Rich Flex United Kingdom"}
{"index":{}}
{"text":"Manuel Turizo La Bachata Colombia"}
{"index":{}}
{"text":"David Guetta, Bebe Rexha I'm Good (Blue) France"}
{"index":{}}
{"text":"David Guetta, Bebe Rexha I'm Good (Blue) United States"}
{"index":{}}
{"text":"Harry Styles As It Was United Kingdom"}
{"index":{}}
{"text":"Bizarrap, Quevedo Quevedo: Bzrp Music Sessions, Vol. 52 Argentina"}
{"index":{}}
{"text":"Bizarrap, Quevedo Quevedo: Bzrp Music Sessions, Vol. 52 Spain"}
{"index":{}}
{"text":"Chris Brown Under The Influence United States"}
{"index":{}}
{"text":"Taylor Swift Midnight Rain United States"}
{"index":{}}
{"text":"Taylor Swift Lavender Haze United States"}
{"index":{}}
{"text":"Bad Bunny, Chencho Corleone Me Porto Bonito Puerto Rico"}
{"index":{}}
{"text":"Bad Bunny, Chencho Corleone Me Porto Bonito Puerto Rico"}
{"index":{}}
{"text":"Tom Odell Another Love United Kingdom"}
{"index":{}}
{"text":"Oliver Tree, Robin Schulz Miss You United States"}
{"index":{}}
{"text":"Oliver Tree, Robin Schulz Miss You Germany"}
{"index":{}}
{"text":"OneRepublic I Ain't Worried United States"}
{"index":{}}
{"text":"Ozuna, Feid Hey Mor Puerto Rico"}
{"index":{}}
{"text":"Ozuna, Feid Hey Mor Colombia"}
{"index":{}}
{"text":"Bad Bunny Tití Me Preguntó Puerto Rico"}
{"index":{}}
{"text":"Steve Lacy Bad Habit United States"}
{"index":{}}
{"text":"Meghan Trainor Made You Look United States"}
{"index":{}}
{"text":"Rihanna Lift Me Up - From Black Panther: Wakanda Forever - Music From and Inspired By Barbados"}
{"index":{}}
{"text":"Taylor Swift, Lana Del Rey Snow On The Beach (feat. Lana Del Rey) United States"}
{"index":{}}
{"text":"Taylor Swift, Lana Del Rey Snow On The Beach (feat. Lana Del Rey) United States"}
{"index":{}}
{"text":"Taylor Swift You're On Your Own, Kid United States"}
{"index":{}}
{"text":"Taylor Swift Maroon United States"}
{"index":{}}
{"text":"Bad Bunny Efecto Puerto Rico"}
{"index":{}}
{"text":"Joji Die For You Jamaica"}
{"index":{}}
{"text":"ROSALÍA DESPECHÁ Spain"}
{"index":{}}
{"text":"Taylor Swift Karma United States"}
{"index":{}}
{"text":"Joji Glimpse of Us Jamaica"}
{"index":{}}
{"text":"Stephen Sanchez Until I Found You United States"}
{"index":{}}
{"text":"d4vd Romantic Homicide United States"}
{"index":{}}
{"text":"Taylor Swift Bejeweled United States"}
{"index":{}}
{"text":"The Weeknd Die For You Canada"}
{"index":{}}
{"text":"Arctic Monkeys I Wanna Be Yours United Kingdom"}
{"index":{}}
{"text":"Rema, Selena Gomez Calm Down (with Selena Gomez) Nigeria"}
{"index":{}}
{"text":"Rema, Selena Gomez Calm Down (with Selena Gomez) United States"}
{"index":{}}
{"text":"Beyoncé CUFF IT United States"}
{"index":{}}
{"text":"Bad Bunny, Bomba Estéreo Ojitos Lindos Puerto Rico"}
{"index":{}}
{"text":"Bad Bunny, Bomba Estéreo Ojitos Lindos Colombia"}
{"index":{}}
{"text":"The Neighbourhood Sweater Weather United States"}

POST _reindex?wait_for_completion=false
{
  "source": {
    "index": "elastic-bnu"
  },
  "dest": {
    "index": "elastic-bnu-with-embeddings",
    "pipeline": "text-embeddings"
  }
}

GET _tasks/<task_id>

GET elastic-bnu-with-embeddings/_search
{
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
  "_source": [
    "id",
    "text"
  ]
}

```

### Hybrid search with RRF
- https://www.elastic.co/blog/whats-new-elastic-enterprise-search-8-9-0
- https://www.elastic.co/guide/en/elasticsearch/reference/current/rrf.html

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