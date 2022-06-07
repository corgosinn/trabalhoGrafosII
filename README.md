1. Objetivos.
 Aplicar os conhecimentos em algoritmos para resolver um problema real.
 Aprimorar a habilidade de programa¸c˜ao de algoritmos em grafos.
 Refor¸car o aprendizado sobre os algoritmos de fluxo em redes.
2. Descri¸c˜ao.
O trabalho consiste em resolver o problema da aloca¸c˜ao de professores `as disciplinas do
DECSI/UFOP atrav´es de algoritmos de fluxo em redes. Cada professor leciona duas ou
trˆes disciplinas e define, a cada semestre quais disciplinas tem preferˆencia por lecionar
dentre as que s˜ao ofertadas pelo DECSI. Um solu¸c˜ao para esse problema consiste em
uma atribui¸c˜ao de disciplinas aos professores de modo a maximizar o atendimento de
suas preferˆencias. Nesse trabalho ser´a considerado o cen´ario de aloca¸c˜ao para o pr´oximo
semestre, 2022/1. Cada professor define compatibilidade com 5 disciplinas distintas, em
ordem decrescente de preferˆencia. Pode haver mais de uma turma de uma determinada
disciplina, como ´e o caso de Banco de Dados I, que ´e ofertada para os cursos de Sistemas
de Informa¸c˜ao e Engenharia de Computa¸c˜ao. A entrada ser˜ao dois arquivos no formato
.csv (separado por v´ırgulas), um de professores e outro de disciplinas conforme o exemplo
abaixo:
professores.csv
Professor # Disciplinas Preferˆencia 1 Preferˆencia 2 Preferˆencia 3
George Fonseca 2 CSI105 CSI466 CSI601
Bruno Monteiro 3 CSI601 CSI602 CSI466
disciplinas.csv
Disciplina Nome # Turmas
CSI105 Alg. e Estruturas de Dados III 1
CSI466 Teoria dos Grafos 1
CSI601 Banco de Dados I 2
CSI602 Banco de Dados II 1
Seu programa deve ler esses arquivos de entrada e criar a rede de fluxo correspondente ao
problema de aloca¸c˜ao. A rede de fluxo ter´a quatro camadas, um com o n´o de super oferta,
outra com n´os representando os professores, outra representando as disciplinas e, por fim,
o n´o de super demanda. Com rela¸c˜ao `as preferˆencias, os seguintes custos incorrem: