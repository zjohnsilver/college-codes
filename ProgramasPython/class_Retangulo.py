class Retangulo:
	def __init__(self):
		self.Base = 1
		self.Altura = 1
		print("Construtor chamado com sucesso!")
	
	def returnvalor(self):
		return self.Base, self.Altura
	
	def change_Lados(self, base, altura):
		self.Base = base
		self.Altura = altura
	
	def area(self):
		return	self.Base*self.Altura
	
	def perimetro(self):
		return self.Base*2 + self.Altura*2
		


print ("Informe as medidas: \n")
largura = float(input("Qual a Largura do local?\n"))
comprimento = float(input("Qual o Comprimento do local?\n"))

piso = Retangulo()

# Tamanho do PISO( Ceramica, azuleijo, etc.. )
print("Valores das medidas do Piso:\n")
larg_Piso = float(input("Largura do Piso: "))
comp_Piso = float(input("Comprimento do Piso: "))

piso.change_Lados(comp_Piso,larg_Piso)

areaLocal = largura*comprimento
qtd_Pisos = round(areaLocal/piso.area())

print("Quantidade necessária: %i pisos."%(qtd_Pisos))	


	