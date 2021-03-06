from asyncio.windows_events import NULL


class Grafo:

    def __init__(self, num_vert=0, num_arestas=0):
        self.quantidade_vertices = num_vert
        self.quantidade_arestas = num_arestas
        self.nome = ['' for i in range(num_vert)]
        self.mat_adj = [[0 for j in range(num_vert)]
                        for i in range(num_vert)]
        self.w_adj = [[0 for j in range(num_vert)]  # Peso separado da matriz original
                      for i in range(num_vert)]
        self.c_adj = [[0 for j in range(num_vert)]  # Matriz de c
                      for i in range(num_vert)]
        self.numeroAresta = [[0 for j in range(num_vert)]  # Cada aresta tera um numero
                             for i in range(num_vert)]
        self.b = [0 for i in range(num_vert)]  # Matriz de b
        self.lista_adj = []  # Lista de adj
        self.contagem = 0  # Inicio dos vertices das disciplinas
        self.nomeCompleto = ['' for i in range(num_vert)]

    def addAresta(self, u, v, w=1, c=0, op=0):
        if u < self.quantidade_vertices and v < self.quantidade_vertices:
            self.numeroAresta[u][v] = self.quantidade_arestas
            self.quantidade_arestas += 1
            self.mat_adj[u][v] = 1
            self.w_adj[u][v] = w
            self.c_adj[u][v] = c
            self.lista_adj.append((u, v, w))

        else:
            print("Aresta invalida!")

    def ler_arquivo(self, csvProf, csvDisc, b):
        """Le arquivo de grafo atravez do csv"""
        try:

            self.quantidade_arestas = 0
            self.quantidade_vertices = 1
            dicPrioridades = {0: 0, 1: 3, 2: 5, 3: 8, 4: 10}
            dicProfs = []
            for elem in csvProf:
                if(int(elem[1]) > 0 and len(elem[0]) > 0):
                    self.quantidade_vertices = self.quantidade_vertices + 1
            for elem in csvDisc:
                if len(elem[0]) > 0:
                    self.quantidade_vertices = self.quantidade_vertices + 1
            self.lista_adj = []
            self.mat_adj = [[0 for j in range(self.quantidade_vertices)]
                            for i in range(self.quantidade_vertices)]
            self.c_adj = [[0 for j in range(self.quantidade_vertices)]
                          for i in range(self.quantidade_vertices)]
            self.w_adj = [[0 for j in range(self.quantidade_vertices)]
                          for i in range(self.quantidade_vertices)]
            self.numeroAresta = [[0 for j in range(self.quantidade_vertices)]
                                 for i in range(self.quantidade_vertices)]
            self.nome = ['' for i in range(self.quantidade_vertices)]
            self.nomeCompleto = ['' for i in range(self.quantidade_vertices)]
            self.b = [0 for i in range(self.quantidade_vertices)]

            self.nome[0] = 'S'
            self.nome[self.quantidade_vertices-1] = 'R'
            indiceDisciplinas = 1
            self.b[0] = b
            self.b[self.quantidade_vertices-1] = -(b)
            for indice, elem in enumerate(csvProf):
                if(int(elem[1]) > 0 and len(elem[0]) > 0):
                    self.nome[indiceDisciplinas] = elem[0]
                    indiceDisciplinas = indiceDisciplinas + 1
                    self.addAresta(0, indice+1, int(elem[1]), elem[1])
            self.contagem = indiceDisciplinas
            for indice, elem in enumerate(csvDisc):
                if len(elem[0]) > 0:
                    self.nome[indiceDisciplinas] = elem[0]
                    self.nomeCompleto[indiceDisciplinas] = elem[1]
                    indiceDisciplinas = indiceDisciplinas + 1
            for indice, elem in enumerate(csvProf):
                dicProfs.clear()
                dicProfs.append(elem[2])
                dicProfs.append(elem[3])
                dicProfs.append(elem[4])
                dicProfs.append(elem[5])
                dicProfs.append(elem[6])
                for materia in range(1, self.quantidade_vertices):
                    if self.nome[materia] in dicProfs and self.nome[materia] != '':
                        self.addAresta(
                            indice+1, materia, dicPrioridades[dicProfs.index(self.nome[materia])], 9999)
            for indice, elem in enumerate(csvDisc):
                if len(elem[0]) > 0:
                    self.addAresta(self.nome.index(
                        elem[0]), self.quantidade_vertices-1, 0, elem[2])

        except IOError:
            print("Nao foi possivel encontrar ou ler o arquivo!")

    def remove_aresta(self, u, v):

        if u < self.quantidade_vertices and v <= self.quantidade_vertices:
            if self.mat_adj[u][v] != 0:
                self.quantidade_arestas -= 1
                self.mat_adj[u][v] = 0
                self.c_adj[u][v] = 0
                self.lista_adj.remove((u, v, self.w_adj[u][v]))
                self.w_adj[u][v] = 0
            else:
                print("Aresta inexistente!")
                return -1
        else:
            print("Aresta invalida!")

    def bellman_ford(self, s=0):
        distancia = [float("inf") for _ in range(
            self.quantidade_vertices)]  # Distance from s
        # Predecessor in shortest path from s
        predecessores = [None for _ in range(self.quantidade_vertices)]
        distancia[s] = 0
        for var in range(self.quantidade_vertices):
            updated = False
            for (u, v, w) in self.lista_adj:
                if distancia[v] > distancia[u] + w:
                    distancia[v] = distancia[u] + w
                    predecessores[v] = u
                    updated = True
            if not updated:
                break
        caminho = []  # Recebe o caminho atravez dos predecessores
        if predecessores[len(predecessores) - 1] != None:
            n = predecessores[len(predecessores) - 1]
            caminho.append(self.quantidade_vertices-1)
            while(True):
                caminho.append(n)
                if(n == 0):
                    break
                n = predecessores[n]
            caminho.reverse()
            min = float("inf")
            for x in range(len(caminho)):
                if x != len(caminho)-1:
                    if int(self.c_adj[caminho[x]][caminho[x+1]]) < float(min):
                        min = self.c_adj[caminho[x]][caminho[x+1]]
            # Se houver caminho minimo
            return predecessores[self.quantidade_vertices - 1], caminho, min
        else:
            return None, None, 0  # Se n??o existir caminho minimo

    def SCM(self):  # Sucessores caminhos minimos
        F = [0 for i in range(self.quantidade_arestas*2)]
        CUSTO = [0 for i in range(self.quantidade_arestas*2)]
        listaBellmanFord = self.bellman_ford()  # Pega o caminho minimo

        # Euquanto houver fluxo de S e caminho minimo de S ate R
        while(listaBellmanFord[0] != None and self.b[0] > 0):

            C = listaBellmanFord[1]
            f = int(listaBellmanFord[2])
            for elementosEmC in range(len(C)):
                # Enquanto nao chegar no final do caminho
                if elementosEmC != len(C)-1:
                    u = C[elementosEmC]
                    v = C[elementosEmC+1]
                    F[self.numeroAresta[u][v]] = F[self.numeroAresta[u]
                                                   [v]] + f  # Aumenta o fluxo
                    CUSTO[self.numeroAresta[u][v]
                          ] = CUSTO[self.numeroAresta[u][v]] + self.w_adj[u][v]
                    # Reduzir capacidade
                    self.c_adj[u][v] = int(self.c_adj[u][v]) - f
                    if self.c_adj[u][v] == 0:
                        if(self.remove_aresta(u, v) == -1):
                            return
                    if self.mat_adj[v][u] == 0:
                        self.addAresta(v, u, -(self.w_adj[u][v]), 999, 1)
                    self.c_adj[v][u] = self.c_adj[v][u] + \
                        f  # Aumentar capacidade arco reverso
                    if F[self.numeroAresta[v][u]] != 0:
                        F[self.numeroAresta[v][u]] = F[self.numeroAresta[v]
                                                       [u]] - f  # Reduzir fluxo arco reverso

            self.b[0] = self.b[0] - f
            self.b[self.quantidade_vertices -
                   1] = self.b[self.quantidade_vertices-1] + f
            listaBellmanFord = self.bellman_ford()
        return F, CUSTO
