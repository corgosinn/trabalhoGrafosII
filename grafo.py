from asyncio.windows_events import NULL
from dis import dis


class Grafo:

    def __init__(self, num_vert=0, num_arestas=0, lista_adj=None, mat_adj=None):
        self.num_vert = num_vert
        self.num_arestas = num_arestas
        if lista_adj is None:
            self.lista_adj = [[] for i in range(num_vert)]
        else:
            self.lista_adj = lista_adj
        if mat_adj is None:
            self.mat_adj = [[0 for j in range(num_vert)]
                            for i in range(num_vert)]
        else:
            self.mat_adj = mat_adj

    def add_aresta(self, u, v, w=1):
        """Adiciona aresta de u a v com peso w"""
        self.num_arestas += 1
        if u < self.num_vert and v < self.num_vert:
            self.lista_adj[u].append((v, w))
            self.mat_adj[u][v] = w
        else:
            print("Aresta invalida!")

    def remove_aresta(self, u, v):
        """Remove aresta de u a v, se houver"""
        if u < self.num_vert and v < self.num_vert:
            if self.mat_adj[u][v] != 0:
                self.num_arestas += 1
                self.mat_adj[u][v] = 0
                for (v2, w2) in self.lista_adj[u]:
                    if v2 == v:
                        self.lista_adj[u].remove((v2, w2))
                        break
            else:
                print("Aresta inexistente!")
        else:
            print("Aresta invalida!")

    def ler_arquivo(self, nome_arq):
        """Le arquivo de grafo no formato dimacs"""
        try:
            arq = open(nome_arq)
            # Leitura do cabecalho
            str = arq.readline()
            str = str.split(" ")
            self.num_vert = int(str[0])
            cont_arestas = int(str[1])
            # Inicializacao das estruturas de dados
            self.lista_adj = [[] for i in range(self.num_vert)]
            self.mat_adj = [[0 for j in range(self.num_vert)]
                            for i in range(self.num_vert)]
            # Le cada aresta do arquivo
            for i in range(0, cont_arestas):
                str = arq.readline()
                str = str.split(" ")
                u = int(str[0])  # Vertice origem
                v = int(str[1])  # Vertice destino
                w = int(str[2])  # Peso da aresta
                self.add_aresta(u, v, w)
        except IOError:
            print("Nao foi possivel encontrar ou ler o arquivo!")

    def BELLMAN_FORD(self, s, destino):
        dist = [float('inf') for v in range(self.num_vert)]
        pred = [NULL for v in range(self.num_vert)]
        dist[s] = 0
        for j in range(self.num_vert - 1):
            mudou = 0
            for u in range(len(self.lista_adj)):
                for (v1, v2) in self.lista_adj[u]:
                    mudou = 1
                    if dist[v1] > dist[u] + v2:
                        dist[v1] = dist[u] + v2
                        pred[v1] = u
            if mudou == 0:
                break

        caminho = self.print_caminho(pred, s, destino)
        self.soma_custo(s, destino, dist, caminho)
        return dist

    def soma_custo(self, origem, destino, dist, caminho, busca=0):
        print(f"Custo: {dist[destino]}")

    def print_caminho(self, pred, origem, destino):
        x = destino
        caminho = []
        while(x != origem):
            caminho.append(x)
            x = pred[x]
        caminho.append(origem)
        caminho.reverse()

        print(f"Caminho: {caminho}")
        return caminho
