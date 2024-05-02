class Pizzaria:
  def __init__(self, cliente, funcionario, pedido, delivery, pizza):
    self.cliente = cliente
    self.funcionario = funcionario
    self.pedido = pedido
    self.delivery = delivery
    self.pizza = pizza

  def menu(self):
    print("Bem vindo a Pizzaria")
    print("1 - Cadastrar cliente")
    print("2 - Cadastrar funcionario")
    print("3 - Cadastrar pedido")
    print("4 - Cadastrar delivery")
    print("5 - Cadastrar pizza")
    print("6 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    return opcao
  
  def cadastrar_cliente(self, nome, cpf, endereço, telefone, email):
    print("Bem vindo ao cadastro de cliente")
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o cpf do cliente: ")
    endereço = input("Digite o endereço do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    email = input("Digite o email do cliente: ")
    cliente = Cliente(nome, cpf, endereço, telefone, email)
    return cliente
    
  def atualizar_cliente(self, nome, cpf, endereço, telefone, email):
    print(f"Bem vindo a atualização cadastral de clientes")
    nome = input("Digite o nome do cliente: ")
    cpf = input("Digite o cpf do cliente: ")
    endereço = input("Digite o endereço do cliente: ")
    telefone = input("Digite o telefone do cliente: ")
    email = input("Digite o email do cliente: ")
    cliente = Cliente(nome, cpf, endereço, telefone, email)
    return cliente
  
  def cadastrar_funcionario(self,nome, cpf, cargo, salário, telefone, email):
    print("Bem vindo ao cadastro de funcionario")
    nome = input("Digite o nome do funcionario: ")
    cpf = input("Digite o cpf do funcionario: ")
    cargo = input("Digite o cargo do funcionario: ")
    salário = input("Digite o salário do funcionario: ")
    telefone = input("Digite o telefone do funcionario: ")
    email = input("Digite o email do funcionario: ")
    funcionario = Funcionario(nome, cpf, cargo, salário, telefone, email)
    return funcionario

  def cadastrar_pizza(self, pizza):
    print("Bem vindo ao cadastro de pizza")
    sabor = input("Digite o sabor da pizza: ")
    tamanho = input("Digite o tamanho da pizza: ")
    preço = input("Digite o preço da pizza: ")
    pizza = Pizza(sabor, tamanho, preço)
    return pizza
    
  def remover_pizza(self, pizza):
    print("Bem vindo ao remover pizza")
    sabor = input("Digite o sabor da pizza: ")
    tamanho = input("Digite o tamanho da pizza: ")
    preço = input("Digite o preço da pizza: ")
    pizza = Pizza(sabor, tamanho, preço)
    return pizza
  
  def cadastrar_pedido(self, cliente, pizza):
    print("Bem vindo ao cadastro de pedido")
    cliente = input("Digite o nome do cliente: ")
    pizza = input("Digite o sabor da pizza: ")
    pedido = Pedido(cliente, pizza)
    return pedido
    
  def cadastrar_delivery(self, pedido, funcionario):
    print(f"Bem vindo ao cadastro de delivery {pedido.cliente}")
    pedido = input("Digite o nome do pedido: ")
    funcionario = input("Digite o nome do funcionario: ")
    delivery = Delivery(pedido, funcionario, "pendente")
    return delivery


class Pizza:
  def __init__(self, sabor, tamanho, preço):
    self.sabor = sabor
    self.tamanho = tamanho
    self.preço = preço


class Funcionario:
  def __init__(self, nome, cpf, cargo, salario, telefone, email):
    self.nome = nome
    self.cpf = cpf
    self.cargo = cargo
    self.salario = salario
    self.telefone = telefone
    self.email = email
    
  
class Cliente:
  def __init__(self, nome, cpf, endereco, telefone, email):
    self.nome = nome
    self.cpf = cpf
    self.endereco = endereco
    self.telefone = telefone
    self.email = email


class Pedido:
  def __init__(self, cliente, pizza):
    self.cliente = cliente
    self.pizza = pizza

class Delivery:
  def __init__(self, pedido, funcionario, status):
    self.pedido = pedido
    self.funcioanrio = funcionario
    self.status = status

  def codigo_pedido(self, pedido):
   
  def status_pedido(self, pedido):
  

    

  
