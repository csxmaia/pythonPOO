from classes.Pessoa import Pessoa

class Fisica(Pessoa):
  def __init__(self,nome=None, idade=None, telefone=None, carro=None, cpf=None):
    super().__init__(nome, idade, telefone, carro)
    self.__cpf = cpf

  def setCpf(self, cpf):
    self.__cpf = cpf

  def getCpf(self):
    return self.__cpf

  def get_info(self):
    return "Fisica class {}{}".format(self.__cpf, super().getIdade())