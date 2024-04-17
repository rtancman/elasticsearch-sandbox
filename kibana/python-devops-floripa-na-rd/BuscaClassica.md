# [ElasticBNU - Criando um buscador utilizando o Elasticsearch](/kibana/74-python-devops-floripa-na-rd/README.md)
74º Python + DevOps Floripa na RD
- Versão utilizada 8.13.2
- Este material utiliza o Docker para rodar os comandos

## Busca Clássica
- Indices, mappings e settings
- Analyzers e tokenizers
- Busca clássica

---

## Busca Clássica

```

GET /_analyze
{
  "tokenizer": "standard",
  "filter": [
    "lowercase",
    "asciifolding",
    {
      "type": "stop",
      "stopwords": "_brazilian_"
    }
  ],
  "text": "Criando um buscador utilizando o Elasticsearch na XVIII SEMINCO"
}

```

### Indices, mappings e settings

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

### Analyzers e tokenizers

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
  "tokenizer" : "standard",
  "filter" : [
    "lowercase",
    "asciifolding"
  ],
  "text" : "Texto com acentos e outros caracteres. Aqui: imprescindível, diligência, índices, ações"
}

```

#### Stop words Analyzers e tokenizers

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

#### Sinônimos

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


### Busca clássica

#### Criando documentos

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
{"titulo": "Recuperação de Informação: Conceitos e Tecnologia das Máquinas de Busca", "descricao": "Diariamente, mais de 1 bilhão de pessoas recorrem às máquinas de busca para encontrar informações. Mas o que está por trás dessa tecnologia? Ricardo Baeza-Yates e Berthier Ribeiro-Neto respondem a esse questionamento neste livro, que é uma introdução integral e atualizada dos conceitos-chave de RI e das tecnologias subjacentes às máquinas de busca. Desde a análise (parse) até a indexação, do agrupamento à classificação, da recuperação à geração do ranking, da realimentação até a avaliação da recuperação, todos os conceitos mais importantes são cuidadosamente introduzidos e exemplificados.", "assunto": "Recuperação da Informação", "autores": ["Ricardo Baeza-Yates", "Berthier Ribeiro-Neto"], "avaliacao": 10}
{"index":{}}
{"titulo": "Manual de Algoritmos e Estruturas de Dados em Pascal e C", "descricao": "Esta segunda edição reúne muitos algoritmos úteis e suas estruturas de dados associadas em uma referência única e útil, apresentando uma nova seção sobre algoritmos de manipulação de texto e cobertura expandida de algoritmos aritméticos. Cada algoritmo é codificado em C e Pascal.", "assunto": ["Algoritmos", "Estruturas de Dados", "Pascal", "C"], "autores": ["Ricardo Baeza-Yates", "Gaston Gonnet"], "avaliacao": 7}
{"index":{}}
{"titulo": "O ambiente de programação Unix", "descricao": "Projetado para usuários inexperientes e experientes, este livro descreve o ambiente de programação UNIX® e a filosofia em detalhes. TÓPICOS-CHAVE: Os leitores obterão uma compreensão não apenas de como usar o sistema, seus componentes e os programas, mas também como eles se encaixam no ambiente total.", "assunto": "Unix", "autores": ["Brian W. Kernighan", "Rob Pike"], "avaliacao": 10}
{"index":{}}
{"titulo": "A Prática da Programação", "descricao": "A prática de programação é mais do que apenas escrever código. Os programadores também devem avaliar as compensações, escolher entre alternativas de design, depurar e testar, melhorar o desempenho e manter o software escrito por eles e outros. Ao mesmo tempo, eles devem se preocupar com questões como compatibilidade, robustez e confiabilidade, ao mesmo tempo em que atendem às especificações. A Prática de Programação cobre todos esses tópicos e muito mais. Este livro está repleto de conselhos práticos e exemplos do mundo real em C, C ++, Java e uma variedade de linguagens de propósito especial.", "assunto": "Programação", "autores": ["Brian W. Kernighan", "Rob Pike"], "avaliacao": 9.2}
{"index":{}}
{"titulo": "Steve Jobs: The Exclusive Biography", "descricao": "Com base em mais de quarenta entrevistas com Steve Jobs conduzidas ao longo de dois anos - bem como entrevistas com mais de 100 membros da família, amigos, adversários, concorrentes e colegas - Walter Isaacson escreveu uma história fascinante da vida na montanha-russa e extremamente intensa personalidade de um empreendedor criativo cuja paixão pela perfeição e ímpeto feroz revolucionou seis setores: computadores pessoais, filmes animados, música, telefones, tablets e editoração digital. O retrato de Isaacson tocou milhões de leitores.", "assunto": "Biografia", "autores": "Walter Isaacson", "avaliacao": 10}


POST /artigos/_bulk
{"index":{}}
{"titulo":"Bias on the Web","descricao":"Nossa tendência humana inerente de favorecer uma coisa ou opinião em detrimento de outra se reflete em todos os aspectos de nossas vidas, criando preconceitos latentes e evidentes em relação a tudo o que vemos, ouvimos e fazemos.","conteudo":"Nossa tendência humana inerente de favorecer uma coisa ou opinião em detrimento de outra se reflete em todos os aspectos de nossas vidas, criando preconceitos latentes e evidentes em relação a tudo o que vemos, ouvimos e fazemos. Qualquer remédio para o preconceito deve começar com a consciência de que existe um preconceito; por exemplo, a maioria das sociedades maduras aumenta a conscientização sobre o preconceito social por meio de programas de ação afirmativa e, embora a conscientização por si só não alivie completamente o problema, ajuda a nos guiar em direção a uma solução. O preconceito na Web reflete preconceitos sociais e internos dentro de nós, emergindo de maneiras mais sutis. Este artigo tem como objetivo aumentar a consciência sobre os efeitos potenciais impostos a todos nós por meio do preconceito presente no uso e no conteúdo da Web. Devemos, portanto, considerá-lo e explicá-lo no projeto de sistemas da Web que realmente atendam às necessidades das pessoas. Bias está intrinsecamente inserido na cultura e na história desde o início dos tempos. No entanto, devido ao aumento dos dados digitais, agora eles podem se espalhar mais rápido do que nunca e atingir muito mais pessoas. Isso fez com que o enviesamento de big data se tornasse um tópico de tendência e polêmico nos últimos anos. As minorias, especialmente, sentiram os efeitos prejudiciais do viés de dados ao perseguir objetivos de vida, com resultados regidos principalmente por algoritmos, de empréstimos hipotecários à personalização de publicidade.24 Embora os obstáculos que enfrentam continuem a ser um obstáculo importante, o viés afeta a todos nós, embora muito de o tempo em que não temos conhecimento de sua existência ou como pode (negativamente) influenciar nosso julgamento e comportamento. A Web é o canal de comunicação mais proeminente da atualidade, bem como um lugar para onde convergem nossos preconceitos. Como as mídias sociais estão cada vez mais no centro da vida diária, elas nos expõem a influenciadores que talvez não tivéssemos encontrado antes. Isso torna a compreensão e o reconhecimento de preconceitos na Web mais essenciais do que nunca. Meu principal objetivo aqui é, portanto, aumentar o nível de conscientização para todos os vieses da web. A percepção do preconceito nos ajudaria a projetar melhores sistemas baseados na Web, bem como sistemas de software em geral.","autores":"Ricardo Baeza-Yates","avaliacao":10}
{"index":{}}
{"titulo":"Algoritmos: um artigo em espanhol sobre algoritmos básicos, incluindo alguns problemas simples e agradáveis.","descricao":"Algoritmo, de acordo com a Royal Academy, é um conjunto ordenado e finito de operações que permite encontre a solução para qualquer problema. Exemplos simples de algoritmos são uma receita para cozinhar ou as instruções para montar uma bicicleta.","conteudo":"Algoritmo, de acordo com a Royal Academy, é um conjunto ordenado e finito de operações que permite encontre a solução para qualquer problema. Exemplos simples de algoritmos são uma receita para cozinhar ou as instruções para montar uma bicicleta. Os primeiros algoritmos registrados datam de Babylon, originou-se na matemática como um método de resolver um problema usando um sequência de cálculos mais simples. Esta palavra tem sua origem no nome de um famoso Matemático e estudioso árabe do século 9, Al-Khorezmi, a quem também devemos as palavras figuras e álgebra (ver anexo). Atualmente o algoritmo é usado para nomear a sequência de etapas a seguir para resolver um problema usando um computador (computador). Por esta razão, algoritmo ou ciência de algoritmos, é um dos pilares da ciência da computação (ciência da computação em inglês). Neste artigo, veremos diferentes tipos de algoritmos e diferentes técnicas para resolver problemas em através de vários exemplos, muitos deles não computacionais. Todos os exemplos resolvem variantes de um problema genérico: a busca de informações, dilema que vivemos diariamente. O o objetivo final será encontrar o algoritmo que usa menos operações ou gasta menos recursos, dependendo do caso. Design e análise de algoritmos O desenvolvimento de um algoritmo tem várias etapas (veja a figura). Primeiro, o problema é modelado precisa resolver, então a solução é desenhada, então é analisada para determinar seu grau de correção e eficiência, e é finalmente traduzido em instruções em um programação que um computador irá entender. O modelo especifica todas as suposições sobre o dados de entrada e a capacidade computacional do algoritmo. O design é baseado em diferentes métodos de solução de problemas, muitos dos quais serão apresentados posteriormente. Para o análise de um algoritmo, devemos estudar quantas operações são realizadas para resolver um dificuldade. Se tivermos um problema x, diremos que o algoritmo realiza operações A (x) (custo de algoritmo). O valor máximo de A (x) é denominado pior caso e o mínimo, melhor caso. No Na prática, o pior caso é interessante, pois representa um limite superior ao custo do algoritmo. Sem No entanto, em muitos problemas, isso ocorre com pouca frequência ou existe apenas na teoria. Então estuda a média de A (x), para a qual é necessário definir a probabilidade de que cada x ocorra, p (x), e calcule a soma ponderada de p (x) por A (x). Embora esta medição seja muito mais realista, muitas vezes é difícil calcular e outras vezes não podemos nem definir p (x) porque não sabemos ou realidade ou é muito difícil modelar. Se pudermos mostrar que não há algoritmo que realizar menos operações para resolver um problema, o algoritmo é considerado ótimo, seja em pior caso ou caso médio, dependendo do modelo. Por este motivo, a análise realimenta para projetar, para melhorar o algoritmo.","autores":"Ricardo Baeza-Yates","avaliacao":8.9}
{"index":{}}
{"titulo":"Cache de dois níveis com preservação de classificação para mecanismos de pesquisa escalonáveis","descricao":"Apresentamos um esquema de armazenamento em cache eficaz que reduz os requisitos de computação e E / S de um mecanismo de pesquisa da Web sem alterar suas características de classificação. A novidade é um esquema de cache de dois níveis que combina simultaneamente resultados de consulta em cache e listas invertidas em cache em um mecanismo de busca de casos reais.","conteudo":"Apresentamos um esquema de armazenamento em cache eficaz que reduz os requisitos de computação e E / S de um mecanismo de pesquisa da Web sem alterar suas características de classificação. A novidade é um esquema de cache de dois níveis que combina simultaneamente resultados de consulta em cache e listas invertidas em cache em um mecanismo de busca de casos reais. Um conjunto de consultas de log é usado para medir e comparar o desempenho e a escalabilidade do mecanismo de pesquisa sem cache, com o cache para resultados da consulta, com o cache para listas invertidas e com o cache de dois níveis. Resultados experimentais mostram que o cache de dois níveis é superior e permite aumentar o número máximo de consultas processadas por segundo em um fator de três, preservando o tempo de resposta. Esses resultados são novos, não foram relatados antes e demonstram a importância de esquemas de cache avançados para mecanismos de pesquisa de casos reais.","autores":["Patricia Correia Saraiva","Edleno Silva de Moura","Nivio Ziviani","Wagner Meira","Rodrigo Fonseca","Berthier Ribeiro-Neto"],"avaliacao":9.2}
{"index":{}}
{"titulo":"Classificação de pesquisa eficiente em redes sociais","descricao":"Anais da décima sexta conferência ACM sobre Conferência sobre gestão de informação e conhecimento","conteudo":"Em redes sociais como Orkut, www. orkut. com, uma grande parte das consultas de usuários referem-se a nomes de outras pessoas. Na verdade, mais de 50% das consultas no Orkut são sobre nomes de outros usuários, com uma média de 1,8 termos por consulta. Além disso, os usuários geralmente procuram pessoas com quem mantêm relacionamento na rede. Esses relacionamentos podem ser modelados como arestas em um gráfico de amizade, um gráfico no qual os nós representam os usuários. Nesse contexto, o ranking de busca pode ser modelado como uma função que depende das distâncias entre os usuários no gráfico, mais especificamente, dos caminhos mais curtos no gráfico de amizade. No entanto, a aplicação dessa ideia à classificação não é direta porque o grande tamanho das redes sociais modernas (dezenas de milhões de usuários) impede o cálculo eficiente dos caminhos mais curtos no momento da consulta. Superamos isso criando uma fórmula de classificação que estabelece um equilíbrio entre","autores":["Monique V Vieira","Bruno M Fonseca","Rodrigo Damazio","Paulo B Golgher","Davi de Castro Reis","Berthier Ribeiro-Neto"],"avaliacao":7.9}
{"index":{}}
{"titulo":"Usando regras de associação para descobrir consultas relacionadas a mecanismos de pesquisa","descricao":"Apresentamos um método para geração automática de sugestões de consultas relacionadas enviadas aos motores de busca da web.","conteudo":"Apresentamos um método para geração automática de sugestões de consultas relacionadas enviadas aos motores de busca da web. O método extrai informações do registro de consultas anteriores enviadas para mecanismos de pesquisa usando algoritmos para mineração de regras de associação. Os resultados experimentais foram realizados em um log contendo mais de 2,3 milhões de consultas submetidas a um motor de busca comercial, dando sugestões corretas em 90,5% das 5 principais sugestões apresentadas para consultas comuns extraídas de um log real.","autores":["Bruno M Fonseca","Paulo Braz Golgher","Edleno Silva de Moura","Nivio Ziviani"],"avaliacao":9.9}
{"index":{}}
{"titulo":"Fontes Go","descricao":"O kit de ferramentas de interface do usuário experimental que está sendo construído em golang.org/x/exp/shiny inclui vários elementos de texto, mas há um problema em testá-los: qual fonte deve ser usada?","conteudo":"O kit de ferramentas de interface do usuário experimental que está sendo construído em golang.org/x/exp/shiny inclui vários elementos de texto, mas há um problema em testá-los: qual fonte deve ser usada? A resposta a essa pergunta nos levou ao anúncio de hoje, o lançamento de uma família de fontes WGL4 TrueType de alta qualidade, criada pela Bigelow & Holmes type foundry especificamente para o projeto Go. A família da fonte, chamada Go (naturalmente), inclui faces de largura fixa e proporcional em renderizações normal, negrito e itálico. As fontes foram testadas para usos técnicos, particularmente programação. O código-fonte Go parece particularmente bom quando exibido em fontes Go, como o próprio nome indica, com coisas como caracteres de pontuação facilmente distinguíveis e operadores alinhados e colocados de forma consistente:","autores":["Nigel Tao","Chuck Bigelow","Rob Pike"],"avaliacao":8.9}


```

#### Realizando queries

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
    "query_string": {
        "query":"Algoritmos Recuperação",
        "fields": ["todos"]
    }
  }
}

GET /busca-artigos-livros/_search
{
  "query": {
    "bool": {
      "filter": {
        "range": {
          "avaliacao": {
            "gte": 8,
            "lte": 10
          }
        }
      },
      "must": {
        "query_string": {
          "query": "Algoritmos -Recuperação",
          "fields": [
            "todos"
          ]
        }
      }
    }
  }
}

GET /busca-geral/_search
{
  "query": {
    "query_string": {
        "query":"recuperação",
        "fields": ["todos"]
    }
  },
  "highlight": {
    "fields" : {
      "todos" : { "pre_tags" : ["<strong>"], "post_tags" : ["</strong>"] }
    }
  }
}
```