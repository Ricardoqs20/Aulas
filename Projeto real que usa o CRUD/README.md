# CRUD de Sistema de Hamburgueria (Python)

**Projeto prático de gerenciamento via terminal (CLI)**

Este projeto foi desenvolvido para gerenciar o cardápio e o fluxo de uma hamburgueria por meio de uma aplicação interativa de terminal. O código aplica a lógica de programação direta utilizando estruturas em memória (dicionários) e laços de repetição, servindo como um modelo funcional para o controle de itens (CRUD).

---

## Funcionalidades (CRUD)

- **Menu Interativo**: Área de navegação contínua em loop.
- **Criar (Create)**: Cadastrar novos hambúrgueres informando o nome e o preço (gerando um ID automático).
- **Ler (Read)**: Listar os itens atuais do cardápio de forma limpa e organizada no console.
- **Atualizar (Update)**: Alterar o nome ou o valor de um hambúrguer já cadastrado buscando pelo seu ID.
- **Excluir (Delete)**: Remover do sistema opções que não são mais vendidas.

---

## Tecnologias Utilizadas

- **Python 3**: Linguagem principal e motor de execução.
- **Console / Terminal**: Ambiente de interação e I/O.
- **Dicionários (`dict`)**: Estrutura de dados utilizada para o armazenamento e persistência temporária do cardápio em tempo real.

---

## Regras de Negócio

1. O preço do hambúrguer deve ser obrigatoriamente um valor numérico positivo.
2. O nome do hambúrguer não pode ficar vazio durante o cadastro inicial.
3. Durante a atualização, as alterações são opcionais (se o usuário apertar *Enter* sem digitar nada, o sistema mantém o valor antigo).
4. O sistema possui validação para evitar que o usuário tente deletar ou atualizar um ID que não existe no cardápio.