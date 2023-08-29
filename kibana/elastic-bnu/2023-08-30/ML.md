# [# ElasticBNU - Vamos falar de Elasticsearch?](/kibana/elastic-bnu/2023-08-30/README.md)
3º Encontro do Elastic Blumenau User Group - https://www.meetup.com/elastic-blumenau-user-group/events/294764876/
- Versão utilizada 8.9.1
- Este material utiliza o Docker para rodar os comandos

## ML

### [Eland](https://www.elastic.co/guide/en/elasticsearch/client/eland/current/machine-learning.html)

```bash
git clone https://github.com/elastic/eland

docker build -t elastic/eland .

docker run -it --rm --network host elastic/eland

docker run -it --rm --network host elastic/eland \
    eland_import_hub_model \
      --url http://localhost:9200 \
      --hub-model-id dslim/bert-base-NER \
      --task-type ner \
      --start
```
### [NER](https://www.elastic.co/blog/how-to-deploy-nlp-named-entity-recognition-ner-example)
```bash
docker run -it --rm --network host elastic/eland \
    eland_import_hub_model \
      --url http://localhost:9200 \
      --hub-model-id elastic/distilbert-base-uncased-finetuned-conll03-english \
      --task-type ner \
      --start


# modelo mais simples

docker run -it --rm --network host elastic/eland \
    eland_import_hub_model \
      --url http://localhost:9200 \
      --hub-model-id dslim/bert-base-NER \
      --task-type ner \
      --start
```

```http
POST _ml/trained_models/elastic__distilbert-base-uncased-finetuned-conll03-english/deployment/_start

POST _ml/trained_models/dslim__bert-base-ner/deployment/_start

POST _ml/trained_models/dslim__bert-base-ner/deployment/_infer
{
  "docs": [
    {
      "text_field": "Hi my name is Josh and I live in Berlin"
    }
  ]
}
```

### [Embeddings](https://www.elastic.co/blog/how-to-deploy-nlp-text-embeddings-and-vector-search)

```bash
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


### Identificador de linguagem
```http
POST _ml/trained_models/lang_ident_model_1/_infer
{
  "docs":[{"text": "The fool doth think he is wise, but the wise man knows himself to be a fool."}]
}

POST _ml/trained_models/lang_ident_model_1/_infer
{
  "docs":[{"text": "eu vou no meetup em blumenau."}]
}
```

### [analise de sentimentos](https://www.elastic.co/blog/how-to-deploy-nlp-sentiment-analysis-example)
```bash
docker run -it --rm --network host elastic/eland \
    eland_import_hub_model \
      --url http://localhost:9200 \
      --hub-model-id distilbert-base-uncased-finetuned-sst-2-english \
      --task-type text_classification \
      --start
```

```http
...
```