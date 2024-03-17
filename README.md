
# API de Gerenciamento de Livros
## Objetivo
O objetivo deste projeto é criar uma API que fornece funcionalidades para consulta, criação, edição e exclusão de livros. A API será acessível localmente a partir da URL base "localhost" e permitirá interações por meio de diversos endpoints.

### Tecnologias Utilizadas
- **Python:** Utilizamos a linguagem de programação Python para desenvolver a lógica da API.
- **Flask:** Flask é um framework de desenvolvimento web em Python que facilita a criação de APIs e aplicações web.
- **JSON:** Os dados são transmitidos entre o cliente e o servidor no formato JSON (JavaScript Object Notation), que é amplamente utilizado para comunicação entre sistemas.
### Endpoints
**Criar Livros (POST):** /livros

Este endpoint permite a criação de um novo livro no sistema. Os dados do livro devem ser enviados no corpo da requisição no formato JSON.

- **Acesso aos Livros (GET):** /livros

Este endpoint retorna todos os livros disponíveis no sistema.

- **Acesso aos Livros por ID (GET):** /livros/id

Este endpoint retorna as informações de um livro específico com base no ID fornecido na URL.

- **Alteração de Livros por ID (PUT):** /livros/id

Este endpoint permite a edição das informações de um livro existente com base no ID fornecido na URL. Os novos dados do livro devem ser enviados no corpo da requisição no formato JSON.

- **Deletar Livros por ID (DELETE):** /livros/id

Este endpoint exclui um livro específico com base no ID fornecido na URL.
### Recursos Disponíveis
**Livros:** Os recursos principais manipulados por esta API são os livros. Cada livro possui um ID único, título e autor.
