## 001 - Em que década aconteceu a "Crise do Software" no mercado?   
## a) 1950     b) 1960     c) 1980     d) 2000
# R: B

## 002 - Qual das caraceterísticas a seguir identifica as primeiras linguagem lineares?
## a) Maior modulariadade   b) Desvios forçados com GOTO    c) Estruturas de controle   d) Instruções de baixo nível
# R: B

## 003 - Quem foi o criador da Smalltalk, umas das primeiras linguagens de Orientação a Objetos (OO)?
## a) Edsger Dijkstra   b) Guido Van Rossum     c) Alan Kay     d)Kristen Nygaard
# R: C

## 004 - A linguagem Simula foi um superconjunto de que outra linguagem?
## a)ALGOL     b)C    c)Smaltalk    d)Python
# R: A

## 005 - Na sigla OOAD, as ultimas duas letras significam...
## a)Algol/Dashboard    b)Algorithms/Digital    c)Analytics/Default     d)Analysis/Design
# R: D


## Quais as vantagens da POO:
# Confiável - Isolamento entre as partes gera algo mais seguro. Ao alterar uma das partes nenhuma outra é afetada.
# Oportuno - Ao dividir tudo em partes, cada uma delas pode ser desenvolvida em paralelo.
# Manutenível - Atualizar é mais fácil. Uma pequena alteração vai beneficiar todas as partes relacionadas.
# Extensivel - Um sistema não deve ser estático. Tudo deve mudar e crescer para permanecer útil.
# Reutilizavel - Objetos que foram criados para um sistema podem ser aproveitados em outros sistemas.
# Natural - Mais fácil de entender. Maior atenção às funcionalidades do que aos detalhes de implementação.

## 006 - Crie um sistema para Escola, ao criar outro sistema para Academia, parte do trabalho já está feita, pois tenho Alunos nos dois.
## a)Confiável      b)Natural       c)Manutenível       d)Reutilizável
# R:D

## 007 - Se precisar adicionar uma nova funcionalidade ao sistema, consigo fazer isso com grande facilidade.
## a)Natural      b)Extensível       c)Reutilizável       d)Oportuna
# R: B

## 008 - Posso desenvolver várias funções que dependam uma da outra ao mesmo tempo se o planejamento for seguido.
## a)Oportuno     b)Reutilizável       c)Confiável       d)Manutenível
# R: A

## 009 - O código fica muito simples de ler e de compreender, já que não preciso saber os detalhes de funcionamento ao programar.
## a)Natural     b)Extensivel       c)Manutenivel       d)Oportuno
# R: A

## 010 - Posso alterar como uma funcionalidade trabalha e tudo continua como antes.
## a)Oportuno    b)Reutilizavel       c)Confiavel       d)Natural
# R: C

## Classe são compostas atributos (caracteristicas) e métodos (ações) que instancia(cria) um objeto.
## Objeto são coisas materiais ou abstratas que é feita a partir de um modelo(classe) e pode ser descrita por meio de suas características(atributos), comportamento(métodos) e estado atual.
## Objetos abstratos são criados apartir classe abstrata(um molde incompleto) que obriga as classes filhas a preencherem todas as lacunas antes de gerarem um objeto concreto.

## 011 - Qual dos objetos abaixo seria o único abstrato da lista?
## a) Sensor    b) Robô     c)Notificação       d)Livro
# R: C

## 012 - Na teoria de Orientação a Objeto, o termo usado para o ato de fazer um objeto existir, a partir de um modelo se chama:
## a) Instanciar   b) Classificar     c)Objetificar       d)Forjar
# R: A

## 013 - Todo objeto tem uma lista de atividades que podem ser feitas com ele ou que ele pode desempenhar sozinho que são:
## a) Atributos   b) Métodos     c) Classes       d)Instancias
# R: B

## 014 - Ao conjunto de todos os valores de atributos de um objeto em um determinado momento, damos o nome de:
## a) Identidade  b) Instancia     c) Método       d) Estado
# R: D

## 015 - Descreva a estrutura de dois objetos: Um concreto e outro abstrato. Inclua também seus principais atributos, métodos e crie um exemplo de estado para cada um deles. Atributos, metodos e Estado.
# R: ObjetoConcreto carro(): {Atributos: [cor,modelo, ano,velocidadeAtual,ligado], metodos:[ligar,desligar,acelerar,frear,trocarMarcha,estacionar],Estado[O carro está rodando, na 2ª marcha, a 30km/h e com as portas trancadas. ]}
# ObjetoAbstrato simulaçãoEmprestimo(): {atributos:[valor,data inicio, data final, parcela, taxa], metodos:[Simular, recomeçar,calcularParcela,exibirResultado], estado:[Simulação de xReais em xParcelas, com taxas de x% ao mês e status Aprovado.]}