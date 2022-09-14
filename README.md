# ThinkWiki

Wikipédia para todas as comunidades

## 1. Sobre

ThinkWiki é um projeto desenvolvido no quinto módulo do curso de Desenvolvimento Web Full Stack da Kenzie Academy Brasil. A aplicação é uma wikipédia onde centraliza acervos de diversos nichos a fim de aproximar comunidades. Sendo assim, nosso objetivo é criar uma API para manipular os conteúdos e as regras de negócio.

## 2. Problema a solucionar

Buscamos proporcionar entretenimento e informações sobre diversos assuntos.

## 3. Documentação da API

[link para doc]

## 4. Tecnologias

- _Python_
- _Django_
- _Django Rest-Framework_
- _PostgreSQL_

## 5. Instalação

### 5.1 Requisitos

- Python a partir da versão 3.10.4
- Gerenciador de pacotes PIP
- Banco de dados PostgreSQL

### 5.2 Instalação

5.2.1 - Crie um novo banco de dados chamado thinkwiki no PostgreSQL

5.2.2 - Ao clonar o repositório, crie um ambiente virtual na pasta do projeto:

`python -m venv venv`

5.2.3 - Rode o seguinte comando para ativar o ambiente virtual:

`source venv/bin/activate`

5.2.4 - Instale as dependências do projeto utilizando o PIP:

`pip install -r requirements.txt`

5.2.5 - Crie um arquivo na raiz do projeto chamado `.env` e faça as configurações das variáveis de ambiente conforme o que está disposto no `.env.example` do projeto:

```
SECRET_KEY=
POSTGRES_PASSWORD=
POSTGRES_USER=
POSTGRES_DB=
HOST=
PORT=
```

5.2.6 - Para rodar o projeto utilize o comando abaixo:

`python manage.py runserver`

## 6. Desenvolvedores

- <a name="andrea" href="https://www.linkedin.com/in/melodea/" target="_blank">Andrea Melo</a>
- <a name="douglas" href="https://www.linkedin.com/in/douglasramires/" target="_blank">Douglas Leão</a>
- <a name="gisela" href="https://www.linkedin.com/in/gisela-mariano/" target="_blank">Gisela Mariano</a>
- <a name="luis" href="https://www.linkedin.com/in/luis-henrique-mota/" target="_blank">Luis H. Mota</a>
- <a name="paulo" href="https://www.linkedin.com/in/paulo-henrique-moro-dos-santos/" target="_blank">Paulo Moro</a>
- <a name="victoria" href="https://www.linkedin.com/in/victoriavianx/" target="_blank">Victoria Viana</a>
