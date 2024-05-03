import random
# abaixo se encontram todas as listas utilizadas durante o uso do sistema, contendo:
# clientes, funcionarios, sabores, tamanhos, adicionais, pedidos e saldos

clientes = [
  {
    'nome': 'Alice',
    'cpf': '12345678900',
    'bairro': 'santa Monica',
    'rua': 'felix kleis',
    'numero' : '123',
    'telefone': '999999999',
    'email': 'alice@example.com'
  },
  {
    'nome': 'Igor',
    'cpf': '12345678911',
    'bairro': 'trindade',
    'rua': 'lauro linhares',
    'numero' : '123',
    'telefone': '999999999',
    'email': 'igor@example.com'
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
    'quantidade_adicionais': 2,
    'entregador': 'fabio',
    'status': 'pendente',
    'valor': 25,
    'codigo': 1234
  },
  {
    'cliente': 'igor',
    'cpf': '12345678911',
    'info_tamanhos': 'grande',
    'info_sabor': 'calabresa',
    'info_adicionais': 'coca',
    'quantidade_adicionais': 3,
    'entregador': 'fabio',
    'status': 'pendente',
    'valor': 25,
    'codigo': 1111
  } 
]



saldos = [
  {
    'dia': '2023-08-01',
    'saldo': 1200.00
  }
]

# fim das listas de interação com o sistema

# incio das classes

class Pizzaria(): # adicionar todas as listas utlizadas na classe pizzaria
  def __init__(self):
    self.clientes = clientes
    self.funcionarios = funcionarios
    self.sabores = sabores
    self.tamanhos = tamanhos
    self.adicionais = adicionais
    self.pedidos = pedidos
    self.saldos = saldos

  def menu_pizzaria(self): #menu secundario
    opcao = 0
    while True:
        try:
            print()
            print("-------------------------Menu Pizzaria-------------------------")
            print("por favor selecione uma das opções abaixo:")
            print("1 - cadastrar saldo do dia")
            print("2 - Visualizar saldo")
            print("3 - Visualizar Armazem")
            print("4- Voltar ao Menu Principal")
            opcao = int(input("Digite a opção desejada: "))
            if opcao == 1:
                self.cadastrar_saldo()
            elif opcao == 2:
                self.visualizar_saldo()
            elif opcao == 3:
                self.visualizar_armazem()
            elif opcao == 4:
                break
        except ValueError:
            print("Opção inválida. Por favor, digite um número válido.")

  def cadastrar_saldo(self):
    dia = input("Digite o dia do saldo: ")
    saldo = float(input("Digite o saldo do dia: "))

    novo_saldo = {
      'dia': dia,
      'saldo': saldo
    }

    self.saldos.append({'dia': dia, 'saldo': saldo})
    print("Saldo cadastrado com sucesso!")

    return novo_saldo

  def visualizar_saldo(self):
    total = 0
    print()
    print("-------------------------Saldos-------------------------")
    for saldo in self.saldos:
      print(f"Dia: {saldo['dia']}, Saldo: R${saldo['saldo']}")
      total += saldo['saldo']
    print()
    print(f"Total de saldos: R${total}")

  def visualizar_armazem(self):
    print()
    print("-------------------------Armazem da Pizzaria-------------------------")
    for sabor in self.sabores:
      print(f"Sabor: {sabor['nome']} - Preço: R${sabor['preco']:.2f}")
    print()
    for adicional in self.adicionais:
      print(f"Adicional: {adicional['nome']} - Quantidade disponível: {adicional['quantidade']} - Preço: R${adicional['preco']:.2f}")



class Pizza:  # adicionar todas as listas utlizadas na classe pizza
  def __init__(self):
    self.sabores = sabores
    self.tamanhos = tamanhos
    self.adicionais = adicionais

  def menu_pizza(self): #menu secundario
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
              self.cadastrar_pizza()
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

    return nova_pizza

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
      print(f"Sabor: {pizza['nome']} - Preço: R${pizza['preco']:.2f}")


  def cadastrar_tamanho(self):
    tipo = input("Digite o nome do tamanho: ")
    multiplicador = float(input("Digite o multiplicador do tamanho: "))

    novo_tamanho = {
      'tipo': tipo,
      'multiplicador': multiplicador
    }

    self.tamanhos.append(novo_tamanho)
    print(f"Tamanho {tipo} cadastrado com sucesso!")

    return novo_tamanho

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
      print(f"Tamanho: {tamanho['tipo']}, Multiplicador: {tamanho['multiplicador']}")

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

    return novo_adicional

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



class Funcionario:  # adicionar todas as listas utlizadas na classe funcionario
  def __init__(self):
    self.funcionarios = funcionarios

  def menu_funcionario(self): #menu secundario
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


class Cliente:  # adicionar todas as listas utlizadas na classe cliente
  def __init__(self):
    self.clientes = clientes

  def menu_cliente(self): #menu secundario
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
          self.cadastrar_clientes()
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

  def cadastrar_clientes(self):
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

    return novo_cliente

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


class Pedido:  # adicionar todas as listas utlizadas na classe pedido
  def __init__(self):
      self.clientes = clientes
      self.sabores = sabores
      self.tamanhos = tamanhos
      self.adicionais = adicionais
      self.pedidos = pedidos

  def menu_pedido(self): #menu secundario
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
                cliente = cliente['nome']
                break
          else:
              print("CPF não encontrado.")
              print("Por favor, cadastre o cliente antes de fazer o pedido.")
              return
      else:
          print("CPF inválido. Por favor, digite um CPF válido (11 dígitos)")
          return

      info_tamanhos = input("Digite o tamanho da pizza: ")
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

      for adicional in self.adicionais:
          if adicional['nome'] == info_adicionais:
              if quantidade_adicionais <= adicional['quantidade']:
                  adicional['quantidade'] -= quantidade_adicionais
                  break
              else:
                  print("Quantidade de adicionais insuficiente.")
                  return

      entregador = input("Digite o nome do entregador (se houver): ")

      valor = self.calcular_valor_pedido(info_sabor, info_tamanhos,
                                         info_adicionais, quantidade_adicionais)

      codigo = self.gerar_codigo_pedido()

      novo_pedido = {
          'cliente': cliente,
          'cpf': cpf,
          'info_tamanhos': info_tamanhos,
          'info_sabor': info_sabor,
          'info_adicionais': info_adicionais,
          'quantidade_adicionais': quantidade_adicionais,
          'entregador': entregador,
          'status': 'Aguardando entrega',
          'valor': valor,
          'codigo': codigo
      }

      self.pedidos.append(novo_pedido)
      print("Pedido cadastrado com sucesso!")

      return novo_pedido

  def visualizar_pedido(self):
    print()
    print("-------------------------Pedidos Cadastrados-------------------------")
    for pedido in self.pedidos:  # Verifica se a lista de pedidos não está vazia
      print()
      print(f"Dados do pedido de {pedido['cliente']}")
      print(f"Nome: {pedido['cliente']}")
      print(f"CPF: {pedido['cpf']}")
      print(f"Tamanho: {pedido['info_tamanhos']}")
      print(f"Sabor: {pedido['info_sabor']}")
      print(f"Adicionais: {pedido['info_adicionais']}, Quantidade: {pedido['quantidade_adicionais']}")
      print(f"Status: {pedido['status']}")
      print(f"Valor: R${pedido['valor']:.2f}")
      print(f"Código: {pedido['codigo']}")
      print()


  def calcular_valor_pedido(self, sabor, tamanho, adicional, quantidade_adicionais):
    valor_pedido = 0
    for sab in self.sabores:
        if sab['nome'] == sabor:
            valor_pedido += sab['preco']
            break
    for tam in self.tamanhos:
        if tam['tipo'] == tamanho:
            valor_pedido = (valor_pedido * tam['multiplicador'])
            break
    for adc in self.adicionais:
        if adc['nome'] == adicional:
            valor_pedido += (adc['preco'] * quantidade_adicionais)
            break
    return valor_pedido

  def gerar_codigo_pedido(self):
    codigo = int(random.randint(1000, 9999))
    return codigo


class Delivery:  # adicionar todas as listas utlizadas na classe delivery
  def __init__(self):
      self.pedidos = pedidos
      self.funcionarios = funcionarios
      self.clientes = clientes

  def menu_delivery(self): #menu secundario
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
                break
            else:
                print("Opção inválida. Por favor, digite um número entre 1 e 3.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número.")


  def visualizar_delivery(self):
    print()
    print("-------------------------Deliverys Cadastrados-------------------------")
    for pedido in self.pedidos:
        cliente_nome = pedido['cliente']
        cliente_endereco = self.obter_endereco_cliente(cliente_nome)
        print()
        print(f"Dados do Delivery de {cliente_nome}")
        print(f"Nome: {cliente_nome}")
        print(f"Tamanho: {pedido['info_tamanhos']}")
        print(f"Sabor: {pedido['info_sabor']}")
        print(f"Adicionais: {pedido['info_adicionais']}, Quantidade:{pedido['quantidade_adicionais']}")
        print(f"Endereço: {cliente_endereco}")
        print(f"Entregador: {pedido.get('entregador', 'Não especificado')}")
        print(f"Status: {pedido['status']}")
        print(f"Valor: R${pedido['valor']:.2f}")
        print()


  def obter_endereco_cliente(self, nome_cliente):
      for cliente in self.clientes:
          if cliente['nome'] == nome_cliente:
              endereco = f"{cliente['rua']}, {cliente['numero']}, {cliente['bairro']}"
              return endereco
      return "Endereço não encontrado"

  def finalizar_delivery(self): 
    cpf = input("Digite o CPF do cliente (apenas números): ")
    codigo_pedido = int(input("Digite o código do pedido para finalizar o delivery: "))
    for pedido in self.pedidos[:]:  # Usando uma cópia da lista para evitar problemas de remoção durante a iteração
        if pedido['cpf'] == cpf and pedido['codigo'] == codigo_pedido:
            pedido['status'] = "Finalizado"
            self.pedidos.remove(pedido)
            print(f"Delivery do pedido {codigo_pedido} finalizado com sucesso!")
            return
    print(f"Delivery do pedido {codigo_pedido} não encontrado.")




def main(): #menu principal - main do sistema, responsavel por perdir acesso a todos os menus secundários
  while True:
    try:
      print("Bem vindo a Pizzaria")
      funcionario_nome = input("Insira o nome do funcionário: ")
      funcionario_senha = input("Insira a senha do funcionário: ")
      for funcionario in funcionarios:
        if funcionario['nome'] == funcionario_nome and funcionario['senha'] == funcionario_senha:
          print(f"Bem vindo {funcionario_nome}!")
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
                    pizza = Pizza()
                    pizza.menu_pizza()
                  elif opcao == 3:
                    cliente = Cliente()
                    cliente.menu_cliente()
                  elif opcao == 4:  
                    funcionario = Funcionario()
                    funcionario.menu_funcionario()
                  elif opcao == 5:
                    pedido = Pedido()
                    pedido.menu_pedido()
                  elif opcao == 6:
                    delivery = Delivery()
                    delivery.menu_delivery()
                  elif opcao == 7:
                    print("Saindo...")
                    break
              except EOFError:
                break
        else:
          print("Senha ou nome de usuário incorretos. Por favor, tente novamente.")  
      else:
          print("Usuário ou senha inválidos.")
    except EOFError:
      break


if __name__ == "__main__":
  main()
