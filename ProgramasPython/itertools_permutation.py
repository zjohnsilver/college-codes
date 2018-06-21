from itertools import *

pessoas = ('Joao', 'Bia', 'Jessica')

print (list(product(list(permutations(pessoas)), count())))
