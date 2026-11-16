# LOGBOOK AFP — GRUPO 1 (UnB 2026.2)
**Docente:** Prof. Rondineli Seba Salomão  
**Projeto:** Sistema de Hamburgueria (CRUD CLI em Python)  
**Estudante:** Ricardo  

---

## CAMPO 01 · ENTRADA

### 1. O que eu achava que sabia
* **Entrada e Saída Básica:** Sabia usar a função `print()` para exibir textos no terminal e `input()` para capturar o que o usuário digita. Achava que o Python já identificava se o dado digitado era um número ou um texto.
* **Fluxo de Decisão Linear:** Acreditava que para criar o menu de opções da hamburgueria bastava encadear vários comandos `if` e `else` sequenciais, comparando diretamente a entrada digitada.
* **Navegação Contínua:** Imaginava que para fazer o menu voltar ao início após um pedido bastaria chamar o bloco novamente ou colocar um laço simples, sem me preocupar com o encerramento do processo.
* **Organização das Informações:** Achava que para representar o cardápio e a personalização bastava declarar variáveis avulsas para cada escolha do cliente (`opcao`, `opcao_pao`, `opcao_carne`).

### 2. O que eu não sabia (Dúvidas e lacunas reais)
* **Tipagem e Coerção:** Não entendia por que comparações como `opcao == 1` falhavam quando eu não convertia a resposta do `input()`, desconhecendo que ela sempre retorna texto (`str`).
* **Controle de Laços e Ponto de Escape:** Não dominava o padrão de menu contínuo com `while True` e a instrução sentinela `break`. Não sabia como evitar que o programa entrasse em loop infinito ou fechasse sozinho logo após a primeira escolha.
* **Submenus e Laços Aninhados:** Não sabia como estruturar a montagem sequencial de um hambúrguer (pão, carne e múltiplos acompanhamentos) sem que uma quebra de laço interna cancelasse o programa inteiro.
* **Tratamento de Entradas Inválidas:** Não sabia como evitar que o sistema quebrasse com erro de execução (`ValueError`) caso o usuário digitasse letras ou pressionasse *Enter* vazio onde se esperava número.

---

## CAMPO 02 · APROFUNDAMENTO

### 1. Pesquisas e Fontes Consultadas
* **Livro de Referência:** *Pense em Python: Pense como um Cientista da Computação* (Allen B. Downey, 2ª edição, Editora Novatec).
  * *Capítulo 1:* A jornada do programa — distinção entre erros de sintaxe, tempo de execução e semânticos.
  * *Capítulo 2:* Variáveis, expressões e instruções — tipos de dados primitivos e conversão explícita de tipos (`int()`, `float()`, `str()`).
  * *Capítulo 5:* Condicionais e recursividade — operadores relacionais (`==`, `!=`), desvios condicionais e cadeias `if-elif-else`.
  * *Capítulo 7:* Iteração — laço `while`, reatribuição e interrupção com `break`.
  * *Capítulos 10 e 11:* Listas e Dicionários — estruturas dinâmicas em memória, coleções mutáveis e mapeamento chave-valor.
* **Documentação Oficial do Python (python.org):** Funções embutidas (`input`, `print`, `int`) e controle de fluxo.

### 2. Como minha hipótese mudou em relação ao Campo 01
* **Coerção Explícita de Tipos:** A consulta ao Cap. 2 confirmou que `input()` retorna estritamente uma string (`str`). A comparação `"1" == 1` resulta em `False`. Por isso, para comparar numericamente no menu da hamburgueria, tornou-se obrigatório converter o valor com `opcao = int(input(...))`.
* **Padrão Canônico de Menu CLI:** Abandonei a ideia de chamadas repetidas ou fluxos lineares. Compreendi pelo Cap. 7 que aplicações de terminal dependem do laço infinito `while True:` mantido ativo até que a condição sentinela de saída dispare o comando `break` (no caso, `if opcao == 5: break`).
* **Laços Aninhados (*Nested Loops*) e Isolamento de Etapas:** Compreendi que a instrução `break` interrompe unicamente o laço mais interno (*inner loop*). Isso permitiu isolar cada etapa da montagem personalizada (pão -> carne -> acompanhamentos) em seu próprio `while True` com validação local, avançando somente após uma escolha válida.
