# elastic-engineer

Plano de estudos para o [exame de certificação da Elastic](https://www.elastic.co/training/elastic-certified-engineer-exam).
- Versão utilizada 8.1
- Este material utiliza o Docker para rodar os comandos

## Overview

### [Docker](/kibana/elastic-engineer/Docker.md)
- Instalação
- Docker para rodar os comandos

### [Data Management](/kibana/elastic-engineer/DataManagement.md)
- Define an index that satisfies a given set of requirements
- Define and use an index template for a given pattern that satisfies a given set of requirements
- Define and use a dynamic template that satisfies a given set of requirements
- Define an Index Lifecycle Management policy for a time-series index
- Define an index template that creates a new data stream

### Searching Data
- Write and execute a search query for terms and/or phrases in one or more fields of an index
- Write and execute a search query that is a Boolean combination of multiple queries and filters
- Write an asynchronous search
- Write and execute metric and bucket aggregations
- Write and execute aggregations that contain sub-aggregations
- Write and execute a query that searches across multiple clusters
- Write and execute a search that utilizes a runtime field

### Developing Search Applications
- Highlight the search terms in the response of a query
- Sort the results of a query by a given set of requirements
- Implement pagination of the results of a search query
- Define and use index aliases
- Define and use a search template

### Data Processing
- Define a mapping that satisfies a given set of requirements
- Define and use a custom analyzer that satisfies a given set of requirements
- Define and use multi-fields with different data types and/or analyzers
- Use the Reindex API and Update By Query API to reindex and/or update documents
- Define and use an ingest pipeline that satisfies a given set of requirements, including the use of Painless to modify documents
- Define runtime fields to retrieve custom values using Painless scripting

### Cluster Management
- Diagnose shard issues and repair a cluster's health
- Backup and restore a cluster and/or specific indices
- Configure a snapshot to be searchable
- Configure a cluster for cross-cluster search
- Implement cross-cluster replication