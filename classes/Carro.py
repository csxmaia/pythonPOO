class Carro(object):
  def __init__(self, nome=None, cor=None):
    self._nome = nome
    self._cor = cor

  def setNome(self, nome):
    self._nome = nome

  def getNome(self):
    return self._nome

  def setCor(self, cor):
    self._cor = cor

  def getCor(self):
    return self._cor

