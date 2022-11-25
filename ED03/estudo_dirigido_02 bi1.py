"""
Caixero viajante : descobrir o menor caminho entre as cidades:

Exemplificando o caso n = 4:
se tivermos quatro cidades A, B, C e D, uma rota que o caixeiro deve considerar
poderia ser: saia de A e daí vá para B,
dessa vá para C, e daí vá para D e então volte a A.

ABCDA

Lista do Estudo Dirigido
https://chaua.gitbook.io/inteligencia-computacional/estudos-dirigidos
"""

from dataclasses import dataclass
from dataclasses import field
from typing import List
from typing import Callable
from random import randint
from typing import Tuple
from random import sample
from random import random


#https://www.youtube.com/watch?v=NFVng_313b4

@dataclass
class Cromossomo:
    fitness: Callable[[int], float]
    tamanho: int = 0
    vetor: List[int] = field(default_factory=list)

    def __post_init__(self):
        """Método chamado após o construtor."""
        if not self.vetor:
          self.vetor = [randint(0, 1) for _ in range(self.tamanho)]

    def __getitem__(self, key):
        return self.vetor[key]

    def __setitem__(self, key, value):
        self.vetor[key] = value

    def __len__(self):
        return self.tamanho

    def get_fitness(self):
        return self.fitness(self.vetor)

    # TODO: Implementar a cache do fitness
    
    
    
# 3 Selecao dos pais
"""
paramentro lista, retorna 2 pares de cromosomo
"""
def selecao_aleatoria_com_reposicao(P: List[Cromossomo]) -> List[Tuple[Cromossomo, Cromossomo]]:
    pais = []
    for _ in range(len(P) // 2):
        pais.append(sample(P, 2))

  return pais
    

# Estudo dirigido 02
#Selecao dos pais ->Torneio
def selecao_pais_torneio(P: List[Cromossomo], k_fator) -> List[Tuple[Cromossomo, Cromossomo]]:
  print("selecao pais torneio")
  pais = []
    
#inicio
  
#Enquanto N > 0:  
  for x in range(len(P) ):
  
 # escolha 2 individuos da populacao aleatorio
 
  #r = valor aleatorio entre 0 e 1
    r = randint(0, 1)
  #Se r < k
    if( r < k_fator):
  #  o melhor individuo escolhido
     pais.append(sample(P, x))
  #Senao
    else:
  #  o pior individuo escolhido
      pais.append(sample(P,x)
  #Fim_se
#Fim_Enquanto
  return pais
#Fim


#Estudo dirigido 03

#Selecao dos pais -> Roleta --> com reposicao, --> sem reposicao
# aptidao == fitness

def selecao_aleatoria_roleta(P: List[Cromossomo]) -> List[Tuple[Cromossomo, Cromossomo]]:
#Inicio
 t = 0
 pais = [] 
 # t = soma os valores de aptidao de todos da populacao
  for x in range(len(P) ):
    t += P.get_fitness
    
  #i = 0
  #Enquanto N > 0:
  for i in range(len(P) ) :        
#r = valor aleatorio entre 0 e t
    r = randint(0, t)
  
 #percorre acumulando aptidao_individuos
  #  aptidao_total += individuos.aptidao[i]
    aptidao += P.get_fitness[i]
    
   # Se aptidao >=  r entao:
    if(aptidao += r):
        
    # seleciona o individuo atual
      return P
    #Fim_se
 # Fim_enquanto
#Fim






    
#Algoritmos de recombinação
def crossover_1_ponto_corte(pais: List[Tuple[Cromossomo, Cromossomo]]):
    filhos = []

    # Crossover - 1 ponto de corte
    for p1, p2 in pais:
        corte = randint(1, len(p1) - 1)

        f1 = p1[:corte] + p2[corte:]
        f2 = p2[:corte] + p1[corte:]

        filhos.append(Cromossomo(p1.fitness, len(f1), f1))
        filhos.append(Cromossomo(p1.fitness, len(f2), f2))

    return filhos   



# 2 pontos de corte
def crossover_2_ponto_corte(pais: List[Tuple[Cromossomo, Cromossomo]]):
    filhos = []

    # Crossover - 1 ponto de corte
    for p1, p2 in pais:
        corte = randint(1, len(p1) - 1)

        f1 = p1[:corte] + p2[corte:]
        f2 = p2[:corte] + p1[corte:]
        f3 = p1[:corte] + p1[corte:]
        f4 = p2[:corte] + p2[corte:]
        
        
        filhos.append(Cromossomo(p1.fitness, len(f1), f1))
        filhos.append(Cromossomo(p1.fitness, len(f2), f2))
        filhos.append(Cromossomo(p1.fitness, len(f4), f3))
        filhos.append(Cromossomo(p2.fitness, len(f3), f4))
            
    return filhos   





# 4 mutacao aleatoria
def mutacao_aleatoria(filhos, taxa):

    for cromossomo in filhos:
        for i, pos in enumerate(cromossomo):
            if random() <= taxa:
                cromossomo[i] = 0 if pos else 1

    return filhos


#Crossover com 2 pontos de corte
# --1 corte do cromossomo


#Crossover com 2 pontos de corte
# --2 corte do cromossomo


# --uniforme corte do cromossomo



# 5 Algoritmos de seleção dos sobreviventes
#  P PAIS e  F FILHOS
def elitismo(P, F):
    populacao_total = P + F
    populacao_total.sort(key=lambda c: -c.get_fitness())
    return populacao_total[:len(P * 0.30)]


# torneio

# roleta

# aleatorio

# m- lambada

# ranking




#---------------------------------------------------------------------------------------
#Algoritmo genético

def algoritmo_genetico(tam_populacao,
                       tam_cromossomo,
                       max_geracoes,
                       taxa_mutacao,
                       fitness,
                       selecionar_pais,
                       realizar_crossover,
                       realizar_mutacao,
                       selecionar_sobreviventes):

    # 1. t = 0
    t = 0

    # 2. Inicializar população P0
    P = [Cromossomo(fitness, TAM_CROMOSSOMO) for _ in range(TAM_POPULACAO)]

    # print("# População inicial")
    # pprint([c.vetor for c in P])

    # 3. Enquanto critério de parada == falso
    # TODO: implementar outros critérios de parada
    while t < max_geracoes:

        #   3.1 Avaliar população (Pt)
        #   OK! Avaliação delegada para o cromossomo 

        #   3.2 P’ = Selecionar pais (Pt)
        pais = selecionar_pais(P)

        #   3.3 F  = Aplicar recombinação e mutação (P’)
        F = realizar_crossover(pais)
        F = realizar_mutacao(F, TAXA_MUTACAO)

        #   3.4 Avaliar população (F)
        #   OK! Avaliação delegada para o cromossomo 

        #   3.5 Pt+1 = Selecionar sobreviventes(Pt + F)
        P = selecionar_sobreviventes(P, F)

        # Imprime o melhor individuo
        print(f'| {t:04d} | {P[0].vetor} | {P[0].get_fitness():4d} |')

        #   3.6 t = t + 1
        t += 1
    
    print()
    print(f'Melhor solução.: {P[0].vetor}')
    print(f'Fitness........: {P[0].get_fitness()}')

    return P[0]
    
    
    
    
    
# 1. Modelar o genótipo e fenótipo do cromossomo
# Cromomossomo normal, sem nenhuma codificação especial para esse problema

# 2. Criar a função de avaliação
def fitness_maximizar_1(cromossomo):
    return sum(cromossomo)

# 3. Parametrizar o AG
TAM_POPULACAO = 10
TAM_CROMOSSOMO = 100
MAX_GERACOES = 10

TAXA_MUTACAO = 0.005
TORNEIO = 2

# 4. Executar
solucao = algoritmo_genetico(tam_populacao = TAM_POPULACAO,
                             tam_cromossomo = TAM_CROMOSSOMO,
                             max_geracoes = MAX_GERACOES,
                             taxa_mutacao = TAXA_MUTACAO,
                             fitness = fitness_maximizar_1,
                             selecionar_pais = selecao_aleatoria_com_reposicao,
                             realizar_crossover = crossover_1_ponto_corte,
                             realizar_mutacao = mutacao_aleatoria,
                             selecionar_sobreviventes = elitismo)


