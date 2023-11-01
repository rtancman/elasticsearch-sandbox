# [elastic-engineer](/kibana/elastic-engineer/README.md)

Plano de estudos para o [exame de certificação da Elastic](https://www.elastic.co/training/elastic-certified-engineer-exam).
- Versão utilizada 8.1
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