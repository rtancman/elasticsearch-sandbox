# [ElasticBNU - Criando um buscador utilizando o Elasticsearch](/kibana/74-python-devops-floripa-na-rd/README.md)
74º Python + DevOps Floripa na RD
- Versão utilizada 8.13.2
- Este material utiliza o Docker para rodar os comandos

## Docker
- Instalação
- Docker para rodar os comandos

---

## Docker

### Instalação

Para instalar o docker em sua máquina, recomendo utilizar seguir os passos da documentação oficial no link https://docs.docker.com/engine/install/.

### Docker para rodar os comandos

```bash
docker-compose up -d
```

Verificar se tudo esta rodando conforme o esperado:
```bash
docker container ls
```

Após verificar que tudo esta rodando, acessar o Kibana atraves da url http://localhost:5601/