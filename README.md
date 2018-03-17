# Repository for A.I. classes

Here will be the activities and tests of Artificial Inteligence classes.

## Prova Prática I

Andamento da prova prática que constitui em 4 questões

### Primeira Questão: Missionários e Canibais

Pronta!

  Abordagem será um array de 3 posições no qual [Missionários,Canibais,Barco]
  As funções para testar possibilidades serão 3 ADD's e 3 SUB's nos quais Adicionam/Subtraem da quantidade de membros
  O estado gerado será avaliado da seguite forma  (Missionários < Canibais) -> Negado
  Caso passe da função de avaliação checaremos com auxílio de uma função repetições se o estado já foi gerado
  Adicionamos o novo estado na lista de borda

  Estado inicial: 331
  Estado final: [0,0,0]

### Segunda Questão: Metrô de Paris

Pronta!

A abordagem do problema será dar para cada ponto o trajeto mais rápido para todos os outros.

Função de avaliação será: A distância do avaliado para o destino e caso não façam parte da mesma linha, soma-se 4.
Teremos que ter 4 listas para demonstar as estações em cada linha.
Primeiro: Função irá procurar na mesma linha a estação com menor distância aplicando a função de avaliação.
Segundo: Procura saber se a estação atual também faz parte de outras linhas, caso positivo repete o primeiro passo.
Segundo: Ir adicionando em uma fila de prioridade (regida pela func. avaliação) as estações encontradas no passo 1 e 2.
Terceiro: Retirar o primeiro da fila (menor peso) e checar se não é o resultado, se não for, adicionar o atual em uma lista de anteriores (caminho) e dar pop no primeiro da fila de prioridade.
Quarto:  Repetir passos 1, 2 e 3 até que o a estação atual seja a final e então dar print na tela a lista de anteriores.

### Terceira Questão: O Caixeiro Viajante

Pronta!

Precisamos primeiramente de uma resposta aceitável(uma solução inicial), portanto:
Primeiro passo: Encontrar uma resposta aceitável. 
Segundo passo: Iterativamente vamos permutar 2 em 2 cidades do resultado inicial, avaliando se também é um resultado aceitável e então aplicando a função de avaliação, caso a função seja menor salvamos esse estado como resposta.

### Quarta Questão: Jogo para Dois Jogadores (Minimax)

Pronta!

Com MINIMAX implementado simulamos uma sequência de jogadas e chamamos a função em um ponto crítico para nos dizer qual a melhor jogada.
