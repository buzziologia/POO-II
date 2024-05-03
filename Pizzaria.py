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
    'nome': 'bob',
    'cpf': '98765432100',
    'cargo': 'atendente',
    'salario': 1500.00,
    'telefone': '888888888',
    'email': 'bob@example.com',
    'senha': 'senha123'
  },
  {  
    'nome': 'fabio',
    'cpf': '12345678912',
    'cargo': 'entregador',
    'salario': 1500.00,
    'telefone': '888888888',
    'email': 'fabio@example.com',
    'senha': 'senha123'
  },
  {
    'nome': 'sophia',
    'cpf': '44455566699',
    'cargo': 'gerente',
    'salario': 1500.00,
    'telefone': '888888888',
    'email': 'sophia@example.com',
    'senha': 'senha123'
  }
]


sabores = [
  {
    'nome': 'calabresa',
    'preco': 25.00
  }
]


tamanhos = [
  {
    'tipo': 'pequena',
   'multiplicador': 1
  },
  {
    'tipo': 'media', 
   'multiplicador': 1.2
  },
  {
    'tipo': 'grande',
   'multiplicador': 1.5
  }
]

adicionais = [
  {
    'nome': 'guarana',
    'preco': 5.00,
    'quantidade': 25
  },
  {
    'nome': 'pepsi',
    'preco': 6.00,
    'quantidade': 25
  },
  {
    'nome': 'coca',
    'preco': 7.00,
    'quantidade': 25
  }
  
]


pedidos = [
  {
    'cliente': 'Alice',
    'cpf': '12345678900',
    'info_tamanhos': 'pequena',
    'info_sabor': 'calabresa',
    'info_adicionais': 'coca',
    'quantidade_adicionais': 2
    'entregador': 'fabio'
  }
]


deliverys = [
  {
    'pedido': 'Pedido 1',
    'funcionario': 'Bob',
    'status': 'Pendente'
  }
]

saldos = [
  {
    'dia': '2023-08-01',
    'saldo': 1200.00
  }
]


class Pizzaria():
  def __init__(self):
    self.clientes = clientes
    self.funcionarios = funcionarios
    self.sabores = sabores
    self.tamanhos = tamanhos
    self.adicionais = adicionais
    self.pedidos = pedidos
    self.deliverys = deliverys
    self.saldos = saldos

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
    print()
    print("-------------------------Saldo da Pizzaria-------------------------")
    print("Saldo da Pizzaria: R$", self.saldo)
    print()

  def visualizar_armazem(self):
    print()
    print("-------------------------Armazem da Pizzaria-------------------------")
    for sabor in self.sabores:
      print(f"Sabor: {sabor['nome']} - Preço: R${sabor['preco']:.2f}")
    print()
    for adicional in self.adicionais:
      print(f"Adicional: {adicional['nome']} - Preço: R${adicional['preco']:.2f} - quantidade: {adicional['quantidade']}")
      


class Pizza:
  def __init__(self, nome, preco, sabores, tamanhos):
    self.nome = nome
    self.preco = preco
    self.sabores = sabores
    self.tamanhos = tamanhos

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
            print("4 - Cadastrar tamanho")
            print("5 - Remover tamannho")
            print("6 - Visualizar tamanhos cadastrados")
            print("7 - Cadastrar adicional")
            print("8 - Remover adicional")
            print("9 - Visualizar adicionais cadastrados")
            print("10 - Voltar ao Menu Principal")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
              pizza = self.cadastrar_pizza()
              self.sabores.append(pizza)
            elif opcao == 2:
              self.remover_pizza()
            elif opcao == 3:
              self.visualizar_pizza()
            elif opcao == 4:
              self.cadastrar_tamanho()
            elif opcao == 5:
              self.remover_tamanho()
            elif opcao == 6:
              self.visualizar_tamanho()
            elif opcao == 7:
              self.cadastrar_adicional()
            elif opcao == 8:
              self.remover_adicional()
            elif opcao == 9:
              self.visualizar_adicional()
            elif opcao == 10:
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
    print()
    print("-------------------------Pizzas Cadastradas-------------------------")
    for pizza in self.sabores:
      print(f"Sabor: {pizza['nome']}, Preço: R${pizza['preco']:.2f}") 

  def cadastrar_tamanho(self):
    nome = input("Digite o nome do tamanho: ")
    multiplicador = float(input("Digite o multiplicador do tamanho: "))

    novo_tamanho = {
      'nome': nome,
      'multiplicador': multiplicador
    }

    self.tamanhos.append(novo_tamanho)
    print(f"Tamanho {nome} cadastrado com sucesso!")

  def remover_tamanho(self):
    nome = input("Digite o nome do tamanho a ser removido: ")
    for tamanho in self.tamanhos:
      if tamanho['nome'] == nome:
        self.tamanhos.remove(tamanho)
        print(f"Tamanho {nome} removido com sucesso!")
        return
    print(f"Tamanho {nome} não encontrado.")

  def visualizar_tamanho(self):
    print()
    print("-------------------------Tamanhos Cadastrados-------------------------")
    for tamanho in self.tamanhos:
      print(f"Tamanho: {tamanho['nome']}, Multiplicador: {tamanho['multiplicador']}")

  def cadastrar_adicional(self):
    nome = input("Digite o nome do adicional: ")
    preco = float(input("Digite o preço do adicional: "))
    quantidade = int(input("Digite a quantidade do adicional: "))

    novo_adicional = {
      'nome': nome,
      'preco': preco,
      'quantidade': quantidade
    }

    self.adicionais.append(novo_adicional)
    print(f"Adicional {nome} cadastrado com sucesso!")

  def remover_adicional(self):
    nome = input("Digite o nome do adicional a ser removido: ")
    for adicional in self.adicionais:
      if adicional['nome'] == nome:
        self.adicionais.remove(adicional)
        print(f"Adicional {nome} removido com sucesso!")
        return
    print(f"Adicional {nome} não encontrado.")

  def visualizar_adicional(self):
    print()
    print("-------------------------------------Adicionais-------------------------------------")
    for adicional in self.adicionais:
      print(f"Adicional: {adicional['nome']}, Preço: R${adicional['preco']:.2f}, Quantidade: {adicional['quantidade']}")


class Funcionario:
  def __init__(self, nome, cpf, cargo, salario, telefone, email, senha):
    self.nome = nome
    self.cpf = cpf
    self.cargo = cargo
    self.salario = salario
    self.telefone = telefone
    self.email = email
    self.senha = senha
    self.funcionarios = funcionarios

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
    print()
    print("-------------------------Funcionários Cadastrados-------------------------")
    for funcionario in self.funcionarios:
      print()
      print(f"Dados do funcionário {funcionario['nome']} ")
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
    self.clientes = clientes

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

    cpf_existe = True  # Defina cpf_existe como False antes do loop

    while True:
        cpf = input("Digite o CPF do cliente (apenas números): ")
        if len(cpf) == 11 and cpf.isdigit():
            for cliente in self.clientes:
                if cliente['cpf'] == cpf:
                    cpf_existe = False
                    print("CPF já cadastrado. Por favor, digite um CPF válido.")
                    break  
            if cpf_existe:
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
    print()
    print("-------------------------Clientes Cadastrados-------------------------")
    for cliente in self.clientes:
      print()
      print(f"Dados do cliente {cliente['nome']}")
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
      self.clientes = clientes
      self.sabores = sabores
      self.tamanhos = tamanhos
      self.adicionais = adicionais
      self.pedidos = pedidos

  def menu_pedido(self):
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
                  self.cadastrar_pedido()
              elif opcao == 2:
                  self.visualizar_pedido()
              elif opcao == 3:
                  break
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

    # Verificar se o adicional informado existe na lista de adicionais
    adicional_existente = False
    for adicional in self.adicionais:
        if adicional['nome'] == info_adicionais:
            adicional_existente = True
            break

    if not adicional_existente:
        print("Adicional não encontrado. Por favor, escolha um adicional válido.")
        return

    quantidade_adicionais = int(input("Digite a quantidade de adicionais: "))
    # Verificar se há quantidade suficiente de adicionais disponíveis
    for adicional in self.adicionais:
        if adicional['nome'] == info_adicionais:
            if quantidade_adicionais <= adicional['quantidade']:
                adicional['quantidade'] -= quantidade_adicionais
                break
            else:
                print("Quantidade de adicionais insuficiente.")
                return

    entregador = input("Digite o nome do entregador (se houver): ")
    
    novo_pedido = {
        'cliente': cliente,
        'cpf': cpf,
        'info_tamanhos': info_tamanhos,
        'info_sabor': info_sabor,
        'info_adicionais': info_adicionais,
        'quantidade_adicionais': quantidade_adicionais
        'entregador': entregador
    }
    
    self.pedidos.append(novo_pedido)
    print("Pedido cadastrado com sucesso!")


  def visualizar_pedido(self):
    print()
    print("-------------------------Pedidos Cadastrados-------------------------")
    for pedido in self.pedidos:
      print()
      print(f"Dados do pedido de {pedido['cliente']}")
      print(f"Nome: {pedido['cliente']}")
      print(f"CPF: {pedido['cpf']}")
      print(f"Tamanho: {pedido['info_tamanhos']}")
      print(f"Sabor: {pedido['info_sabor']}")
      print(f"Adicionais: {pedido['info_adicionais']}, Quantidade: {pedido['quantidade_adicionais']}")
      print(f"Entregador: {pedido['entregador']}")

  def calcular_valor_pedido(self, pedido):
    valor_pedido = 0
    for sabor in self.sabores:
        if sabor['nome'] == pedido['info_sabor']:
            valor_pedido += sabor['preco']
            break
    for tamanho in self.tamanhos:
        if tamanho['nome'] == pedido['info_tamanhos']:
            valor_pedido = (valor_pedido*tamanho['preco'])
            break
    for adicional in self.adicionais:
      
    
  
class Delivery:
  def __init__(self, pedido, funcionario, status, deliverys):
    self.pedido = pedido
    self.funcioanrio = funcionario
    self.status = status
    self.deliverys = deliverys

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
                    pizza = Pizza(None, None, sabores, tamanhos)
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
