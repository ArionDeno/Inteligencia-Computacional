# -*- coding: utf-8 -*-
"""
carregar os dados do vinho tinto

classficar com k-Means
"""
#https://medium.com/programadores-ajudando-programadores/k-means-o-que-%C3%A9-como-funciona-aplica%C3%A7%C3%B5es-e-exemplo-em-python-6021df6e2572


import csv
import pandas
import math
import random


# distancia eucliana
def dist_eclidiana(xb,xa,yb,ya):
    # distancias de X e y
    dist_x = xb - xa
    dist_y = yb - ya
    # eleva a 2 os valores
    math.pow(dist_x,2)
    math.pow(dist_y, 2)
    # tira a raiz e retona
    return math.sqrt(dist_x + dist_y)




with open("./winequality-red.csv",'r') as arq:

    csv_arq = csv.reader(arq, delimiter=';')
    for linhas in csv_arq:
        print(linhas)


#abrindo o arquivo para separar os dados
dados = pandas.read_csv('winequality-red.csv', delimiter=';')

#---------------------------------------------------------------------
# 1 - achar número de clusters (ou agrupamentos).

# para cada atributo
# maior de cada vira um centroid

#separamos em lista

acidez_fixa =[]
acidez_volatil =[]
acido_citrico =[]
acucar_residual =[]
cloretos =[]
livre_dioxido_enxofre =[]
total_dioxido_enxofre =[]
densidade = []
ph = []
sulfatos =[]
alcool =[]
qualidade =[]

#vemos qual maior e vira centroid

maior =0.0







matriz = []

for i, linha in dados.iterrows():
    matriz.append(linha.to_list())
    print(dados)
#classicando em cada lista
    acidez_fixa.append(matriz[0][i])
    acidez_volatil.append(matriz[1][i])
    acido_citrico.append(matriz[2][i])
    acucar_residual.append(matriz[3][i])
    cloretos.append(matriz[4][i])
    livre_dioxido_enxofre.append(matriz[5][i])
    total_dioxido_enxofre.append(matriz[6][i])
    densidade.append(matriz[7][i])
    ph.append(matriz[8][i])
    sulfatos.append(matriz[9][i])
    alcool.append(matriz[10][i])
    qualidade.append(matriz[11][i])




##print(matriz[55][8])



# 2 - definir, aleatoriamente, um centroide para cada cluster

centroid_acidez_fixa = random.randrange(0,len(acidez_fixa))
centroid_acidez_volatil = random.randrange(0,len(acidez_volatil))
centroid_acido_citrico = random.randrange(0,len(acido_citrico))
centroid_acucar_residual = random.randrange(0,len(acucar_residual))
centroid_cloretos =  random.randrange(0,len(cloretos))
centroid_livre_dioxido_enxofre = random.randrange(0,len(livre_dioxido_enxofre))
centroid_total_dioxido_enxofre = random.randrange(0,len(total_dioxido_enxofre))
centroid_densidade = random.randrange(0,len(densidade))
centroid_ph = random.randrange(0,len(ph))
centroid_sulfatos = random.randrange(0,len(sulfatos))
centroid_alcool = random.randrange(0,len(alcool))
centroid_qualidade = random.randrange(0,len(qualidade))


while(centroid_qualidade != 0 and centroid_acidez_volatil !=0 and centroid_acido_citrico !=0 and
      centroid_acucar_residual !=0 and centroid_cloretos != 0 and centroid_livre_dioxido_enxofre !=0 and
      centroid_total_dioxido_enxofre !=0 and centroid_densidade !=0 and centroid_ph !=0 and centroid_sulfatos !=0 and
       centroid_alcool != 0 and centroid_qualidade != 0):

# 3 - calcular, para cada ponto, o centroides de menor distância. Cada ponto pertencerá ao centroide mais próximo

#----------------------------
  for x in len(acidez_fixa):
      if centroid_acidez_fixa < acidez_fixa[x]:
        #insere no final
        acidez_fixa[x *-1].append(acidez_fixa[x])

#-----------------------------
  for x in len(acidez_volatil):
      if centroid_acidez_volatil < acidez_volatil[x]:
      #insere no final
        acidez_volatil[x *-1].append(acidez_volatil)

#-----------------------------
  for x in len(acido_citrico):
      if centroid_acido_citrico < acido_citrico[x]:
       #insere no final
        acido_citrico[x *-1].append(acido_citrico)

#-----------------------------
  for x in len(acucar_residual):
      if centroid_acucar_residual < acucar_residual[x]:
      #insere no final
        acucar_residual[x *-1].append(acucar_residual)

#-----------------------------
  for x in len(cloretos):
      if centroid_cloretos < cloretos[x]:
      #insere no final
        cloretos[x *-1].append(cloretos)

#-----------------------------
  for x in len(livre_dioxido_enxofre):
      if centroid_livre_dioxido_enxofre < livre_dioxido_enxofre[x]:
      #insere no final
        livre_dioxido_enxofre[x *-1].append(livre_dioxido_enxofre)

#-----------------------------
  for x in len(total_dioxido_enxofre):
      if centroid_total_dioxido_enxofre < total_dioxido_enxofre[x]:
      #insere no final
        total_dioxido_enxofre[x *-1].append(total_dioxido_enxofre)

#-----------------------------
  for x in len(densidade):
      if centroid_densidade < densidade[x]:
      #insere no final
        densidade[x *-1].append(densidade)

#-----------------------------
  for x in len(ph):
      if centroid_ph < ph[x]:
       #insere no final
        ph[x *-1].append(ph)

#-----------------------------
  for x in len(sulfatos):
      if centroid_sulfatos < sulfatos[x]:
      #insere no final
        sulfatos[x *-1].append(sulfatos)

#-----------------------------
  for x in len(alcool):
      if centroid_alcool < alcool[x]:
      #insere no final
         alcool[x *-1].append(alcool)

#-----------------------------
 for x in len(qualidade):
     if centroid_qualidade < qualidade[x]:
      #insere no final
         qualidade[x *-1].append(qualidade)

# 4 - A nova posição do centroide deve ser a média da posição de todos os pontos do cluster.

# 5 - repete o passo 3 e 4 ate ter posicao mais proximas dos objetos
