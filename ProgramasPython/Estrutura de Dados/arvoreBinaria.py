class BSTNode(object):
	def __init__ (self, key, value = None, left = None, right = None):
		## Informacoes da raiz
		self.key = key
		self.value = key
		self.left = left
		self.right = right

	def inserir (self, node):
		if (node.value < self.value):
			if self.left == None:
				self.left = node
			else:
				self.left.inserir(node)

		else:
			if self.right == None:
				self.right = node
			else:
				self.right.inserir(node)




arvoreBinaria = BSTNode(30)
 
arvoreBinaria.inserir(20)

print arvoreBinaria.left.value
