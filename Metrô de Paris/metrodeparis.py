#Formular em questão de estado inicial, final
#Função de avaliação
#Busca Heurística com A*


#----------------------------------------------
#A abordagem do problema será dar para cada ponto o trajeto mais rápido para todos os outros.
#
#Função de avaliação será o tempo gasto, somando: A velocidade do metro (30km/h) e caso haja baldeação, 4 min por linha trocada.
#Teremos que ter 4 listas para demonstar as estações de cada linha.
#Primeiro: Função irá procurar na mesma linha a estação com menor distância aplicando a função de avaliação
#Segundo: Ir adicionando em uma fila de prioridade as estações da linha com seus respectivos pesos
#Terceiro: Retirar o primeiro da fila (menor peso) e checar se não é o resultado, se não for, 
#          adicionar o atual em uma lista de anteriores e dar pop da fila de prioridade.
#Quarto:  
#----------------------------------------------

#Pega as listas onde se encontram o atual 
#Checa se é atual é igual ao final, se sim imprime a lista de prioridades (ver peculiaridades)
#Para cada elemento de cada lista faz todas as distancias (tirando a origem) para o destino com o seguinte if: -HEURISTICA - pronta
#   			SE elemento é adjacente com destino: 
#						salva na fila de prioridade a distancia
#               ELSE:
#						salva na fila de prioridade a distancia+4
#Adiciona atual origem na fila do caminho 
#Tira o primeiro da fila de prioridade e repete o procedimento




from queue import PriorityQueue

class Estacao:
	#Classe comum para as estações
	def __init__(self, nome,valor):
		self.nome = nome
		self.valor = valor
		self.distancia = 0

	def set_Distancia(self, distancia):
		self.distancia = distancia

	def __lt__(self, other):
		self_distancia = self.distancia
		other_distancia = other.distancia
		if(self_distancia < other_distancia):
			return 1
		else:
			return 0

def dist_entrepontos(grafo, A, B):#Retorna a distância entre os dois pontos
	linha = A.valor - 1
	coluna = B.valor - 1

	resultado = grafo[linha][coluna]
	return resultado

def esta_nalista(A, lista): #Checa se determinado elemento está em uma lista
	if A in lista:
		return 1
	else:
		return 0

def ret_mesmovalor(A): #Como python é tipado, temos que copiar o objeto dessa forma
	aux = A
	return aux

def estao_mesmalista(azul, amarela, vermelha, verde, atual, destino): #Checa que dois elementos estão na mesma lista
	
	if((atual in vermelha)&(destino in vermelha)):
		return 1
	elif ((atual in verde)&(destino in verde)):
		return 1
	elif((atual in amarela)&(destino in amarela)):
		return 1
	elif((atual in azul)&(destino in azul)):
		return 1
	else:
		return 0

def fun_heuristica(grafo, azul, amarela, vermelha, verde, atual, destino): #Retorna o operando para adicionar na fila de prioridade
	
	objt = atual

	if(estao_mesmalista(azul, amarela, vermelha, verde, atual, destino)):
		aux = dist_entrepontos(grafo,atual,destino)
	else:
		aux = dist_entrepontos(grafo,atual,destino) + 4
	
	objt.set_Distancia(aux)
	return objt

def search_A(grafo, azul, amarela, vermelha, verde, atual, destino):
	lista_de_prioridades = PriorityQueue() #Lista de prioridade
	lista = [] #Lista com caminhos gravados
	aux = 0
	aux2 = ret_mesmovalor(atual)
	lista.append(aux2) #Começamos do atuals

	while atual != destino:
		if(esta_nalista(atual,azul)): #Se atual estiver na lista carrega na PriorityQueue todas as dist de cada um pro destino
			azul.remove(atual)
			tam = len(azul)
			for i in range(0,tam):
				aux = fun_heuristica(grafo, azul, amarela, vermelha, verde, azul[i], destino)
				#print(aux.nome, 'e', aux.distancia, 'na lista azul')
				if(aux != atual):
					aux2 = ret_mesmovalor(aux)
					lista_de_prioridades.put(aux2)
		if(esta_nalista(atual,amarela)):#Se atual estiver na lista carrega na PriorityQueue todas as dist de cada um pro destino
			amarela.remove(atual)			
			tam = len(amarela)
			#print("ENTREI")
			for i in range(0,tam):
				aux = fun_heuristica(grafo, azul, amarela, vermelha, verde, amarela[i], destino)
				#print(aux.nome, 'e', aux.distancia, 'na lista amarela')
				if(aux != atual):
					aux2 = ret_mesmovalor(aux)
					lista_de_prioridades.put(aux2)
		if(esta_nalista(atual,vermelha)):#Se atual estiver na lista carrega na PriorityQueue todas as dist de cada um pro destino
			vermelha.remove(atual)
			tam = len(vermelha)
			for i in range(0,tam):
				aux = fun_heuristica(grafo, azul, amarela, vermelha, verde, vermelha[i], destino)
				if(aux != atual):
					aux2 = ret_mesmovalor(aux)
					lista_de_prioridades.put(aux2)
		if(esta_nalista(atual,verde)):#Se atual estiver na lista carrega na PriorityQueue todas as dist de cada um pro destino
			verde.remove(atual)
			tam = len(verde)
			for i in range(0,tam):
				aux = fun_heuristica(grafo, azul, amarela, vermelha, verde, verde[i], destino)
				if(aux != atual):
					aux2 = ret_mesmovalor(aux)
					lista_de_prioridades.put(aux2)
		
		print(atual.nome)
		atual = lista_de_prioridades.get(0) #Depois de preenchida a lista, retira o de menor valor
		#print(atual.nome)
		#break
		aux2 = ret_mesmovalor(atual)
		lista.append(aux2) #Adiciona este de menor valor na lista de caminho e então faz novamente todo o percurso

	tam = len(lista)
	print('O trajeto mais rápido de: ',lista[0].nome, 'até', lista[tam-1].nome, ' é: ')
	for x in range(0,tam):
		if(x+1 < tam):
			if(lista[x] != lista[x+1]):
				if(x == tam-1):
					print(lista[x].nome,'.')
				else:
					print(lista[x].nome,'->')
		else:
			print(lista[x].nome,'.')



grafo = [[0,11,20,27,40,43,39,28,18,10,18,30,30,32],
		 [11,0,9,16,29,32,28,19,11,4,17,23,21,24],
		 [20,9,0,7,20,22,19,15,10,11,21,21,13,18],
		 [27,16,7,0,13,16,12,13,13,18,26,21,11,17],
		 [40,29,20,13,0,3,2,21,25,31,38,27,16,20],
		 [43,32,22,16,3,0,4,23,28,33,41,30,17,20],
		 [39,28,19,12,2,4,0,22,25,29,38,28,13,17],
		 [28,19,15,13,21,23,22,0,9,22,18,7,25,30],
		 [18,11,10,13,25,28,25,9,0,13,12,12,23,28],
		 [10,4,11,18,31,33,29,22,13,0,20,27,20,23],
		 [18,17,21,26,38,41,28,18,12,20,0,15,35,39],
		 [30,23,21,21,27,30,28,7,12,27,15,0,31,37],
		 [30,21,13,11,16,17,13,25,23,20,35,31,0,5],
		 [32,24,18,17,20,20,17,30,28,23,39,37,5,0]]

lista_de_prioridades = PriorityQueue()

E1 = Estacao('E1',1)
E2 = Estacao('E2',2)
E3 = Estacao('E3',3)
E4 = Estacao('E4',4)
E5 = Estacao('E5',5)
E6 = Estacao('E6',6)
E7 = Estacao('E7',7)
E8 = Estacao('E8',8)
E9 = Estacao('E9',9)
E10 = Estacao('E10',10)
E11 = Estacao('E11',11)
E12 = Estacao('E12',12)
E13 = Estacao('E13',13)
E14 = Estacao('E14',14)

vermelha = [E11,E9,E3,E13]
verde = [E12,E8,E4,E13,E14]
amarela = [E10,E2,E9,E8,E5,E7]
azul = [E1,E2,E3,E4,E5,E6]

todos = [E1,E2,E3,E4,E5,E6,E7,E8,E9,E10,E11,E12,E13,E14]

contagem = 0

for x in range(0,len(todos)):
	for y in range(0,len(todos)):
		aux_azul = ret_mesmovalor(azul)
		aux_amarela = ret_mesmovalor(amarela)
		aux_vermelha = ret_mesmovalor(vermelha)
		aux_verde = ret_mesmovalor(verde)
		search_A(grafo, aux_azul, aux_amarela, aux_vermelha, aux_verde, todos[x], todos[y])
		contagem = contagem + 1

print('Foram efetuados ', contagem, ' cálculos de distância.')

#search_A(grafo, azul, amarela, vermelha, verde, E1, E3)


'''E1.set_Distancia(5)
E2.set_Distancia(10)
E3.set_Distancia(15)

lista_de_prioridades.put(E2)
lista_de_prioridades.put(E3)
lista_de_prioridades.put(E1)

while not lista_de_prioridades.empty():
	aux = lista_de_prioridades.get(0)
	print('Nome: ',aux.nome,'Valor: ', aux.distancia)'''