# [# Elastic - Curso Rápido](/kibana/elastic-bnu/curso-rapido/README.md)
- Versão utilizada 8.12.2
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