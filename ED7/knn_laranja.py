# -*- coding: utf-8 -*-
""""
Carrega o CSV, e implementa 
Algoritimo KNN
"""

import csv
import pandas 
import math
import numpy


"""
abrindo o arquivo com os dados
"""

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
 
#------------------------------------------
def manhattan_distance(point1, point2):
    distance = 0
    for x1, x2 in zip(point1, point2):
        difference = x2 - x1
        absolute_difference = abs(difference)
        distance += absolute_difference

    return distance
  
    
#-------------------------------------


# campos do arquivo
campos=['name','diameter','weight','red','green','blue'] 



with open("./citrus.csv",'r') as arq:
    
    csv_arq = csv.reader(arq, delimiter=',')
    for linhas in csv_arq:
        print(linhas)
        
#abrindo o arquivo para separar os dados        
dados = pandas.read_csv('citrus.csv') 

#tamanho da linha e colunas da matriz
tam_linha = 5
tam_coluna = 0

matriz = []
for i, linha in dados.iterrows():
    matriz.append(linha.to_list())
    tam_coluna+= 1  
    
    
print(matriz[55][0])

print("tamanho total colunas", tam_coluna)

##----Lista das laranjas
laranja=[]

## lista das toranjas
toranja=[]


#----------------------------------------

"""
classificando qual é de qual grupo
"""
# percorrendo a matriz 

#percorrendo os dados e classificando em duas listas
for x ,fruta in tam_coluna:
  if matriz[x][0] == 'orange':
    laranja.append(fruta.to_list)
    print(matriz[x][0])
  else:
    toranja.append(fruta.to_list)   
    print(matriz[x][0])


"""
implementacao do algoritimo
"""
dista_laranjas =[]
quant_laranjas =0
quant_toranjas =0

# 1 Receba um dado não classificado e meça distância do novo dado 
#em relação a cada um dos outros dados que já estão classificados;

#medindo a distancia das laranjas
for z in laranja:
  #calcula a distancia  
  dis =dist_eclidiana(laranja[z][1],laranja[z+1][2], laranja[z][3], laranja[z][4])
  dist2 = dist_eclidiana(laranja[z+1][1],laranja[z+1][2], laranja[z+1][3], laranja[z+1][4])
##classifica
# 2  Selecione as K menores distâncias

#3  Verifique a(s) classe(s) dos dados que tiveram as K menores distâncias e contabilize a quantidade de vezes que cada classe que apareceu;

  if dis < dist2:
    quant_laranjas+=1  
    dista_laranjas.append(laranja)
  else:
   dista_laranjas[z+1].append(laranja)   
   quant_laranjas+=1


#---------classficacao das toranjas
dist_toranja =[] 

#medindo a distancia das toranjas]
for z in toranja:
  #calcula a distancia  
  dis =dist_eclidiana(toranja[z][1],toranja[z+1][2],toranja[z][3], toranja[z][4])
  dist2 = dist_eclidiana(toranja[z+1][1],toranja[z+1][2], toranja[z+1][3], toranja[z+1][4])

# 2  Selecione as K menores distâncias
##classifica

#3  Verifique a(s) classe(s) dos dados que tiveram as K menores distâncias e contabilize a quantidade de vezes que cada classe que apareceu;

  if dis < dist2:
    dista_toranja.append(laranja)
    quant_laranjas+=1
  else:
    dista_toranja[z+1].append(laranja)   
    quant_laranjas+=1

# 4 Classifique esse novo dado como pertencente à classe que mais apareceu.
 
print("quantidade de laranjas: ",quant_laranjas)

print("quantidade de toranjas: ", quant_toranjas)




