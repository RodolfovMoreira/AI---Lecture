#Estado inicial = posições do tabuleiro + quem é a vez
#Estado final = posições em que o jogo acaba
#Operadores = Jogadas legais
#Função Utilidade = Valor numérico do resultado (pontuação)

#O conceito de MINIMAX é maximizar o ganho supondo que o adversário vai tertar minimizá-lo
# MAX = Agente / MIN = Adversário



#---------------------------------------------------------------------------------------
#1 - Teremos uma classe JogodaVelha, na qual todas as funções jogáveis estarão contidas
#2 - Nossa função MINIMAX retornará a melhor jogada
#Nossa representação do tabuleiro será um array de 9 posições no qual será:
#Tabuleiro = [0,1,2,
#             3,4,5,
#             6,7,8]
#
#
#---------------------------------------------------------------------------------------

class JogodaVelha:
	def __init__(self):
		self.posicoes = {}
		self.combos = ([0,1,2],
					   [3,4,5],
					   [6,7,8],
					   [0,3,6],
					   [1,4,7],
					   [2,5,8],
					   [0,4,8],
					   [2,4,6])

	def criar_Tabuleiro(self): #Cria o tabuleiro com '.' em todos os lugares
		for i in range(0,9):
			self.posicoes[i] = "."
		#print(self.posicoes)

	def mostrar_Tabuleiro(self): #Printa o tabuleiro na tela
		print(self.posicoes[0],self.posicoes[1],self.posicoes[2])
		print(self.posicoes[3],self.posicoes[4],self.posicoes[5])
		print(self.posicoes[6],self.posicoes[7],self.posicoes[8])

	def retorna_JogadasPossiveis(self): #Retorna lista com os índices das possíveis jogadas
		self.jogadaspossiveis = []
		for i in range(0,9):
			if self.posicoes[i] == ".":
				self.jogadaspossiveis.append(i)
		return self.jogadaspossiveis

	def fazer_Jogada(self, posicao, jogador): #Faz jogada em 'posicao', pelo 'jogador'
		if(self.posicoes[posicao] == 'x' or self.posicoes[posicao] == 'o'):
			print("Nesta posição já existe uma jogada, escolha outra: ")
		else:
			self.posicoes[posicao] = jogador
			self.mostrar_Tabuleiro()

	def pegar_Vencedor(self):
		for jogador in ("x","o"):
			for combo in self.combos:
				if self.posicoes[combo[0]] == jogador and self.posicoes[combos[1]] == jogador and self.posicoes[combos[2]] == jogador:
					return jogador
			if "." not in self.posicoes.values():
				return "empate"
			return None

	def jogo_Completo(self): #Verdadeiro caso o jogo tenha terminado, falso o contrário
		if "." not in self.posicoes.values(): 
			return True
		if self.pegar_Vencedor() != None:
			return True
		return False

	def trocar_Jogador(self, jogador):
		if jogador = "x"
			return "o"
		return "x"

	def MINIMAX(self, jogador, profundidade = 0):
		pass




a = JogodaVelha()
a.criar_Tabuleiro()
a.mostrar_Tabuleiro()