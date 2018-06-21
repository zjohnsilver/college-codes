####
#### Lancelot - 03/12/2017
####


from No import No
from random import randint

class ArvoreBinaria(object):
	def __init__(self, root = None):
		self.root = root

	### Inserindo um No na Arvore
	def inserirNo(self, value):
		if self.root is None:
			self.root = No(value)
		else:
			self.inserirNo2(self.root, value)


	def inserirNo2(self, noBase, value):
		if (value > noBase.value):
			if noBase.right is None:
				noBase.right = No(value, noBase)
			else:
				self.inserirNo2(noBase.right, value)
		else:
			if noBase.left is None:
				noBase.left = No(value, noBase)
			else:
				self.inserirNo2(noBase.left, value)

	### Metodos de impressao da arvore
	def preFixado(self, noBase):
		if (noBase):
			print(noBase.value, end = " ")
			self.preFixado(noBase.left)
			self.preFixado(noBase.right)
	def posFixado(self, noBase):
		if (noBase):
			self.posFixado(noBase.left)
			self.posFixado(noBase.right)
			print(noBase.value, end = " ")
	def inFixado(self, noBase):
		if (noBase):
			self.inFixado(noBase.left)
			print(noBase.value, end = " ")
			self.inFixado(noBase.right)


tree  = ArvoreBinaria()

#Adiciona elementos a arvore
for x in range(20):
	tree.inserirNo(randint(10,100))

tree.preFixado(tree.root)




