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




with open('lensesdataset','r') as csvfile:
	lines = csv.reader(csvfile)
	#for row in lines:
	#	print(row[0])

k = 0
print('Digite o "k" que você deseja:')
k = int(input()) # 'k' NEAREST NEIGHBORS


 

