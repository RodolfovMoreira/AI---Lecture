#Função de avaliação
#Buscas por melhoras iterativas com Hill-Climbing

#-------------------------------------------------------------
#Precisamos primeiramente de uma resposta aceitável, portanto:
#Primeiro passo: Encontrar uma resposta aceitável. 
#Segundo passo: Iterativamente vamos permutar 2 em 2 cidades do resultado inicial,
#               avaliando se também é um resultado aceitável e então aplicando a função de avaliação,
#               caso a função seja menor salvamos esse estado como resposta.
#-------------------------------------------------------------

solucao_inicial = [0,1,9,2,7,3,4,8,6,5,0]

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


print(grafo)
print('O tamanho é: ', len(grafo))