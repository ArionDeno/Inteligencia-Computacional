# -*- coding: utf-8 -*-
"""
Implemente um perceptron e treine ele para reconhecer o seguinte exemplo:
    Pessoa        --Cientista--|--Escritor--|--Homen--|--Mulher--
 Albert Eisten      V                        V
--------------|-----------|------------|----------|-------------------
Machado de assis               V            V
--------------|-----------|------------|----------|-------------------
Raquel Queiroz                   V                      V        
--------------|-----------|------------|----------|-------------------
Marie Currie         V                                  V                 
--------------|-----------|------------|----------|-------------------
"""


dados=[]



from matplotlib.colors import ListedColormap
import matplotlib.pyplot as plt
import numpy 
import pandas
import csv

 
"""
classe do perceptron
"""
class Perceptron:

#construtor
  def __init__(self, eta = 0.01, n_inter = 10):
    self.eta = eta
    self.n_inter = n_inter

# valor de entradas
  def net_entrada(self, X):
    return(numpy.dot(X,self.w[1:]) + self.w[0])


# meotodo predicado
  def predicado(self,X):
    return numpy.where(self.net_entrada(X) >= 0.0 , 1, -1)


# metodo para treinar o perceptron
  def treinar(self, X,y):
    self.w = numpy.zeros(1+ X.shape[1])
    self.erros= []
    
#laoco de interacao
    for i in range(self.n_inter):
      erros  =0
      
      for xi , target in zip(X,y):
        atualiza = self.eta * (target - self.predicado(xi))
        self.w[1:] += atualiza * xi
        self.w[0] += atualiza 
        erros += int(atualiza != 0.0)
      self.erros.append(erros)
#------------------------------------------------


dados_lido =[]

with open("./dados.csv",'r') as arq:
  csv_arq = csv.reader(arq,delimiter=',')
  for x, linhas in csv_arq:
    print(linhas)
    dados_lido.append(linhas)

    
    
#-------------------------------------------------
perceptron = Perceptron(eta= 0.1, n_inter=10)

#metodo treinar 
perceptron.treinar(dados_lido, 4)

