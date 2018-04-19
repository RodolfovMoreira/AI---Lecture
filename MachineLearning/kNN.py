#O DATASET ESCOLHIDO FOI O DE LENSES
#FOI NECESSÁRIO PRIMEIRAMENTE DISPOR OS DADOS EM FORMATO .csv

import csv
import math

def distanciaEuclidiana(dado1, dado2):
	distancia = 0
	resultado = 0
	for x in range(1,4):
		distancia = distancia + pow(dado1[x] - dado2[x], 2)

	resultado = math.sqrt(distancia)
	return resultado

def tranformToInt(row):
	retorno = []
	aux = 0
	for x in range(0,6):
		aux = int(row[x])
		retorno.append(aux)
	return retorno


def retornarBase():
	linhas = []
	aux = 0
	with open('lensesdataset','r') as csvfile:
		lines = csv.reader(csvfile)
		for row in lines:
			aux = tranformToInt(row)
			linhas.append(aux)
		#print(linhas)
		return linhas

def retornaMenor(lista):
	aux = 0
	pos = 0
	for x in range(0,len(lista)):
		if(aux <= lista[x]):
			aux = lista[x]
			pos = x
	return aux,pos


k = 0
dado_input = 0
lista_distancias = []
indice = 0
lines = []
classe1 = 0
classe2 = 0
classe3 = 0
lista_menoresdistancias = []
posicao = 0
tamanho = 0

print('Digite o "k" que você deseja:')
k = int(input()) # 'k' NEAREST NEIGHBORS
print('Seguindo o formato "x x x x x", onde x são números, digite o dado a ser avaliado:')
dado_input = [int(i) for i in input().split()]

lines = retornarBase()
#print(lines)

for elemento in lines:
	lista_distancias.append(distanciaEuclidiana(dado_input,elemento))
	indice = indice + 1

while k > 0:
	tamanho,posicao = retornaMenor(lista_distancias)
	lista_menoresdistancias.append(lines[posicao])
	#print(lista_distancias)
	lista_distancias.remove(tamanho)
	#print(lista_distancias)
	k = k - 1

for elemento in lista_menoresdistancias:
	#print(elemento)
	if(elemento[5] == 1):
		classe1 = classe1 + 1
	elif(elemento[5] == 2):
		classe2 = classe2 + 1
	else:
		classe3 = classe3 + 1

print('Elementos próximos da classe 1:',classe1,'Elementos próximos da classe 2:',classe2,'Elementos próximos da classe 3:',classe3)
if(classe1 >= classe2 and classe1 >= classe3):
	print('O elemento pertence à classe 1!')
elif(classe2 > classe1 and classe2 > classe3):
	print('O elemento pertence à classe 2!')
else:
	print('O elemento pertence à classe 3!')
print()
print('Caso haja numero de casos iguais entre o 1 e o 3, é preferível que o paciente use as lentes.')
print('Caso haja numero de casos iguais entre o 2 e o 3, é preferível que o paciente não use as lentes.')