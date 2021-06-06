# Elasticsearch como máquina de busca


## Iniciando com o docker

```bash

docker-compose up -d

```
Acesse o kibana na pela url [http://localhost:5601/app/dev_tools](http://localhost:5601/app/dev_tools).


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
            "asciifolding",
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
      }
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
      "avaliacao": {
        "type": "float"
      }
    }
  }
}

POST /_aliases
{
  "actions" : [
    { "add" : { "indices" : ["autores", "artigos", "livros"], "alias" : "busca-geral" } }
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


## Query

### Criando documentos 

```

### Criando os documentos para testar query
POST /autores/_bulk
{"index":{}}
{"nome":"Ricardo Baeza-Yates","descricao":"Ricardo é Professor Pesquisador do Instituto de IA Experiencial da Northeastern University. Ele também é professor em tempo parcial na Universitat Pompeu Fabra em Barcelona e na Universidad de Chile em Santiago. Antes, ele foi VP de Pesquisa no Yahoo Labs, com sede em Barcelona, Espanha, e depois em Sunnyvale, Califórnia, de 2006 a 2016. Ele é coautor do best-seller Modern Information Retrieval publicado pela Addison-Wesley em 1999 e 2011 (2ª ed), que ganhou o prêmio ASIST 2012 Book of the Year. De 2002 a 2004 foi eleito para o Conselho de Governadores do IEEE CS e entre 2012 e 2016 foi eleito para o Conselho ACM. Desde 2010 é membro fundador da Academia Chilena de Engenharia. Em 2009 foi nomeado ACM Fellow e em 2011 IEEE Fellow, entre outros prêmios. Ele obteve um Ph.D. em CS da Univ. de Waterloo, Canadá, em 1989, e sua especialidade é em pesquisa na web e mineração de dados, recuperação de informações, preconceito e ética em IA, ciência de dados e algoritmos em geral.","email":"Baeza-Yates@exemplotdc.com.br","site":"http://www.baeza.cl/","especialidade":"recuperação da informacao","data_nascimento":"1961-03-21T00:00:00"}
{"index":{}}
{"nome":"Berthier Ribeiro-Neto","descricao":"Berthier Ribeiro-Neto é Professor Associado do Departamento de Ciência da Computação da Universidade Federal de Minas Gerais, atualmente em regime de meio período. Ele também é Diretor de Engenharia e Site Lead no Centro de Pesquisa e Desenvolvimento do Google, localizado em Belo Horizonte. Seus interesses de pesquisa incluem recuperação de informações (RI), sistemas da Web e bibliotecas digitais.","email":"Berthier-Ribeiro-Neto@exemplotdc.com.br","site":"https://scholar.google.com/citations?user=JMkfK0sAAAAJ","especialidade":"recuperação da informacao","data_nascimento":"1981-05-11T00:00:00"}
{"index":{}}
{"nome":"Edleno Silva de Moura","descricao":"Edleno Silva de Moura graduou-se em Processamento de Dados na UFAM em 1994 e obteve o grau de Doutor em Ciência da Computação na UFMG em 1999, sendo o primeiro aluno do curso a concluir o doutorado sem ter se formado mestre. Teve recentemente sua bolsa de pesquisa aprovada para nível 1b a partir de março de 2019. Após seu doutoramento, atuou como Diretor de Tecnologia da empresa Akwan S/A até 2002. Desde 2002 atua no Instituto de Computação UFAM como professor, sendo hoje professor titular.","email":"EdlenoSilvadeMoura@exemplotdc.com.br","site":"https://scholar.google.com/citations?user=gMHGurgAAAAJ&hl=en","especialidade":"recuperação da informacao","data_nascimento":"1982-01-21T00:00:00"}
{"index":{}}
{"nome":"Rob Pike","descricao":"Robert C. Pike (1956) é um engenheiro de software e escritor. Foi responsável pelo projeto dos sistemas operacionais Plan 9 e Inferno, e da linguagem de programação Limbo, quando trabalhou na equipe que desenvolveu o sistema Unix, nos laboratórios Bell. Ele também trabalhou no terminal gráfico Blit, após ter escrito o primeiro sistema de janelas para o Unix, em 1981. Também escreveu editores de texto como o Sam e o Acme, que continuam em desenvolvimento e ainda hoje são utilizados. Com Ken Thompson criou o padrão UTF-8. Atualmente Pike trabalha para a empresa Google.","email":"RobPike@exemplotdc.com.br","site":"https://pt.wikipedia.org/wiki/Rob_Pike","especialidade":"engenheiro de software","data_nascimento":"1956-01-21T00:00:00"}
{"index":{}}
{"nome":"Steve Jobs","descricao":"Steven Paul Jobs foi um magnata americano dos negócios, designer industrial, investidor e proprietário de mídia. Ele foi o presidente do conselho, diretor executivo (CEO) e cofundador da Apple Inc .; o presidente e acionista majoritário da Pixar; membro do conselho de diretores da The Walt Disney Company após a aquisição da Pixar; e o fundador, presidente e CEO da NeXT. Jobs é amplamente reconhecido como o pioneiro da revolução do computador pessoal das décadas de 1970 e 1980, junto com seu primeiro parceiro de negócios e co-fundador da Apple, Steve Wozniak.","email":"Steve-Jobs@exemplotdc.com.br","site":"https://en.wikipedia.org/wiki/Steve_Jobs","especialidade":"engenheiro de software","data_nascimento":"1955-01-21T00:00:00"}


POST /livros/_bulk
{"index":{}}
{}


POST /artigos/_bulk
{"index":{}}
{}
```


### Realizando queries

```

GET /busca-geral/_search

GET /busca-geral/_search
{
  "query": {
    "match": {
      "todos": "Berthier"
    }
  }
}

GET /busca-geral/_search
{
  "query": {
    "match": {
      "todos": "recuperacao da informação"
    }
  }
}

GET /busca-geral/_search
{
  "query": {
    "range": {
      "avaliacao": {
        "gte": 2,
        "lte": 9
      }
    }
  }
}

GET /busca-geral/_search
{
  "query": {
    "query_string": {
        "query":"informação",
        "fields": ["todos"]
    }
  }
}

```