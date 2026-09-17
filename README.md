# CRUD de Sistema Imobiliário (Flask)

**Projeto real e comercial**  
Desenvolvido e colocado em produção real para gerenciar a comercialização e o catálogo de imóveis por meio de uma aplicação web modular em Flask, interface PWA e banco de dados SQLite. Este projeto não é apenas um exercício acadêmico teórico: ele foi totalmente implementado, validado e executado em ambiente real de produção com domínio e hospedagem próprios para clientes reais.

## Escopo do Projeto
O projeto abrange o desenvolvimento de uma solução web completa para o setor imobiliário, focando na agilidade de entrega, facilidade de uso em dispositivos móveis através de PWA, otimização de recursos de hardware e imagens, além da infraestrutura de hospedagem própria, domínio personalizado e painel administrativo dedicado.

## Objetivos
* Aplicar conceitos práticos de desenvolvimento web na criação de um produto comercial funcional.
* Implementar as operações CRUD: criar, consultar, atualizar e excluir.
* Organizar o código em camadas de rotas, modelos ORM e persistência.
* Trabalhar com validação de dados, regras condicionais e tratamento de arquivos/imagens.
* Persistir informações localmente em banco de dados SQLite com SQLAlchemy.
* Integrar recursos visuais utilizando a biblioteca Pillow para tratamento e otimização de imagens.
* Colocar a aplicação em um ambiente de produção real com domínio próprio e infraestrutura de hospedagem nacional personalizada.

## Funcionalidades
* **Painel administrativo completo**: área restrita para o gerenciamento, controle e visualização de todos os registros e dados da imobiliária.
* Cadastrar imóveis e suas informações comerciais, permitindo escolher entre as modalidades de **venda ou aluguel**.
* Permitir o **cadastro manual de imóveis** caso o corretor prefira não registrá-los diretamente no sistema.
* Suportar o **cadastro por link**, facilitando a importação rápida de informações.
* Exibição dos imóveis em um **formato visual otimizado** (cards responsivos limpos e organizados) voltado para conversão e consumo rápido no celular.
* Geração de **links exclusivos para os clientes** compartilharem ou acessarem os imóveis de forma direta.
* Listar imóveis de forma responsiva para visualização mobile (PWA).
* Atualizar informações dos imóveis cadastrados.
* Excluir imóveis da lista.

## Tipos de Dados
* **Título**: string
* **Descrição**: string
* **Preço**: int
* **Modalidade**: string (venda ou aluguel)
* **Imagem**: string (nome do arquivo otimizado)

## Regras de Negócio
* **RN01**: O preço do imóvel deve ser um número inteiro (`int`) e maior que 0. Caso seja 0 ou um valor negativo, o sistema deve informar que o valor deve ser maior que 0.
* **RN02**: O título do imóvel não pode ficar vazio. Caso fique vazio, o sistema deve informar que não é possível cadastrar sem colocar o título.
* **RN03**: O upload de imagens deve obrigatoriamente passar por redimensionamento e otimização utilizando a biblioteca Pillow.
* **RN04**: O sistema deve organizar a exibição dos registros e garantir estabilidade de carregamento utilizando uma infraestrutura de produção otimizada.

## Requisitos Funcionais
* **RF01**: O sistema deve permitir cadastrar imóveis e suas informações (incluindo escolha de venda ou aluguel, opção de cadastro manual caso o corretor não queira usar o sistema, e cadastro via link).
* **RF02**: O sistema deve disponibilizar um painel administrativo para gestão e controle.
* **RF03**: O sistema deve permitir listar imóveis em formato visual otimizado (cards) e gerar links diretos para os clientes.
* **RF04**: O sistema deve permitir atualizar informações dos imóveis.
* **RF05**: O sistema deve permitir excluir imóveis da lista.

## Requisitos Não Funcionais
* **RNF01**: O sistema deve possuir uma interface simples, leve e fácil de utilizar no celular (PWA).
* **RNF02**: O sistema deve funcionar integrado à infraestrutura de hospedagem contratada.
* **RNF03**: O sistema deve ser desenvolvido utilizando a linguagem Python e o framework Flask.

## Ferramentas e Tecnologias
* **Python**: linguagem principal.
* **Flask**: framework web para criação das rotas e requisições HTTP.
* **SQLAlchemy**: camada ORM utilizada para comunicação com o banco de dados.
* **SQLite**: banco de dados local baseado em arquivo.
* **Pillow (PIL)**: biblioteca para manipulação, redimensionamento e otimização de imagens.
* **HTML, CSS e JavaScript**: interface web responsiva e Progressive Web App (PWA).
* **GitHub**: versionamento de código e controle de alterações.
* **Hospedagem Nacional personalizada**: ambiente de produção real.

## Estrutura do Projeto
* **`app.py`** — aplicação Flask principal, modelos e endpoints de rotas.
* **`models.py`** — modelos ORM e operações de banco de dados.
* **`templates/`** — interfaces web, painel administrativo e arquivos HTML da aplicação.
* **`static/uploads/`** — diretório de armazenamento e cache de imagens otimizadas.
* **`requirements.txt`** — dependências Python do projeto.
* **`imoveis.db`** — banco SQLite local criado durante a execução.
