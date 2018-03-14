#Função de avaliação
#Buscas por melhoras iterativas com Hill-Climbing

#-------------------------------------------------------------
#Precisamos primeiramente de uma resposta aceitável(uma solução inicial), portanto:
#Primeiro passo: Encontrar uma resposta aceitável. 
#Segundo passo: Iterativamente vamos permutar 2 em 2 cidades do resultado inicial,
#               avaliando se também é um resultado aceitável e então aplicando a função de avaliação,
#               caso a função seja menor salvamos esse estado como resposta.
#-------------------------------------------------------------

def func_avaliacao(grafo, solucao_atual):#A função deve retornar o valor total do percurso
	soma_total = 0
	aux = fazer_copia(solucao_atual)
	valor = 0
	x = 0
	y = 0
	for i in range(0,10):
		x = aux[i]
		y = aux[i+1]
		valor = grafo[x][y]
		if(valor != -1):
			soma_total = soma_total + valor
	return soma_total

def caminho_existe(grafo,solucao_atual): 
	valor = 0
	aux = fazer_copia(solucao_atual)

	if(len(solucao_atual) < 10):
		return 0
	for i in range(0,10):
		x = aux[i]
		y = aux[i+1]
		valor = grafo[x][y]
		if (valor == -1):
			return 0
	return 1

def fazer_copia(a):
	aux = list(a)
	return aux

def subida_da_montanha(grafo,solucao_inicial):#Hill-Climbing, procurando solucao melhor 
	possivel_solucao = fazer_copia(solucao_inicial)
	melhor_ate_agora = 0
	valor_possivel = 0
	valor_inicial = func_avaliacao(grafo,solucao_inicial)
	aux = 0
	for x in range(1,10):#Alternando entre todos os número do miolo [1,...,1]
		aux = possivel_solucao[x]
		for y in range(1,10):#Alternando posição 'x' fixa com todos os outros
			if(x != y):
				possivel_solucao[x] = possivel_solucao[y]
				possivel_solucao[y] = aux
				print('Avaliando:', possivel_solucao)
				if(caminho_existe(grafo,possivel_solucao)):#Se o caminho existir
					valor_possivel = func_avaliacao(grafo,possivel_solucao)
					if(valor_inicial > valor_possivel):#Se o novo caminho for menor
						melhor_ate_agora = fazer_copia(possivel_solucao)
						valor_inicial = valor_possivel
						#A nova solução é a encontrada
				possivel_solucao[y] = possivel_solucao[x]
				possivel_solucao[x] = aux

	if(melhor_ate_agora != 0):
		return melhor_ate_agora
	else:
		return solucao_inicial


				

solucao_inicial = [0,9,1,2,7,3,4,8,6,5,0]


grafo = [[0,30,84,56,-1,-1,-1,75,-1,80],
		 [30,0,65,-1,-1,-1,70,-1,-1,40],
		 [84,65,0,74,52,55,-1,60,143,48],
		 [56,-1,74,0,135,-1,-1,20,-1,-1],
		 [-1,-1,52,135,0,70,-1,122,98,80],
		 [70,-1,55,-1,70,0,63,-1,82,35],
		 [-1,70,-1,-1,-1,63,0,-1,120,57],
		 [75,-1,135,20,122,-1,-1,0,-1,-1],
		 [-1,-1,143,-1,98,82,120,-1,0,-1],
		 [80,40,48,-1,80,35,57,-1,-1,0]]

b = func_avaliacao(grafo,solucao_inicial)
print('O percurso atual é: ',solucao_inicial,' ,com distancia: ',b,'km')
a = subida_da_montanha(grafo,solucao_inicial)
valor = func_avaliacao(grafo,a)
if(a == solucao_inicial):
	print('Não foi encontrada uma solução melhor, portanto o valor ainda é de',valor,'km.')
else:
	print('O novo percurso é:',a,',com distancia:',valor,'km')
