from datetime import datetime
from elasticsearch import Elasticsearch
es = Elasticsearch()

doc = {
    'author': 'kimchy',
    'text': 'Elasticsearch: cool. bonsai cool.',
    'timestamp': datetime.now(),
}
res = es.index(index="test-index", id=1, body=doc)
print(res['result'])

res = es.get(index="test-index", id=1)
print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
print("Got %d Hits:" % res['hits']['total']['value'])
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])

resp = es.search(
    index="test-index",
    size=0,
    body={
        "query": {
            "query_string": {
                "query":"bonsai"
            }
        }
    }
)

print(resp)



## criando indices

es.indices.create(
    index="filmes-python",
    body={
        "settings": {"number_of_shards": 1},
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
        },
    },
    ignore=400,
)


doc_id = '7Rt9cXUBhWsOrFfCWDh1'
doc = {
  "nome": "Matrix",
  "descricao": "Melhor filme ever!",
  "classificao": "livre",
  "nota": 10,
  "data_lancamento": "1999-05-21T14:12:12"
}
## criar o documento 
res = es.index(index="filmes-python", id=doc_id, body=doc)
print(res)

## pegar documentos
res = es.get(index='filmes-python',id=doc_id)
print(res)


## deletar

res = es.delete(index='filmes-python',id=doc_id)
print(res['result'])


## busca 
res= es.search(index='filmes-python',body={'query':{'match_all':{}}})
