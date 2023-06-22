from abc import ABC # abstract base classes
from collections.abc import MutableSequence, Sized
from numbers import Complex

class MinhaListagem(Sized):
    def __init__(self, descricao):
        self.descricao = descricao
        
    def __str__(self):
        return self.descricao
    
lista = MinhaListagem('Nova_lista')
print(lista)

#class Numero(Complex):
 #   def __getitem__(self, item):
  #      super().__getitem__()
        
#filmes = Numero()