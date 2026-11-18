# 📘 Assignment: Testing APIs with pytest

## 🎯 Objetivo

Escreva testes automatizados para uma API de produtos feita com FastAPI. Você vai usar pytest e `TestClient` para verificar respostas, validação de dados e tratamento de erros sem iniciar um servidor web.

## 📝 Tarefas

### 🛠️ Verificar endpoints de consulta

#### Descrição

Instale as dependências com `python -m pip install fastapi pytest httpx` e execute os exemplos incluídos com `pytest -q`. Em `test_api.py`, adicione verificações para a lista de produtos e para a consulta de um produto existente.

#### Requisitos

O conjunto de testes deve:

- Confirmar que `GET /products` retorna status `200` e uma lista com os produtos iniciais.
- Confirmar que `GET /products/1` retorna status `200` e os dados do produto com identificador `1`.
- Verificar pelo menos um campo do corpo JSON, além do código de status.

### 🛠️ Testar criação e validação

#### Descrição

Adicione testes para criar produtos válidos e enviar dados inválidos. Use os dados da resposta para conferir o produto criado e o comportamento de validação da API.

#### Requisitos

O conjunto de testes deve:

- Confirmar que `POST /products` aceita um produto válido e retorna status `201`.
- Verificar que o produto criado aparece na resposta com um identificador e os dados enviados.
- Confirmar que um preço igual ou inferior a zero é rejeitado com status `422`.

### 🛠️ Cobrir atualização, remoção e erros

#### Descrição

Complete a suíte verificando as operações restantes e os casos em que o produto solicitado não existe. Execute os testes repetidamente para garantir que cada caso começa com o catálogo inicial.

#### Requisitos

O conjunto de testes deve:

- Confirmar que `PUT /products/{product_id}` atualiza um produto existente e retorna status `200`.
- Confirmar que `DELETE /products/{product_id}` remove um produto e retorna status `204`.
- Confirmar que consultas, atualizações e remoções de identificadores inexistentes retornam status `404`.
- Passar em execuções repetidas de `pytest -q` sem depender da ordem dos testes.