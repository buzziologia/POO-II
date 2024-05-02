clientes = [
  {
    'nome': 'Alice',
    'cpf': '12345678900',
    'bairro': 'santa Monica',
    'rua': 'felix kleis',
    'numero' : '123',
    'telefone': '999999999',
    'email': 'alice@example.com'
  }
]


funcionarios = [
  {
    'nome': 'Bob',
    'cpf': '98765432100',
    'cargo': 'Atendente',
    'salario': 1500.00,
    'telefone': '888888888',
    'email': 'bob@example.com',
    'senha': 'senha123'
  }
]


sabores = [
  {
    'nome': 'Calabresa',
    'preco': 25.00
  }
]


tamanhos = [
  {
    'tipo': 'Pequena',
    'multiplicador': 1
  }
  {
    'tipo': 'Média',
    'multiplicador': 1.2
  }
  {
    'tipo': 'Grande',
    'multiplicador': 1.5
  }
]

adicionais = [
  {
    'nome': 'Borda Recheada',
    'preco': 5.00
  }
]


pedidos = [
  {
    'cliente': 'Alice',
    'info_tamanhos': 'Pequena',
    'info_sabor': 'Calabresa',
    'info_adicionais': 'Borda Recheada'
  }
]


deliverys = [
  {
    'pedido': 'Pedido 1',
    'funcionario': 'Bob',
    'status': 'Pendente'
  }
]


class Pizzaria():
  def __init__(self):
    self.clientes = []
    self.funcionarios = []
    self.sabores = []
    self.tamanhos = []
    self.adicionais = []
    self.pedidos = []
    self.deliverys = []
    self.ganhos = []

  def menu_pizzaria(self):
    opcao = 0
    while True:
        try:
            print()
            print("-------------------------Menu Pizzaria-------------------------")
            print("por favor selecione uma das opções abaixo:")
            print("1 - Visualizar saldo da pizzaria")
            print("2 - Visualizar Armazem")
            print("3 - Voltar ao Menu Principal")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                self.saldo_pizzaria()
            elif opcao == 2:
                self.visualizar_armazem()
            elif opcao == 3:
                break
        except ValueError:
            print("Opção inválida. Por favor, digite um número válido.")

  def saldo_pizzaria(self):
    saldos = [
      {'dia': '01/05/2024', 'saldo_diario': 1200},
      # Adicione os saldos de cada dia aqui
    ]
    print()
    print("-------------------------Saldo da Pizzaria-------------------------")
    print("Saldo da Pizzaria: R$", self.saldo)
    print()

  def visualizar_armazem(self):
    print()
    print("-------------------------Armazem da Pizzaria-------------------------")
    print("Sabores: ", self.sabores)
    print("Tamanhos: ", self.tamanhos)
    print("Adicionais: ", self.adicionais)
    print()


class Pizza:
  def __init__(self, nome, preco, sabores):
    self.nome = nome
    self.preco = preco
    self.sabores = []

  def menu_pizza(self):
    opcao = 0
    while True:
        try:
            print()
            print("-------------------------Menu Pizzas-------------------------")
            print("Por favor selecione uma das opções abaixo: ")
            print("1 - Cadastrar pizza")
            print("2 - Remover pizza")
            print("3 - Visualizar pizzas cadastradas")
            print("4 - Voltar ao Menu Principal")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
              pizza = self.cadastrar_pizza()
              self.sabores.append(pizza)
            elif opcao == 2:
              self.remover_pizza()
            elif opcao == 3:
              self.visualizar_pizza()
            elif opcao == 4:
              break    
            else:
              print("Opção inválida. Por favor, digite um número válido.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número válido.")

  def cadastrar_pizza(self):
    nome = input("Digite o sabor da pizza: ")
    preco = float(input("Digite o preço da pizza: "))

    nova_pizza = {
      'nome': nome,
      'preco': preco,
    }

    self.sabores.append(nova_pizza)
    print(f"Pizza de {nome} cadastrada com sucesso!")

  def remover_pizza(self):
    nome = input("Digite o nome da pizza a ser removida: ")
    for pizza in self.sabores:
      if pizza['nome'] == nome:
        self.sabores.remove(pizza)
        print(f"Pizza de {nome} removida com sucesso!")
        return
    print(f"Pizza de {nome} não encontrada.")

  def visualizar_pizza(self):
    print("Pizzas cadastradas:")
    for pizza in self.sabores:
      print(f"Sabor: {pizza['nome']}, Preço: R${pizza['preco']:.2f}") 



class Funcionario:
  def __init__(self, nome, cpf, cargo, salario, telefone, email, senha):
    self.nome = nome
    self.cpf = cpf
    self.cargo = cargo
    self.salario = salario
    self.telefone = telefone
    self.email = email
    self.senha = senha
    self.funcionarios = []

  def menu_funcionario(self):
    opcao = 0
    while True:
      try:
        print()
        print("-------------------------Menu Funcionarios-------------------------")
        print("Por favor selecione uma das opções abaixo: ")
        print("1 - Cadastrar funcionário")
        print("2 - Remover funcionário")
        print("3 - Visualizar funcionários cadastrados")
        print("4 - Voltar ao Menu Principal")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
          funcionario = self.cadastrar_funcionario()
          self.funcionarios.append(funcionario)
        elif opcao == 2:
          self.remover_funcionario()
        elif opcao == 3:
          self.visualizar_funcionario()
        elif opcao == 4:
          break
        else:
          print("Opção inválida. Por favor, digite um número entre 1 e 4.")
      except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

  def cadastrar_funcionario(self):
    nome = input("Digite o nome do funcionário: ")
    cpf = input("Digite o CPF do funcionário: ")
    cargo = input("Digite o cargo do funcionário: ")
    salario = float(input("Digite o salário do funcionário: "))
    telefone = input("Digite o telefone do funcionário: ")
    email = input("Digite o email do funcionário: ")
    senha = input("Digite a senha do funcionário: ")

    novo_funcionario = {
      'nome': nome,
      'cpf': cpf,
      'cargo': cargo,
      'salario': salario,
      'telefone': telefone,
      'email': email,
      'senha': senha
    }

    print(f"Funcionário {nome} cadastrado com sucesso!")
    return novo_funcionario

  def remover_funcionario(self):
    cpf = input("Digite o CPF do funcionário a ser removido: ")
    for funcionario in self.funcionarios:
      if funcionario['cpf'] == cpf:
        self.funcionarios.remove(funcionario)
        print(f"Funcionário com CPF {cpf} removido com sucesso!")
        return
    print(f"Funcionário com CPF {cpf} não encontrado.")

  def visualizar_funcionario(self):
    print("Funcionários Cadastrados")
    for funcionario in self.funcionarios:
      print()
      print(f"----------------- Dados de {funcionario['nome']} -----------------")
      print(f"Nome: {funcionario['nome']}")
      print(f"CPF: {funcionario['cpf']}")
      print(f"Cargo: {funcionario['cargo']}")
      print(f"Salário: R${funcionario['salario']:.2f}")
      print(f"Telefone: {funcionario['telefone']}")
      print(f"Email: {funcionario['email']}")
      print()


class Cliente:
  def __init__(self, nome, cpf, bairro, rua, numero, telefone, email):
    self.nome = nome
    self.cpf = cpf
    self.bairro = bairro
    self.rua = rua
    self.numero = numero
    self.telefone = telefone
    self.email = email
    self.clientes = []

  def menu_cliente(self):
    opcao = 0
    while True:
        try:
            print()
            print("-------------------------Menu Clientes-------------------------")
            print("Por favor selecione uma das opções abaixo: ")
            print("1 - Cadastrar cliente")
            print("2 - Remover cliente")
            print("3 - Visualizar clientes cadastrados")
            print("4 - Voltar ao Menu Principal")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
              cliente = self.cadastrar_cliente()
              self.clientes.append(cliente)
            elif opcao == 2:
              self.remover_clientes()
            elif opcao == 3:
              self.visualizar_clientes()
            elif opcao == 4:
              break
            else:
              print("Opção inválida. Por favor, digite um número entre 1 e 4.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

  def cadastrar_cliente(self):
    print()
    print("-------------------------Cadastro de Cliente-------------------------")
    nome = input("Digite o nome do cliente: ")

    cpf_existe = False  # Defina cpf_existe como False antes do loop

    while True:
        cpf = input("Digite o CPF do cliente (apenas números): ")
        if len(cpf) == 11 and cpf.isdigit():
            for cliente in self.clientes:
                if cliente['cpf'] == cpf:
                    cpf_existe = True
                    print("CPF já cadastrado. Por favor, digite um CPF válido.")
                    break  
            if not cpf_existe:
                break 
        else:
            print("CPF inválido. Por favor, digite um CPF válido (11 dígitos)")

    bairro = input("Digite o bairro do cliente: ")
    rua = input("Digite a rua do cliente: ")
    numero = int(input("Digite o número da casa do cliente: "))
    telefone = input("Digite o telefone do cliente: ")
    email = input("Digite o email do cliente: ")

    novo_cliente = {
        'nome': nome,
        'cpf': cpf,
        'bairro': bairro,
        'rua': rua,
        'numero': numero,
        'telefone': telefone,
        'email': email,
    }

    self.clientes.append(novo_cliente)
    print(f"Cliente {nome} cadastrado com sucesso!")

  def remover_clientes(self):
    cpf = input("Digite o CPF do cliente a ser removido: ")
    for cliente in self.clientes:
      if cliente['cpf'] == cpf:
        self.clientes.remove(cliente)
        print(f"Cliente com CPF {cpf} removido com sucesso!")
        return
    print(f"Cliente com CPF {cpf} não encontrado.")

  def visualizar_clientes(self):
    print("Clientes Cadastrados")
    for cliente in self.clientes:
      print()
      print(f"----------------- Dados de {cliente['nome']} -----------------")
      print(f"Nome: {cliente['nome']}")
      print(f"CPF: {cliente['cpf']}")
      print(f"Bairro: {cliente['bairro']}")
      print(f"Rua: {cliente['rua']}")
      print(f"Número: {cliente['numero']}")
      print(f"Telefone: {cliente['telefone']}")
      print(f"Email: {cliente['email']}")
      print()


class Pedido:
  def __init__(self):
    self.clientes = []
    self.sabores = []
    self.pedidos = []

  def menu_pedido(self):
    opcao = 0
    while True:
        try:
            print()
            print("-------------------------Menu Pedidos-------------------------")
            print("Por favor selecione uma das opções abaixo: ")
            print("1 - Cadastrar pedido")
            print("2 - Visualizar pedidos")
            print("3 - Voltar ao Menu Principal")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
              pedido = self.cadastrar_pedido()
              self.pedidos.append(pedido)
            elif opcao == 2:
              self.visualizar_pedido()
            elif opcao == 3:
              self.menu_pedido()
            else:
              print("Opção inválida. Por favor, digite um número entre 1 e 3.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")

  def cadastrar_pedido(self):
    print()
    print("-------------------------Cadastro de Pedido-------------------------")
    cpf = input("Digite o CPF do cliente (apenas números): ")
    if len(cpf) == 11 and cpf.isdigit():
        for cliente in self.clientes:
            if cliente['cpf'] == cpf:
                break  
        else:
            print("CPF não encontrado.")
            print("Por favor, cadastre o cliente antes de fazer o pedido.")
            return
    else:
        print("CPF inválido. Por favor, digite um CPF válido (11 dígitos)")
        return

    info_tamanhos = input("Digite o tamanho da pizza (pequena, média ou grande): ")
    info_sabor = input("Digite o sabor da pizza: ")
    info_adicionais = input("Digite os adicionais da pizza (se houver): ")

    novo_pedido = {
        'cliente': cliente,
        'info_tamanhos': info_tamanhos,
        'info_sabor': info_sabor,
        'info_adicionais': info_adicionais,
    }
    self.pedidos.append(novo_pedido)
    print(f"Pedido de {cliente} feito com sucesso!")

  def visualizar_pedido(self):
    print("Pedidos Cadastrados")
    for pedido in self.pedidos:
      print()
      print(f"----------------- Dados de {pedido['cliente']} -----------------")
      print(f"Nome: {pedido['cliente']['nome']}")
      print(f"CPF: {pedido['cliente']['cpf']}")
      print(f"Tamanho: {pedido['info_tamanhos']}")
      print(f"Sabor: {pedido['info_sabor']}")
      print(f"Adicionais: {pedido['info_adicionais']}")
      print()


class Delivery:
  def __init__(self, pedido, funcionario, status, deliverys):
    self.pedido = pedido
    self.funcioanrio = funcionario
    self.status = status
    self.deliverys = []

  def menu_delivery(self):
    opcao = 0
    while True:
      try:
        print()
        print("-------------------------Menu Delivery-------------------------")
        print("Por favor selecione uma das opções abaixo: ")
        print("1 - Visualizar deliverys")
        print("2 - Finalizar delivery")
        print("3 - Voltar ao Menu Delivery")
        opcao = int(input("Digite a opção desejada: "))
        if opcao == 1:
          self.visualizar_delivery()
        elif opcao == 2:
          self.finalizar_delivery()
        elif opcao == 3:
          self.menu_delivery()
        else:
          print("Opção inválida. Por favor, digite um número entre 1 e 3.")
      except ValueError:
        print("Entrada inválida. Por favor, digite um número.")

  def visualizar_delivery(self):
    print("Deliverys Cadastrados")
    for delivery in self.deliverys:
      print()
      print(f"----------------- Dados de {delivery['pedido']} -----------------")
      print(f"Nome: {delivery['pedido']['cliente']['nome']}")
      print(f"CPF: {delivery['pedido']['cliente']['cpf']}")
      print(f"Tamanho: {delivery['pedido']['info_tamanhos']}")
      print(f"Sabor: {delivery['pedido']['info_sabor']}")
      print(f"Adicionais: {delivery['pedido']['info_adicionais']}")
      print(f"Funcionário: {delivery['funcionario']['nome']}")
      print(f"Status: {delivery['status']}")
      print()

  def finalizar_delivery(self):
    cpf = input("Digite o CPF do cliente que fez o pedido: ")
    codigo_pedido = input("Digite o código do pedido: ")
    for delivery in self.deliverys:
      if (delivery['pedido']['cliente']['cpf'] == cpf and 
      delivery['pedido']['codigo'] == codigo_pedido):
        delivery['status'] = "Finalizado"
        print(f"Delivery do pedido {codigo_pedido} finalizado com sucesso!")
        return
      else:
        print(f"Delivery do pedido {codigo_pedido} não encontrado.")
        return


#inicio do codigo em si
def main():
  while True:
    try:
      print("Bem vindo a Pizzaria")
      user = input("Insira o usuário: ")
      senha_user = input("Insira a senha: ")
      if user == "admin" and senha_user == "password":
          print("Autenticação bem-sucedida!")
          opcao = 0
          while True:
              try:
                  print()
                  print("-------------------------Menu Principal-------------------------")
                  print("Por favor selecione uma das opções abaixo: ")
                  print("1 - Pizzaria")
                  print("2 - Pizza")
                  print("3 - Cliente")
                  print("4 - Funcionário")
                  print("5 - Pedido")
                  print("6 - Delivery")
                  print("7 - Sair")
                  opcao = int(input("Digite a opção desejada: "))
                  if opcao == 1:
                    pizzaria = Pizzaria()
                    pizzaria.menu_pizzaria()
                  elif opcao == 2:
                    pizza = Pizza(None, None, sabores,)
                    pizza.menu_pizza()
                  elif opcao == 3:
                    cliente = Cliente(None, None, None, None, None, None, None)
                    cliente.menu_cliente()
                  elif opcao == 4:  
                    funcionario = Funcionario(None, None, None, None, None, None, None)
                    funcionario.menu_funcionario()
                  elif opcao == 5:
                    pedido = Pedido()
                    pedido.menu_pedido()
                  elif opcao == 6:
                    delivery = Delivery(None, None, None, None)
                    delivery.menu_delivery()
                  elif opcao == 7:
                    print("Saindo...")
                    break
              except EOFError:
                break
      else:
          print("Usuário ou senha inválidos.")
    except EOFError:
      break


if __name__ == "__main__":
  main()
