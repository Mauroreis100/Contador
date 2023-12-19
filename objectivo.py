class objectivo:

   def __init__(self, nome, valor_inicial=0, valor_final=float('inf')):
        self.nome = nome
        self.valor_actual = valor_inicial
        self.valor_inicial = valor_inicial
        self.valor_final = valor_final


   def incrementar(self, step=1):
      if self.valor_actual + step <= self.valor_final:
         self.valor_actual += step
      else:
         print(f"{self.nome}/{self.valor_final}")

   def decrementar(self, step=1):
      if self.valor_actual - step >= 0:
         self.valor_actual -= step
      else:
         print(f"Cannot decrementar {self.nome} abaixo de {self.valor_inicial}")

   def __str__(self):
      return f"{self.nome}: {self.valor_actual}/{self.valor_final}\n"