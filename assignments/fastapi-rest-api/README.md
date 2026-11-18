# 📘 Assignment: Building REST APIs with FastAPI

## 🎯 Objetivo

Construa uma API REST para gerenciar produtos usando FastAPI e Pydantic. Você vai praticar métodos HTTP, rotas, validação de dados e códigos de status em uma aplicação Python.

## 📝 Tarefas

### 🛠️ Criar endpoints para consultar produtos

#### Descrição

Use o código inicial para criar os endpoints de leitura da coleção de produtos. Instale as dependências com `python -m pip install fastapi uvicorn` e inicie a aplicação com `uvicorn starter-code:app --reload`.

#### Requisitos

O programa concluído deve:

- Retornar todos os produtos em `GET /products`.
- Retornar um produto por identificador em `GET /products/{product_id}`.
- Responder com status `404` quando o identificador solicitado não existir.

### 🛠️ Adicionar produtos à API

#### Descrição

Implemente a criação de produtos e valide os dados enviados pelo cliente usando o modelo Pydantic fornecido.

#### Requisitos

O programa concluído deve:

- Criar um produto com `POST /products`, recebendo nome, descrição e preço.
- Gerar um identificador único para cada produto criado.
- Retornar o produto criado com status `201`.
- Rejeitar preços que não sejam maiores que zero.

### 🛠️ Completar as operações CRUD

#### Descrição

Adicione as operações para atualizar e remover produtos. Use os códigos de status HTTP apropriados e trate identificadores inexistentes de forma consistente.

#### Requisitos

O programa concluído deve:

- Atualizar os dados de um produto com `PUT /products/{product_id}`.
- Remover um produto com `DELETE /products/{product_id}`.
- Retornar status `404` para atualização ou remoção de um produto inexistente.
- Responder à remoção bem-sucedida com status `204` e sem conteúdo no corpo.