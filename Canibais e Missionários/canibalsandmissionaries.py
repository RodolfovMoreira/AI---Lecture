#Gerar estados
#Validar estados
#Não gerar estados repetidos

#--------------------------------------
#  Abordagem será um array de 3 posições no qual [Missionários,Canibais,Barco]
#  As funções para testar possibilidades serão 3 ADD's e 3 SUB's nos quais Adicionam/Subtraem da quantidade de membros
#  O estado gerado será avaliado da seguite forma  (Missionários < Canibais) -> Negado
#  Caso passe da função de avaliação checaremos com auxílio de uma função repetições se o estado já foi gerado
#  Adicionamos o novo estado na lista de borda
#
#  Estado inicial: 331
#  Estado final: [0,0,0]
#--------------------------------------


final_state = [0,0,0] #Estado final
initial_state = [3,3,1] #Estado inicial
already_chkd = [[0] for x in range(0,332)] #Array para checar se o estado já apareceu, se sim 1, se não 0
edge = [] #Nossa borda de estados a serem checados ficará aqui
	
def add_Boat(array):
	array[2] = array[2] + 1

def sub_Boat(array):
	array[2] = array[2] - 1

def is_valid(array): #Retorna 1 se for válido e 0 se não for
	if(array[0] == 1):
		if(array[1] == 0):
			return 0
		elif(array[1] == 2):
			return 0
		elif(array[1] == 3):
			return 0
	elif(array[0] == 2):
		if(array[1] == 0):
			return 0
		elif(array[1] == 1):
			return 0
		elif(array[1] == 3):
			return 0
	else:
		return 1

def transform_number(array): #transforma o array para número
	cent = array[0]*100
	dez = array[1]*10
	unit = array[2]

	return cent+dez+unit

def set_state(already_chkd, array): #Setar no array de repetições que a respectiva repetição já foi checada
	index = transform_number(array)
	already_chkd[index] = 1

def check_state(already_chkd, array): #Função para checar se o estado já apareceu, se sim 1, se não 0
	index = transform_number(array)
	if(already_chkd[index] == 1):
		return 1
	else:
		return 0

def m_dead(array): #Retorna 1 caso o número de canibais seja maior que o número de missionários
	if(array[0] < array[1]):
		return 1
	else:
		return 0 

def wrong_array(array): #Retorna 1 se estado estiver fora do escopo do problema
	if(array[0] > 3):
		return 1
	elif(array[1] > 3):
		return 1
	elif(array[0] < 0):
		return 1
	elif(array[1] < 0):
		return 1
	else:
		return 0

def copy(array):
	aux = [0,0,0]
	for i in range(0,3):
		aux[i] = array[i]

	return aux

#Existem 10 casos possíveis para alteração dos números, os mesmos seguem abaixo:

def Caso_1(array):#Retorna o array caso seja possível, senão retorna array 0
	aux = copy(array)
	aux[0] = aux[0] - 1
	sub_Boat(aux)
	if(m_dead(aux)):
		return 0
	elif(wrong_array(aux)):
		return 0
	else:
		return aux

def Caso_2(array):#Retorna o array caso seja possível, senão retorna array 0
	aux = copy(array)
	aux[0] = aux[0] - 2
	sub_Boat(aux)
	if(m_dead(aux)):
		return 0
	elif(wrong_array(aux)):
		return 0
	else:
		return aux

def Caso_3(array):#Retorna o array caso seja possível, senão retorna array 0
	aux = copy(array)
	aux[0] = aux[0] - 1
	aux[1] = aux[1] - 1
	sub_Boat(aux)
	if(m_dead(aux)):
		return 0
	elif(wrong_array(aux)):
		return 0
	else:
		return aux

def Caso_4(array):#Retorna o array caso seja possível, senão retorna array 0
	aux = copy(array)
	aux[1] = aux[1] - 1
	sub_Boat(aux)
	if(m_dead(aux)):
		return 0
	elif(wrong_array(aux)):
		return 0
	else:
		return aux

def Caso_5(array):#Retorna o array caso seja possível, senão retorna array 0
	aux = copy(array)
	aux[1] = aux[1] - 2
	sub_Boat(aux)
	if(m_dead(aux)):
		return 0
	elif(wrong_array(aux)):
		return 0
	else:
		return aux

def Caso_6(array):#Retorna o array caso seja possível, senão retorna array 0
	aux = copy(array)
	aux[0] = aux[0] + 1
	add_Boat(aux)
	if(m_dead(aux)):
		return 0
	elif(wrong_array(aux)):
		return 0
	else:
		return aux

def Caso_7(array):#Retorna o array caso seja possível, senão retorna array 0
	aux = copy(array)
	aux[0] = aux[0] + 2
	add_Boat(aux)
	if(m_dead(aux)):
		return 0
	elif(wrong_array(aux)):
		return 0
	else:
		return aux

def Caso_8(array):#Retorna o array caso seja possível, senão retorna array 0
	aux = copy(array)
	aux[0] = aux[0] + 1
	aux[1] = aux[1] + 1
	add_Boat(aux)
	if(m_dead(aux)):
		return 0
	elif(wrong_array(aux)):
		return 0
	else:
		return aux

def Caso_9(array):#Retorna o array caso seja possível, senão retorna array 0
	aux = copy(array)
	aux[1] = aux[1] + 1
	add_Boat(aux)
	if(m_dead(aux)):
		return 0
	elif(wrong_array(aux)):
		return 0
	else:
		return aux

def Caso_10(array):#Retorna o array caso seja possível, senão retorna array 0
	aux = copy(array)
	aux[1] = aux[1] + 2
	add_Boat(aux)
	if(m_dead(aux)):
		return 0
	elif(wrong_array(aux)):
		return 0
	else:
		return aux

def confere(array):
	final = [0,0,0]

	if(array == final):
		print("TODOS ATRAVESSARAM SÃO E SALVOS! OS MISSIONÁRIOS VIVOS E OS CANIBAIS COM FOME!")
		return 1
	return 0

array = 0
array_aux = 0
check = 0
edge.append(initial_state)

while(array != final_state):
	#print('Edge é:',edge)
	array = edge.pop(0)

	if(array[2] == 1): #Se o barco estiver na esquerda
		array_aux = Caso_1(array)
		if(array_aux != 0):
			if(confere(array_aux)):
				break
			check = check_state(already_chkd, array_aux)
			if(check == 0):
				set_state(already_chkd, array_aux)
				edge.append(array_aux)
				print(edge)	

		array_aux = Caso_2(array)
		if(array_aux != 0):
			if(confere(array_aux)):
				break
			check = check_state(already_chkd, array_aux)
			if(check == 0):
				set_state(already_chkd, array_aux)
				edge.append(array_aux)
				print(edge)

		array_aux = Caso_3(array)
		if(array_aux != 0):
			if(confere(array_aux)):
				break
			#print('entrou')
			check = check_state(already_chkd, array_aux)
			if(check == 0):
				set_state(already_chkd, array_aux)
				edge.append(array_aux)
				print(edge)

		array_aux = Caso_4(array)
		if(array_aux != 0):
			if(confere(array_aux)):
				break
			check = check_state(already_chkd, array_aux)
			if(check == 0):
				set_state(already_chkd, array_aux)
				edge.append(array_aux)
				print(edge)

		array_aux = Caso_5(array)
		if(array_aux != 0):
			if(confere(array_aux)):
				break
			check = check_state(already_chkd, array_aux)
			if(check == 0):
				set_state(already_chkd, array_aux)
				edge.append(array_aux)
				print(edge)

	else: #Se o barco estiver na direita

		array_aux = Caso_6(array)
		if(array_aux != 0):
			if(confere(array_aux)):
				break
			check = check_state(already_chkd, array_aux)
			if(check == 0):
				set_state(already_chkd, array_aux)
				edge.append(array_aux)
				print(edge)

		array_aux = Caso_7(array)
		if(array_aux != 0):
			if(confere(array_aux)):
				break
			check = check_state(already_chkd, array_aux)
			if(check == 0):
				set_state(already_chkd, array_aux)
				edge.append(array_aux)
				print(edge)

		array_aux = Caso_8(array)
		if(array_aux != 0):
			if(confere(array_aux)):
				break
			check = check_state(already_chkd, array_aux)
			if(check == 0):
				set_state(already_chkd, array_aux)
				edge.append(array_aux)
				print(edge)

		array_aux = Caso_9(array)
		if(array_aux != 0):
			if(confere(array_aux)):
				break
			check = check_state(already_chkd, array_aux)
			if(check == 0):
				set_state(already_chkd, array_aux)
				edge.append(array_aux)
				print(edge)

		array_aux = Caso_10(array)
		if(array_aux != 0):
			if(confere(array_aux)):
				break
			check = check_state(already_chkd, array_aux)
			if(check == 0):
				set_state(already_chkd, array_aux)
				edge.append(array_aux)
				print(edge)



print("Fim! :)")