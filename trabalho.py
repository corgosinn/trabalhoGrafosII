# Thiago Corgosinho Silva - 20.2.8117
from prettytable import PrettyTable
import grafo
import time
import os
import csv

# LER ARQUIVOS CSV
disciplinaCSV = []
professoresCSV = []

# MENU DE ARQUIVOS
fileDisciplina = 'disciplinas_toy.csv'
fileProfessores = 'professores_toy.csv'
print("Escolha os nomes dos arquivos: ")
print("1- discplinas_toy.csv e professores_toy.csv")
print("2- disciplinas.csv e professores.csv")
print('3- Outros')

op = int(input("Digite: "))

if op == 1:
    fileDisciplina = 'disciplinas_toy.csv'
    fileProfessores = 'professores_toy.csv'
elif op == 2:
    fileDisciplina = 'disciplinas.csv'
    fileProfessores = 'professores.csv'
else:
    print("Digite o nome do arquivo de disciplina: ")
    fileDisciplina = input()
    print("Digite o nome do arquivo de professores: ")
    fileProfessores = input()


somaFluxo = 0
# Inicia o time
inicioTime = time.time()
# LER DISCIPLINAS CSV
try:
    fileDisciplinaCSV = open(os.path.join(os.path.dirname(__file__),
                                          f'csv\\{fileDisciplina}'), encoding='utf-8', newline='')
    csvReader = csv.reader(fileDisciplinaCSV, delimiter=';')
    for x, dadoCsv in enumerate(csvReader):
        if(x != 0):
            disciplinaCSV.append(dadoCsv)
    fileDisciplinaCSV.close()
except:
    print("Erro ao ler disciplinas")

# LER PROFESSORES CSV

try:
    fileProfessoresCSV = open(os.path.join(os.path.dirname(__file__),
                                           f'csv\\{fileProfessores}'), encoding='utf-8', newline='')
    csvProfReader = csv.reader(fileProfessoresCSV, delimiter=';')
    for x, dadoCsv in enumerate(csvProfReader):
        if(x != 0):
            professoresCSV.append(dadoCsv)
    fileDisciplinaCSV.close()
except:
    print("Erro ao ler professores")

# DEFINIR GRAFOS

for x in range(0, len(professoresCSV)):
    somaFluxo = somaFluxo + int(professoresCSV[x][1])
grafo = grafo.Grafo()
grafo.ler_arquivo(professoresCSV, disciplinaCSV, somaFluxo)

dados = grafo.SCM()
qtdTurmas = dados[0]


# PRINTA TABELA NA TELA
table = PrettyTable(['Professor', 'Disciplina', 'Nome', 'Turmas', 'Custo'])
for linha in range(grafo.contagem):
    for coluna in range(len(grafo.mat_adj[linha])):
        if(grafo.mat_adj[linha][coluna] == 1 and qtdTurmas[grafo.numeroAresta[linha][coluna]] > 0 and grafo.nome[coluna] != 'S'):
            table.add_row([grafo.nome[linha], grafo.nome[coluna], grafo.nomeCompleto[coluna],
                           qtdTurmas[grafo.numeroAresta[linha][coluna]], dados[1][grafo.numeroAresta[linha][coluna]]])
print(table)
# Printa na tela o tempo
print(f"Tempo de execução: {round(time.time()-inicioTime,4)} segundos")
