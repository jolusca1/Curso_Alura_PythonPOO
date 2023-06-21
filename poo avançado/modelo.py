
class Filme:
    
    def __init__(self, nome, ano, duracao):
        self.nome = nome 
        self. ano = ano
        self.duracao = duracao

class Serie:
    
    def __init__(self, nome, ano, temporadas):
        self.nome = nome 
        self. ano = ano
        self.temporadas = temporadas
        
        
vingadores = Filme("Vingadores - Guerra Infinita", 2018, 160)
print(vingadores.nome)

atlanta = Serie("Atlanta", 2017, 2)
print(f'''  
      Nome: {atlanta.nome}, 
      Ano: {atlanta.ano}, 
      Temporadas: {atlanta.temporadas}
      ''')