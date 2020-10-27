# elasticsearch-sandbox kibana example 2

Vamos ver na prática como os analyzers e os tokenizers funcionam.

```
PUT /example2
{
  "settings": {
    "index": {
      "analysis": {
        "filter": {
          "synonym": {
            "type": "synonym",
            "lenient": true,
            "synonyms": [
              "i-pod, i pod => ipod",
              "universe, cosmos"
            ]
          }
        },
        "analyzer": {
          "default": {
            "filter": [
              "asciifolding",
              "lowercase",
              "stop",
              "synonym"
            ],
            "tokenizer": "standard"
          }
        }
      }
    }
  }
}

GET /_analyze
{
  "tokenizer": "standard",
  "filter": [ "stop" ],
  "text": "a quick fox jumps over the lazy dog"
}

POST /example2/_analyze
{
  "analyzer": "default",
  "text": "Este é um exemplo de texto que eu gostaria de indexar."
}

POST /example2/_analyze
{
  "analyzer": "default",
  "text": "i pod e cosmos são coisas bem loucas!"
}


POST /example2/_doc
{
  "title":"Este é um exemplo de texto que eu gostaria de indexar."
}

POST /example2/_doc
{
  "title":"exemplo para comprar um i pod."
}

GET /example2/_search
{
  "query": {
    "query_string": {
        "query":"exemplo de texto",
        "analyzer": "default"
    }
  }
}
```