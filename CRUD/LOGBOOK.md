# LOGBOOK AFP — Algoritmos e Programação
**Universidade de Brasília (UnB) — Semestre 2026.2**  
**Docente:** Prof. Rondineli Seba Salomão  
**Projeto:** Sistema de Hamburgueria (Python)  
**Estudante:** Ricardo  

---

### CAMPO 01 · ENTRADA (Diagnóstico Inicial — sem consulta)

#### 1. O que eu achava que sabia
* **Entrada e Saída Básica:** Sabia usar a função `print()` para exibir textos no terminal e `input()` para capturar o que o usuário digita. Achava que o Python já identificava se o dado digitado era um número ou um texto.
* **Fluxo de Decisão Linear:** Acreditava que para criar o menu de opções da hamburgueria bastava encadear vários comandos `if` e `else` sequenciais, comparando diretamente a entrada digitada.
* **Navegação Contínua:** Imaginava que para fazer o menu voltar ao início após um pedido bastaria chamar o bloco novamente ou colocar um laço simples, sem me preocupar com o encerramento do processo.
* **Organização das Informações:** Achava que para representar o cardápio e a personalização bastava declarar variáveis avulsas para cada escolha do cliente (`opcao`, `opcao_pao`, `opcao_carne`).

#### 2. O que eu não sabia (Dúvidas e lacunas reais)
* **Tipagem e Coerção:** Não entendia por que comparações como `opcao == 1` falhavam quando eu não convertia a resposta do `input()`, desconhecendo que ela sempre retorna texto (`str`).
* **Controle de Laços e Ponto de Escape:** Não dominava o padrão de menu contínuo com `while True` e a instrução sentinela `break`. Não sabia como evitar que o programa entrasse em loop infinito ou fechasse sozinho logo após a primeira escolha.
* **Submenus e Laços Aninhados:** Não sabia como estruturar a montagem sequencial de um hambúrguer (pão, carne e múltiplos acompanhamentos) sem que uma quebra de laço interna cancelasse o programa inteiro.
* **Tratamento de Entradas Inválidas:** Não sabia como evitar que o sistema quebrasse com erro de execução (`ValueError`) caso o usuário digitasse letras ou pressionasse *Enter* vazio onde se esperava número.

---

### CAMPO 02 · APROFUNDAMENTO (Pesquisa, Fundamentação e Mudança de Hipóteses)

#### 1. Pesquisas e Fontes Consultadas
* **Livro de Referência:** *Pense em Python: Pense como um Cientista da Computação* (Allen B. Downey, 2ª edição, Editora Novatec).
  * *Capítulo 1:* A jornada do programa — tipos de erros (sintaxe, tempo de execução e semânticos).
  * *Capítulo 2:* Variáveis, expressões e instruções — tipos de dados primitivos e conversão explícita de tipos (`int()`, `float()`, `str()`).
  * *Capítulo 5:* Condicionais e recursividade — operadores relacionais (`==`, `!=`), desvios condicionais e cadeias `if-elif-else`.
  * *Capítulo 7:* Iteração — laço `while`, reatribuição e interrupção com `break`.
* **Documentação Oficial do Python (python.org):** Funções embutidas (`input`, `print`, `int`) e controle de fluxo.

#### 2. Como minha hipótese mudou em relação ao Campo 01
* **Coerção Explícita de Tipos:** A consulta ao Cap. 2 confirmou que `input()` retorna estritamente uma string (`str`). A comparação `"1" == 1` resulta em `False`. Por isso, para comparar numericamente no menu da hamburgueria, tornou-se obrigatório converter o valor com `opcao = int(input(...))`.
* **Padrão Canônico de Menu CLI:** Abandonei a ideia de chamadas repetidas ou fluxos lineares. Compreendi pelo Cap. 7 que aplicações de terminal dependem do laço infinito `while True:` mantido ativo até que a condição sentinela de saída dispare o comando `break` (no caso, `if opcao == 5: break`).
* **Laços Aninhados (*Nested Loops*) e Isolamento de Etapas:** Compreendi que a instrução `break` interrompe unicamente o laço mais interno (*inner loop*). Isso permitiu isolar cada etapa da montagem personalizada (pão -> carne -> acompanhamentos) em seu próprio `while True` com validação local, avançando somente após uma escolha válida.

---

### Campo 03 — Execução e desvios

#### 3a. Pelo menos 2 achados que mudaram sua compreensão do problema, cada um com o objeto de conhecimento associado:

* **Achado 1:**
  * **Objeto de conhecimento associado:** *Laços de repetição (`while`) e comando de interrupção (`break`).*
  * **Meu achado:** Quando eu fui fazer a parte de montar o hambúrguer (onde o cliente escolhe o pão, a carne e os acompanhamentos), eu achava que o comando `break` encerrava o programa inteiro e voltava para o começo de tudo. Quando fui testar, descobri que quando temos um looping dentro de outro looping, o `break` encerra apenas o looping de dentro onde ele foi colocado. Isso mudou minha compreensão, pois percebi que para fazer o cliente passar de uma escolha para a outra (do pão para a carne e depois para os acompanhamentos), eu precisava criar um looping `while True` separado para cada etapa, usando o `break` para avançar sem derrubar o menu principal.

* **Achado 2:**
  * **Objeto de conhecimento associado:** *Variáveis simples e fluxo de atribuição na memória.*
  * **Meu achado:** Ao fazer a parte de escolher mais de um acompanhamento, eu tentei usar a mesma variável para guardar as respostas. Descobri que toda vez que o comando `input()` era executado de novo, ele apagava a resposta anterior que estava guardada na variável. Como eu só posso usar variáveis simples, percebi que para não perder o que o cliente escolheu, eu precisava criar variáveis separadas para cada resposta (`opcao_acompanhamento1`, `opcao_acompanhamento2`, `opcao_acompanhamento3`) e usar condicionais com `if` para controlar quantas perguntas seriam feitas.

---

#### 3b. Pelo menos 1 desvio em relação ao Campo 02 (o que você planejou e não aconteceu) e a causa técnica:

* **O que eu planejei no Campo 02:**
  Eu planejava fazer uma repetição única e curta para perguntar os acompanhamentos, repetindo a mesma pergunta na tela quantas vezes o cliente quisesse.
* **O que realmente aconteceu (meu desvio):**
  No meu arquivo `Hamburgueria.py`, acabei criando três blocos separados usando `if opcao_acompanhamento == 1:`, `elif opcao_acompanhamento == 2:` e `elif opcao_acompanhamento == 3:`, repetindo a estrutura dos loopings para cada acompanhamento.
* **Causa técnica real do desvio:**
  O desvio aconteceu porque tive dificuldade em fazer um único looping repetir a pergunta mudando o texto ("primeiro", "segundo", "terceiro") sem que a resposta nova apagasse o valor da anterior na mesma variável. Para ter certeza de que cada resposta ficaria salva em uma variável separada e que o programa não se perderia, preferi separar o código em três blocos de `if` com variáveis próprias para cada acompanhamento.

---

#### 3c. Pelo menos 1 decisão de ajuste, com justificativa e fonte, e o objeto de conhecimento mobilizado:

* **Objeto de conhecimento mobilizado:**
  *Estruturas condicionais (`if-elif-else`) e laços de repetição (`while`).*
* **Minha decisão de ajuste no código:**
  Nos menus de escolher o pão, a carne e os acompanhamentos, eu adicionei a linha `else: print('Opção inválida. Tente novamente.')` no final de cada condicional, sem colocar o comando `break` nesse ramo.
* **Justificativa técnica:**
  Sem o `else`, se o usuário digitasse um número que não existia (por exemplo, 0 ou 4), o programa não entrava em nenhum `if`, passava direto e deixava a variável sem a resposta certa. Com o `else` dentro do `while True`, se o usuário digitar uma opção inválida, o programa avisa o erro e o looping se repete, prendendo o usuário na mesma pergunta até ele digitar uma opção válida (1, 2 ou 3) e acionar o `break`.
* **Fonte técnica:**
  Livro *Pense em Python* (Allen B. Downey), Capítulo 5 ("Condicionais e recursividade", seção 5.6 sobre condicionais encadeadas e comparação de valores com `==`).

---

### Campo 04 — Interação com IA

#### 4b. Transcreva a pergunta na íntegra (copie e cole):
> *"Como faço para não deixar o usuário passar para a próxima opção da hamburgueria se ele digitar um número errado, usando apenas while e if/else?"*

---

#### 4c. Resuma a resposta em um parágrafo com as suas palavras:
A IA me explicou que eu deveria colocar cada pergunta dentro de um laço de repetição `while True:`, ler a resposta com `int(input())` e usar `if` e `elif` para checar os números válidos. Quando o número digitado for correto, o código mostra a escolha e usa o `break` para sair daquele laço; se o número for errado, o fluxo cai no `else`, imprime uma mensagem de erro e, como não tem `break` no `else`, o looping repete a mesma pergunta automaticamente. A IA também me sugeriu criar funções com `def` e usar comandos mais avançados para diminuir as linhas de código.

---

#### 4d. O que você aceitou, ligando ao objeto de conhecimento:
* **Objeto de conhecimento:** *Laços de repetição (`while True`), comando `break` e estruturas condicionais (`if-elif-else`).*
* **O que aceitei e por quê:**
  Aceitei o padrão de colocar a pergunta dentro de um `while True:` com `if/elif` dando `break` somente quando o número digitado for válido, e deixando o `else` sem `break` apenas com o aviso de erro. Isso resolveu perfeitamente o problema do meu programa usando apenas os conceitos básicos de variáveis, repetições e condicionais que vimos em aula.

---

#### 4e. O que você questionou ou descartou, com argumento técnico ou fonte:
* **O que descartei/questionei:**
  Descartei a sugestão da IA de criar funções com `def` e de usar comandos mais avançados para juntar as opções.
* **Argumento técnico com base em testes e no aprendizado:**
  Descartei o uso de funções e comandos avançados porque na disciplina estamos focados em dominar primeiro a lógica pura de variáveis, condicionais (`if/elif/else`) e repetições (`while`). Testei o código usando apenas variáveis simples e laços `while` e comprovei que ele funciona perfeitamente sem precisar de nada complexo, mantendo a execução linear e fácil de explicar na defesa técnica sem misturar conteúdos que ainda não domino.

---

## 📌 GRUPO 3 (Prazo: Quinta 26/11 · 23h59)

### Campo 05 — Revisão por pares (2 colegas)

#### Revisão 1 — Projeto do colega: Kenzo
* **Pontos positivos observados:** No sistema do Kenzo, gostei bastante de como ele organizou os textos do menu com `print()` e da forma como manteve o programa ativo em ciclo contínuo usando `while True:` com `break` apenas na opção de saída.
* **Falha técnica identificada:** Ao testar o fluxo dele, vi que em um dos menus ele colocou vários `if` soltos em sequência sem usar `elif`. Por causa disso, o `else` lá de baixo acabava disparando `"Opção inválida"` mesmo quando eu digitava uma das primeiras opções certas. Também faltou um `else` dentro de um submenu para impedir que o usuário avançasse ao digitar um número inexistente.
* **Minha recomendação:** Indiquei transformar os `if` soltos em uma estrutura `if-elif-else` encadeada e adicionar o `else` sem `break` dentro do `while True`, garantindo que o looping repita a pergunta até receber um número válido (*Pense em Python*, Cap. 5 e Cap. 7).

#### Revisão 2 — Projeto do colega: Gustavo
* **Análise geral do código:** O Gustavo já estruturou corretamente a árvore de decisões com `if-elif-else` e deixou bem intuitivo o passo a passo das escolhas no terminal.
* **Bugs encontrados nos testes:** Identifiquei dois problemas diferentes do código do Kenzo. Primeiro, em uma das entradas ele usou `input()` direto sem `int()` e comparou com número (`== 1`), o que falhava sempre porque `input()` retorna texto (`str`). Segundo, ele reaproveitou a mesma variável para ler duas respostas seguidas, fazendo o segundo `input()` apagar o valor da primeira escolha antes de exibir o resumo.
* **Ajuste proposto:** Orientei aplicar `int(input(...))` para converter a entrada para número inteiro antes da comparação (*Pense em Python*, Cap. 2 — Variáveis e conversão de tipos) e declarar uma variável própria para cada resposta que precisa ser guardada.

---

### Campo 06 — Próximos passos

#### 6a. O que eu defendo na minha solução (`Hamburgueria.py`):
Defendo que meu programa entrega um fluxo interativo completo de pedidos e montagem personalizada de hambúrguer no terminal utilizando exclusivamente os fundamentos base da disciplina: variáveis simples, conversão de tipos com `int(input())`, condicionais encadeadas (`if-elif-else`) e laços de repetição aninhados (`while True` com `break`). Cada etapa da montagem (pão, carne e acompanhamentos) é isolada em seu próprio laço de validação, garantindo que o cliente não avance com uma opção numérica inválida.

#### 6b. O que falta melhorar (limites que reconheço):
Reconheço três limites claros na versão atual do `Hamburgueria.py`:
1. **Entradas não numéricas:** Se o usuário digitar uma letra ou pressionar *Enter* vazio no `int(input())`, o programa encerra com `ValueError`, pois ainda não há tratamento de erro para caracteres não numéricos.
2. **Repetição de código nos acompanhamentos:** Na opção de 2 ou 3 acompanhamentos, repeti os blocos de `while True` e `if/elif` para cada escolha (`opcao_acompanhamento1` até `opcao_acompanhamento6`), deixando o código mais longo.
3. **Limitação de variáveis simples:** Como o código usa apenas variáveis simples em memória, as escolhas não ficam armazenadas em um histórico persistente nem permitem editar ou excluir pedidos depois que o programa fecha.

#### 6c. Qual pergunta difícil a banca fará e como respondo:
* **Pergunta provável da banca:** *"Por que você repetiu o mesmo bloco de laço várias vezes para os acompanhamentos em vez de usar um único looping, e o que acontece se o usuário digitar uma letra no menu?"*
* **Minha resposta:** Eu repeti os blocos porque, usando apenas variáveis simples, se eu reaproveitasse a mesma variável dentro de um único looping, cada nova resposta com `input()` sobrescreveria a escolha anterior na memória. Separar em variáveis diferentes (`opcao_acompanhamento2`, `opcao_acompanhamento3`, etc.) garantiu que nenhuma escolha fosse perdida. Quanto a digitar uma letra, reconheço o limite: o `int(input())` gera um `ValueError` porque letras não podem ser convertidas para inteiro na base 10; na versão atual eu trato apenas números fora do intervalo válido usando a cláusula `else` dentro do `while True`.

---

### Campo 07 — Evolução conceitual

#### 7a. Retomando o Campo 01 (de onde saí até onde cheguei):
No Campo 01, eu achava que `input()` identificava números sozinho, que bastava empilhar vários `if` e `else` e que o menu voltava para o início automaticamente. Hoje, ao concluir o ciclo, sei exatamente que `input()` sempre devolve texto (`str`), que condicionais independentes causam erro lógico no `else` final (exigindo `if-elif-else`), e que um menu contínuo depende de `while True:` com `break` apenas na condição de saída.

#### 7b. Domínio dos objetos de conhecimento mobilizados:
Consolidei o domínio prático de quatro pilares da programação estruturada (referenciados em *Pense em Python*, Capítulos 1, 2, 5 e 7):
1. **Variáveis, tipos e coerção (`int()`, `str`, `input()`, `print()`):** Entendimento do tipo retornado pela entrada padrão e da necessidade de conversão explícita antes de comparações numéricas.
2. **Estruturas condicionais (`if-elif-else`):** Uso de ramificações mutuamente exclusivas e da cláusula residual `else` como barreira de validação.
3. **Laços de repetição (`while True`) e escopo do `break`:** Compreensão de que o `break` encerra apenas o laço mais interno (*inner loop*), permitindo construir submenus em sequência sem quebrar o laço principal.
4. **Atribuição e preservação de estado em variáveis simples:** Controle de variáveis distintas para evitar que novas leituras apaguem escolhas anteriores.

#### 7c. Principal erro corrigido durante o processo:
O erro mais marcante que identifiquei e corrigi foi o uso de condicionais não encadeadas e o posicionamento errado do `break`: no início, a mensagem de `"Opção inválida"` aparecia mesmo em escolhas válidas, ou o `break` fechava o programa inteiro em vez de apenas sair de um submenu. Corrigi estruturando `if-elif-else` corretamente e confinando cada etapa em seu próprio `while True`.

#### 7d. Transferência para um contexto novo:
Se eu precisasse desenvolver hoje outro sistema de terminal totalmente diferente — como um **caixa eletrônico** ou um **sistema de votação** — eu aplicaria a mesma lógica estruturada: um laço `while True` principal para manter o menu aberto até a opção de saída (`break`), conversão `int(input())` nas opções, `if-elif-else` para separar cada operação com `else` de erro para entradas inválidas, e laços internos isolados com variáveis próprias para etapas obrigatórias (como confirmar o número do candidato ou escolher o tipo de operação) antes de retornar ao menu inicial.
