class acontecimento:

   def __init__(self, nome, quantidade=0):
        self.nome = nome
        self.quantidade = quantidade

   def set_nome(self, new_nome):
       self.nome = new_nome

   def set_quantidade(self, new_quantidade):
         self.quantidade = new_quantidade
   
   def incrementar(self, step=1):
      self.quantidade += int(step)
   
   def decrementar(self, step=1):
      if self.quantidade - step >= 0:
         self.quantidade -= step
      else:
         print(f"Cannot decrementar {self.nome} abaixo de 0")

   def __str__(self):
      return f"{self.nome}: {self.quantidade}"