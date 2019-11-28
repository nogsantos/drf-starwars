# Starwars

[![Build Status](https://travis-ci.org/nogsantos/drf-starwars.svg?branch=master)](https://travis-ci.org/nogsantos/drf-starwars)

Desenvolver uma API que contenha os dados dos planetas.

**Requisitos:**

- A API deve ser REST

Para cada planeta, os seguintes dados devem ser obtidos do banco de dados da aplicação, sendo inserido manualmente:

- Nome
- Clima
- Terreno

Para cada planeta também devemos ter a quantidade de aparições em filmes, que podem ser obtidas pela API pública do Star Wars: https://swapi.co/

**Funcionalidades desejadas:**

- Adicionar um planeta com
  - nome
  - clima
  - terreno
- Listar planetas
- Buscar por nome
- Buscar por ID
- Remover planeta


## Setup

**Desenvolvimento**

```console
pip install -r requirements-dev.txt
cp contrib/env.sample .env
```

**Coverage**

Visualizar relatório de cobertura de testes

```console
coverage run --source='starwars' manage.py test --noinput --failfast --parallel
coverage report
```
