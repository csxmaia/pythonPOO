from classes.Fisica import Fisica
from classes.Pessoa import Pessoa
from classes.Carro import Carro
from persistencia import save, read

def main():
  # pessoa = Pessoa()
  # pessoa.setNome("Cristhian")
  # pessoa.setIdade("19")
  # pessoa.setTelefone("997516796")
  # nome = pessoa.getNome()
  # idade= pessoa.getIdade()
  # telefone= pessoa.getTelefone()

  # print(nome)
  # print(idade)
  # print(telefone)

  fisica = Fisica()
  
  fisica.setNome("gta")
  fisica.setIdade("19")
  fisica.setTelefone("997516796")
  fisica.setCpf(44444444444)

  carro = Carro()
  carro.setNome("Nome 01")
  carro.setCor("Vermelho")
  fisica.setCarro(carro)

  print(vars(fisica))
  print(fisica.getCpf())
  print(fisica.getNome())
  print(fisica.getIdade())
  print(fisica.getTelefone())
  print(fisica.getCarro())
  print(fisica.getCarro().getNome())
  print(fisica.getCarro().getCor())
  
  # after_data = None
  # try:
  #   after_data = read()
  # except FileNotFoundError:
  #   pass

  # data = "{}&&{}$${}$${}$${}$${}".format(after_data, fisica.getCpf(), fisica.getNome(), fisica.getIdade(), fisica.getTelefone(), fisica.getCarro())
  # save(vars(fisica))


  # file_r = open("data.txt", "r")
  # content = file_r.read()
  # content = content.split("&&")
  # for i in content:
  #   print(i.split("$$"))



main()