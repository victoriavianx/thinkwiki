# ThinkWiki

Wikipédia para todas as comunidades

## 1. Sobre

ThinkWiki é um projeto desenvolvido no quinto módulo do curso de Desenvolvimento Web Full Stack da Kenzie Academy Brasil. A aplicação é uma wikipédia onde centraliza acervos de diversos nichos a fim de aproximar comunidades. Sendo assim, nosso objetivo é criar uma API para manipular os conteúdos e as regras de negócio.

## 2. Problema a solucionar

Buscamos proporcionar entretenimento e informações sobre diversos assuntos.

## 3. Features Gerais

  - Cadastro e login de usuário;
  - Criação de posts;
  - Adição de colaboradores em posts;
  - Curtir posts;
  - Comentar em posts;
  - Seguir categorias;
  - Adicionar amigos.

## 4. Tecnologias

- _Python_
- _Django_
- _Django Rest-Framework_
- _Python-Dotenv_
- _Coverage_
- _APSchedule_
- _Friendship_
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


# 7. Documentação ThinkWiki

## Insomnia:

Faça download com o modelo do insomnia contendo as variáveis de ambiente, todas as rotas e exemplos de requisições.

[Baixe Nosso Workspace no Insomnia](https://insomnia.rest/run?label=ThinkWiki&uri=https%3A%2F%2Finsomnia-thinkwiki.com)

---

# Rotas:

- **Base Url:** [https://thinkwiki.herokuapp.com/api](https://thinkwiki.herokuapp.com/api)

## 🔖 Users:

### **Criação de Usuário**:

**Endpoint:** `/users/`

**Método:** POST

**Headers:**

- Content-Type application/json

**Nível de acesso:** Livre

**Sobre a rota:** Rota para criação de um novo usuário.

**O que deve ser enviado:**

```json
{
  "username": "johndoe",
  "email": "johndoe@mail.com",
  "password": "1234",
  "first_name": "john",
  "last_name": "doe"
}
```

**O que será retornado em caso de sucesso:**

```json
{
  "id": "dee334b1-e2f0-4624-b7ed-cc28bbdd6b6a",
  "username": "johndoe",
  "email": "johndoe@mail.com",
  "last_login": null,
  "is_superuser": false,
  "date_joined": "2022-09-08T19:20:05.159669Z",
  "first_name": "john",
  "last_name": "doe"
}
```

---

### **Login**:

**Endpoint:** `/users/`

**Método:** POST

**Headers:**

- Content-Type application/json

**Nível de acesso:** Livre

**Sobre a rota:** Rota para login de usuários.

**O que deve ser enviado:**

```json
{
  "username": "johndoe",
  "password": "1234"
}
```

**O que será retornado em caso de sucesso:**

```json
{
  "token": "bf9310b8b19557e9e5fc108d42f3a6778afb6d25"
}
```

---

### **Listar Usuários**:

**Endpoint:** `/users/`

**Método:** GET

**Headers:** None

**Nível de acesso:** Livre

**Sobre a rota:** Rota para listar todos os usuários ativos e algumas informações sobre os mesmos.

**O que será retornado em caso de sucesso:**

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "3227460f-1e72-48e4-a932-ef106ed4e617",
      "username": "johndoe",
      "email": "johndoe@mail.com",
      "last_login": null,
      "is_superuser": false,
      "is_active": true,
      "date_joined": "2022-09-08T19:20:05.159669Z",
      "first_name": "john",
      "last_name": "doe"
    }
  ]
}
```

---

### **Listar Usuários Por um Administrador**:

**Endpoint:** `/users/management/`

**Método:** GET

**Headers:**

- Authorization Token <token_do_usuário>

**Nível de acesso:** Restrito para administradores

**Sobre a rota:** Rota para listar todos os usuários ativos/inativos e algumas informações sobre os mesmos.

**O que será retornado em caso de sucesso:**

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "3227460f-1e72-48e4-a932-ef106ed4e617",
      "username": "peterparker",
      "email": "peterparker@mail.com",
      "last_login": null,
      "is_superuser": false,
      "is_active": false,
      "date_joined": "2022-09-08T19:20:05.159669Z",
      "first_name": "peter",
      "last_name": "parker"
    }
  ]
}
```

---

### **Listar Perfil de Usuário**:

**Endpoint:** `/users/<id_user>/`

**Método:** GET

**Headers:** None

**Nível de acesso:** Livre

**Sobre a rota:** Rota para listar as informações detalhadas sobre um usuário

**O que será retornado em caso de sucesso:**

```json
{
  "id": "a39fdc91-c7bc-4677-a8de-34fab3cdb6a3",
  "username": "johdoe",
  "email": "johdoe@mail.com",
  "first_name": "john",
  "last_name": "doe",
  "is_active": true,
  "is_superuser": false,
  "posts": [
    {
      "id": "ec74c7fd-be52-4b84-af5a-5554ded129cd",
      "title": "about movies",
      "updated_at": "2022-09-08T23:52:18.935360Z",
      "created_at": "2022-09-08T23:52:18.935360Z",
      "category": {
        "id": "3dab40da-3fdb-4d91-97cf-0f7820f0f57f",
        "name": "movies"
      },
      "likes": 0
    }
  ],
  "collab_posts": [
    {
      "id": "9eac2726-40b6-4942-9a0e-5c583f6c56cd",
      "title": "about games",
      "updated_at": "2022-09-08T23:51:31.967865Z",
      "created_at": "2022-09-08T23:51:31.967865Z",
      "category": {
        "id": "7f5e7510-6416-45bd-a240-0f20424d7c92",
        "name": "games"
      },
      "likes": 0
    }
  ],
  "liked_posts": [
    {
      "id": "ec74c7fd-be52-4b84-af5a-5554ded129cd",
      "title": "about movies",
      "updated_at": "2022-09-08T23:52:18.935360Z",
      "created_at": "2022-09-08T23:52:18.935360Z",
      "category": {
        "id": "3dab40da-3fdb-4d91-97cf-0f7820f0f57f",
        "name": "movies"
      },
      "likes": 0
    }
  ],
  "date_joined": "2022-09-08T23:15:48.249512Z",
  "last_login": null
}
```

---

### **Atualizar Usuário**:

**Endpoint:** `/users/<id_user>/`

**Método:** PATCH

**Headers:**

- Content-Type application/json
- Authorization Token <token_do_usuário>

**Nível de acesso:** Restrito para usuário dono do perfil e administradores

**Sobre a rota:** Rota para atualizar/editar as informações de um usuário. As informações que podem ser editadas são: username, email, first_name, last_name.

**Exemplo de requisição que pode ser enviada:**

```json
{
  "username": "johndoe updated",
  "first_name": "john updated"
}
```

**O que será retornado em caso de sucesso:**

```json
{
  "id": "dee334b1-e2f0-4624-b7ed-cc28bbdd6b6a",
  "username": "johndoe updated",
  "email": "johndoe@mail.com",
  "last_login": null,
  "is_superuser": false,
  "date_joined": "2022-09-08T19:20:05.159669Z",
  "first_name": "john updated",
  "last_name": "doe"
}
```

---

### **Deletar Usuário (Soft Delete)**:

**Endpoint:** `/users/management/<id_user>/`

**Método:** PATCH

**Headers:**

- Content-Type application/json
- Authorization Token <token_do_usuário>

**Nível de acesso:** Restrito para usuário dono do perfil e administradores

**Sobre a rota:** Rota ativar/desativar um usuário.

**O que deve ser enviado:**

```json
{
  "is_active": false
}
```

**O que será retornado em caso de sucesso:**

```json
{
  "id": "dee334b1-e2f0-4624-b7ed-cc28bbdd6b6a",
  "username": "johndoe updated",
  "email": "johndoe@mail.com",
  "last_login": null,
  "is_superuser": false,
  "date_joined": "2022-09-08T19:20:05.159669Z",
  "first_name": "john updated",
  "last_name": "doe"
}
```

---

## 🔖 Categories:

### **Criar Categoria**:

**Endpoint:** `/categories/`

**Método:** POST

**Headers:**

- Content-Type application/json
- Authorization Token <token_do_usuário>

**Nível de acesso:** Restrito para administradores

**Sobre a rota:** Rota para criação de categoria.

**O que deve ser enviado:**

```json
{
  "name": "movies"
}
```

**O que será retornado em caso de sucesso:**

```json
{
  "id": "3dab40da-3fdb-4d91-97cf-0f7820f0f57f",
  "name": "movies"
}
```

---

### **Seguir/Parar de Seguir Categoria:**

**Endpoint:** `/categories/follow/<id_category>/`

**Método:** PATCH

**Headers:**

- Authorization Token <token_do_usuário>

**Nível de acesso:** Restrito para usuários logados

**Sobre a rota:** Rota para seguir categoria.

**O que deve ser enviado:**

```
No Body
```

**O que será retornado em caso de sucesso:**

```json
Status 204 - No Content
```

---

### **Listar Categorias:**

**Endpoint:** `/categories/`

**Método:** GET

**Headers:** None

**Nível de acesso:** Livre

**Sobre a rota:** Rota para listagem de categorias.

**O que será retornado em caso de sucesso:**

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "3dab40da-3fdb-4d91-97cf-0f7820f0f57f",
      "name": "movies"
    }
  ]
}
```

---

### **Listar Categorias Seguidas:**

**Endpoint:** `/categories/follow/`

**Método:** GET

**Headers:** None

**Nível de acesso:** Restrito para usuários logados

**Sobre a rota:** Rota listagem de categorias seguidas.

**O que será retornado em caso de sucesso:**

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "3dab40da-3fdb-4d91-97cf-0f7820f0f57f",
      "name": "movies"
    }
  ]
}
```

---

### **Listar Uma Categoria:**

**Endpoint:** `/categories/<id_category>/`

**Método:** GET

**Headers:** None

**Nível de acesso:** Livre

**Sobre a rota:** Rota para criação de categoria.

**O que será retornado em caso de sucesso:**

```json
{
  "id": "3dab40da-3fdb-4d91-97cf-0f7820f0f57f",
  "name": "movies"
}
```

---

### **Atualizar Uma Categoria:**

**Endpoint:** `/categories/<id_category>/`

**Método:** PATCH

**Headers:**

- Content-Type application/json
- Authorization Token <token_do_usuário>

**Nível de acesso:** Restrito para administradores

**Sobre a rota:** Rota para atualização/edição de uma categoria.

**O que deve ser enviado:**

```json
{
  "name": "movies updated"
}
```

**O que será retornado em caso de sucesso:**

```json
{
  "id": "3dab40da-3fdb-4d91-97cf-0f7820f0f57f",
  "name": "movies updated"
}
```

---

### **Deletar Uma Categoria:**

**Endpoint:** `/categories/<id_category>/`

**Método:** DELETE

**Headers:**

- Authorization Token <token_do_usuário>

**Nível de acesso:** Restrito para administradores

**Sobre a rota:** Rota para deleção de uma categoria.

**O que será retornado em caso de sucesso:**

```
Status 204 - No Content
```

---

## 🔖 Posts:

### **Criar Um Post:**

**Endpoint:** `/posts/`

**Método:** POST

**Headers:**

- Content-Type application/json
- Authorization Token <token_do_usuário>

**Nível de acesso:** Restrito para usuários logados

**Sobre a rota:** Rota para criação de um post.

**O que deve ser enviado:**

```json
{
  "title": "about movies",
  "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
  "is_editable": true,
  "category": "3dab40da-3fdb-4d91-97cf-0f7820f0f57f"
}
```

**O que será retornado em caso de sucesso:**

```json
{
  "id": "3385c646-052b-499b-b58c-40f1f3a7a516",
  "title": "about movies",
  "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
  "is_editable": true,
  "created_at": "2022-09-08T23:48:21.323087Z",
  "updated_at": "2022-09-08T23:48:21.323087Z",
  "category": {
    "id": "3dab40da-3fdb-4d91-97cf-0f7820f0f57f",
    "name": "movies"
  }
}
```

---

### **Curtir/Descurtir Um Post:**

**Endpoint:** `/posts/like/<id_post>/`

**Método:** PATCH

**Headers:**

- Authorization Token <token_do_usuário>

**Nível de acesso:** Restrito para usuários logados

**Sobre a rota:** Rota para curtir ou descurtir um post.

**O que deve ser enviado:**

```
No body
```

**O que será retornado em caso de sucesso:**

```
Status 204 - No Content
```

---

### **Adicionar Colaborador Em Um Post:**

**Endpoint:** `/posts/<id_post>/<id_collaborator>/`

**Método:** PATCH

**Headers:**

- Authorization Token <token_do_usuário>

**Nível de acesso:** Restrito para usuário dono do post e administradores

**Sobre a rota:** Rota para adição de colaboradores em um post.

**O que deve ser enviado:**

```
No Body
```

**O que será retornado em caso de sucesso:**

```json
{
  "id": "3385c646-052b-499b-b58c-40f1f3a7a516",
  "title": "about movies",
  "updated_at": "2022-09-08T23:48:21.323087Z",
  "created_at": "2022-09-08T23:48:21.323087Z",
  "post_collab": [
    {
      "id": "f9456d95-b092-481a-aa0b-3c22165db0b7",
      "username": "janedoe"
    }
  ]
}
```

---

### **Listar Posts:**

**Endpoint:** `/posts/`

**Método:** GET

**Headers:** None

**Nível de acesso:** Livre

**Sobre a rota:** Rota para listagem de todos os posts e as informações gerais do mesmo.

**O que será retornado em caso de sucesso:**

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "ec74c7fd-be52-4b84-af5a-5554ded129cd",
      "title": "about movie",
      "updated_at": "2022-09-08T23:52:18.935360Z",
      "created_at": "2022-09-08T23:52:18.935360Z",
      "owner": {
        "id": "dee334b1-e2f0-4624-b7ed-cc28bbdd6b6a",
        "username": "johndoe"
      },
      "category": {
        "id": "3dab40da-3fdb-4d91-97cf-0f7820f0f57f",
        "name": "movies"
      },
      "likes": 0
    }
  ]
}
```

---

### **Listar Um Post:**

**Endpoint:** `/posts/<id_post>/`

**Método:** GET

**Headers:** None

**Nível de acesso:** Livre

**Sobre a rota:** Rota para listagem de um post e as informações detalhadas do mesmo.

**O que será retornado em caso de sucesso:**

```json
{
  "id": "ec74c7fd-be52-4b84-af5a-5554ded129cd",
  "title": "about movie",
  "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
  "updated_at": "2022-09-08T23:52:18.935360Z",
  "created_at": "2022-09-08T23:52:18.935360Z",
  "owner": {
    "id": "dee334b1-e2f0-4624-b7ed-cc28bbdd6b6a",
    "username": "johndoe"
  },
  "category": {
    "id": "3dab40da-3fdb-4d91-97cf-0f7820f0f57f",
    "name": "movies"
  },
  "post_collab": [
    {
      "id": "f9456d95-b092-481a-aa0b-3c22165db0b7",
      "username": "janedoe"
    }
  ],
  "likes": [
    {
      "id": "f9456d95-b092-481a-aa0b-3c22165db0b7",
      "username": "janedoe"
    }
  ]
}
```

---

### **Listar Posts De Um Usuário:**

**Endpoint:** `/posts/users/<id_user>/`

**Método:** GET

**Headers:** None

**Nível de acesso:** Livre

**Sobre a rota:** Rota para listagem dos posts de um usuário e as informações gerais do mesmo.

**O que será retornado em caso de sucesso:**

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "ec74c7fd-be52-4b84-af5a-5554ded129cd",
      "title": "about movie",
      "updated_at": "2022-09-08T23:52:18.935360Z",
      "created_at": "2022-09-08T23:52:18.935360Z",
      "category": {
        "id": "3dab40da-3fdb-4d91-97cf-0f7820f0f57f",
        "name": "movies"
      },
      "likes": 0
    }
  ]
}
```

---

### **Listar Posts Por Categoria:**

**Endpoint:** `/posts/categories/<id_category>/`

**Método:** GET

**Headers:** None

**Nível de acesso:** Livre

**Sobre a rota:** Rota para listagem dos posts por categoria.

**O que será retornado em caso de sucesso:**

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "ec74c7fd-be52-4b84-af5a-5554ded129cd",
      "title": "about movie",
      "updated_at": "2022-09-08T23:52:18.935360Z",
      "created_at": "2022-09-08T23:52:18.935360Z",
      "owner": {
        "id": "dee334b1-e2f0-4624-b7ed-cc28bbdd6b6a",
        "username": "johndoe"
      },
      "category": {
        "id": "3dab40da-3fdb-4d91-97cf-0f7820f0f57f",
        "name": "movies"
      },
      "likes": 0
    }
  ]
}
```

---

### **Listar Posts Curtidos:**

**Endpoint:** `/posts/like/`

**Método:** GET

**Headers:**

- Authorization Token <token_do_usuário>

**Nível de acesso:** Restrito para usuários logados

**Sobre a rota:** Rota para listagem dos posts curtidos.

**O que será retornado em caso de sucesso:**

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "ec74c7fd-be52-4b84-af5a-5554ded129cd",
      "title": "about movie",
      "updated_at": "2022-09-08T23:52:18.935360Z",
      "created_at": "2022-09-08T23:52:18.935360Z",
      "owner": {
        "id": "dee334b1-e2f0-4624-b7ed-cc28bbdd6b6a",
        "username": "johndoe"
      },
      "category": {
        "id": "3dab40da-3fdb-4d91-97cf-0f7820f0f57f",
        "name": "movies"
      },
      "likes": 0
    }
  ]
}
```

---

### **Atualizar Um Post:**

**Endpoint:** `/posts/<id_post>/`

**Método:** PATCH

**Headers:**

- Content-Type application/json
- Authorization Token <token_do_usuário>

**Nível de acesso:** Restrito para usuário dono do post, colaboradores e administradores.

**Sobre a rota:** Rota para atualização/edição de um post. Os campos que podem ser editados são os mesmo da criação: title, content, is_editable, category

**Exemplo do que pode ser enviado:**

```json
{
  "title": "about movies is now about games",
  "category": "ab904c28-4f04-4098-84b1-18ec6003f844"
}
```

**O que será retornado em caso de sucesso:**

```json
{
  "id": "3385c646-052b-499b-b58c-40f1f3a7a516",
  "title": "about movies is now about games",
  "content": "Lorem ipsum dolor sit amet, consectetur adipiscing elit.",
  "is_editable": true,
  "created_at": "2022-09-08T23:48:21.323087Z",
  "updated_at": "2022-09-08T23:48:21.323087Z",
  "category": {
    "id": "ab904c28-4f04-4098-84b1-18ec6003f844",
    "name": "games"
  }
}
```

---

### **Deletar Um Post:**

**Endpoint:** `/posts/<id_post>/`

**Método:** DELETE

**Headers:**

- Authorization Token <token_do_usuário>

**Nível de acesso:** Restrito para usuário dono do post e administradores.

**Sobre a rota:** Rota para deleção de um post.

**O que será retornado em caso de sucesso:**

```
Status 204 - No Content
```

---

## 🔖 Comments:

### **Criar Um Comentário:**

**Endpoint:** `/posts/<id_post>/comments/`

**Método:** POST

**Headers:**

- Content-Type application/json
- Authorization Token <token_do_usuário>

**Nível de acesso:** Restrito para usuários logados

**Sobre a rota:** Rota para criação de um comentário em um post.

**O que deve ser enviado:**

```json
{
  "comment": "this is a cool comment! :)"
}
```

**O que será retornado em caso de sucesso:**

```json
{
  "id": "de0c99bd-9d6b-4699-a0f5-23c99d61bc63",
  "comment": "this is a cool comment! :)",
  "created_at": "2022-09-09T18:14:54.592766Z",
  "updated_at": "2022-09-09T18:14:54.592766Z"
}
```

---

### **Listar Comentários:**

**Endpoint:** `/posts/<id_post>/comments/`

**Método:** GET

**Headers:** None

**Nível de acesso:** Livre

**Sobre a rota:** Rota para listagem de comentários.

**O que será retornado em caso de sucesso:**

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "de0c99bd-9d6b-4699-a0f5-23c99d61bc63",
      "comment": "this is a cool comment! :)",
      "created_at": "2022-09-09T18:14:54.592766Z",
      "updated_at": "2022-09-09T18:14:54.592766Z",
      "user": {
        "id": "2deb69af-43c7-44df-af6e-47092f1eb021",
        "username": "johndoe"
      }
    }
  ]
}
```

---

### **Listar Um Comentário:**

**Endpoint:** `/posts/<id_post>/comments/<id_comment>/`

**Método:** GET

**Headers:** None

**Nível de acesso:** Livre

**Sobre a rota:** Rota para listagem de um comentário.

**O que será retornado em caso de sucesso:**

```json
{
  "id": "de0c99bd-9d6b-4699-a0f5-23c99d61bc63",
  "comment": "this is a cool comment! :)",
  "created_at": "2022-09-09T18:14:54.592766Z",
  "updated_at": "2022-09-09T18:14:54.592766Z",
  "user": {
    "id": "2deb69af-43c7-44df-af6e-47092f1eb021",
    "username": "johndoe"
  }
}
```

---

### **Atualizar Um Comentário:**

**Endpoint:** `/posts/<id_post>/comments/<id_comment>/`

**Método:** PATCH

**Headers:**

- Content-Type application/json
- Authorization Token <token_do_usuário>

**Nível de acesso:** Rota restrita para usuário dono do comentário e administradores.

**Sobre a rota:** Rota para atualizar/editar um comentário.

**O que deve ser enviado:**

```json
{
  "comment": "this is a cooler edited comment! :D"
}
```

**O que será retornado em caso de sucesso:**

```json
{
  "id": "de0c99bd-9d6b-4699-a0f5-23c99d61bc63",
  "comment": "this is a cooler edited comment! :D",
  "created_at": "2022-09-09T18:14:54.592766Z",
  "updated_at": "2022-09-09T17:02:42.178216Z"
}
```

---

### **Deletar Um Comentário:**

**Endpoint:** `/posts/<id_post>/comments/<id_comment>/`

**Método:** DELETE

**Headers:**

- Content-Type application/json
- Authorization Token <token_do_usuário>

**Nível de acesso:** Rota restrita para usuário dono do comentário e administradores.

**Sobre a rota:** Rota para deleção de um comentário.

**O que será retornado em caso de sucesso:**

```
Status 204 - No Content
```

---

## 🔖 Friends:

### **Adicionar Um Amigo:**

**Endpoint:** `/users/friends/<id_friend>/`

**Método:** POST

**Headers:**

- Authorization Token <token_do_usuário>

**Nível de acesso:** Rota restrita para usuários logados

**Sobre a rota:** Rota para adicionar um amigo

**O que deve ser enviado:**

```
No Body
```

**O que será retornado em caso de sucesso:**

```
Status 204 - No Content
```

---

### **Listar Solicitações de Amizades:**

**Endpoint:** `/users/friends/pending/`

**Método:** GET

**Headers:**

- Authorization Token <token_do_usuário>

**Nível de acesso:** Rota restrita para usuários logados

**Sobre a rota:** Rota para listar as solicitações de amizades do que está usuário logado.

**O que será retornado em caso de sucesso:**

```json
{
    "count": 1,
    "next": null,
    "previous": null,
    "results": [
        {
            "id": 6,
            "created": "2022-09-09T19:04:42.759691Z",
            "user": {
		            "id": "f9456d95-b092-481a-aa0b-3c22165db0b7",
		            "username": "janedoe"
                "first_name": "jane",
                "last_name": "doe"
            }
        }
    ]
}
```

---

### **Recusar Um Pedido de Amizade:**

**Endpoint:** `/users/friends/pending/<id_friend>/?accept=0`

**Método:** DELETE

**Headers:**

- Authorization Token <token_do_usuário>

**Nível de acesso:** Rota restrita para usuários logados

**Sobre a rota:** Rota para recusar um pedido de amizade

**O que deve ser enviado:**

```
No Body
```

**O que será retornado em caso de sucesso:**

```
Status 204 - No Content
```

---

### **Aceitar Um Pedido de Amizade:**

**Endpoint:** `/users/friends/pending/<id_friend>/?accept=1`

**Método:** POST

**Headers:**

- Authorization Token <token_do_usuário>

**Nível de acesso:** Rota restrita para usuários logados

**Sobre a rota:** Rota para aceitar um pedido de amizade

**O que deve ser enviado:**

```
No Body
```

**O que será retornado em caso de sucesso:**

```
Status 204 - No Content
```

---

### **Listar Amigos:**

**Endpoint:** `/users/friends/`

**Método:** GET

**Headers:**

- Authorization Token <token_do_usuário>

**Nível de acesso:** Rota restrita para usuários logados

**Sobre a rota:** Rota para listar os amigos do usuário logado.

**O que será retornado em caso de sucesso:**

```json
{
  "count": 1,
  "next": null,
  "previous": null,
  "results": [
    {
      "id": "00321fd9-7f22-4f65-bffe-b4b24457acfb",
      "username": "janedoe",
      "first_name": "jane",
      "last_name": "doe"
    }
  ]
}
```

---

### **Remover Um Amigo:**

**Endpoint:** `/users/friends/<id_friend>/`

**Método:** DELETE

**Headers:**

- Authorization Token <token_do_usuário>

**Nível de acesso:** Rota restrita para usuários logados

**Sobre a rota:** Rota para remover um amigo

**O que será retornado em caso de sucesso:**

```
Status 204 - No Content
```

---

## 🔖 Retornos Gerais de Erros:

### **Usuários Sem Permissões:**

**Sobre:** Erro caso um usuário tente alterar algo que não tenha permissão.

```json
{
  "detail": "You do not have permission to perform this action."
}
```

---

### **Requisições Sem Token:**

**Sobre:** Erro caso um usuário tente acessar uma rota sem estar logado.

```json
{
  "detail": "Authentication credentials were not provided."
}
```

---

### **Campos Incompletos:**

**Sobre:** Erro caso falte algum campo nas requisições.

```json
{
  "password": ["This field is required."],
  "first_name": ["This field is required."]
}
```
