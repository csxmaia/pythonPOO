from classes.Carro import Carro

class Pessoa(object):
  def __init__(self, nome=None, idade=None, telefone=None, carro=None):
    self.__nome = nome
    self.__idade = idade
    self.__telefone = telefone
    self.__carro = carro

  def setNome(self, nome):
    self.__nome = nome

  def getNome(self):
    return self.__nome

  def setIdade(self, idade):
    self.__idade = idade

  def getIdade(self):
    return self.__idade

  def setTelefone(self, telefone):
    self.__telefone = telefone

  def getTelefone(self):
    return self.__telefone

  def setCarro(self, carro):
    self.__carro = carro

  def getCarro(self):
    return self.__carro

  def get_info(self):
    return "Pessoa class {}".format(self.__nome)