class No():
	def __init__(self, estado, pai = None, filhos = []):
		self.estado = estado
		self.pai = pai
		self.filhos = filhos
		self.profundidade = 0
