def menu():
    menu = ('''
[D]  - Depositar
[S]  - Sacar
[E]  - Extrato
[nc] - Nova conta
[lc] - Listar contas
[nu] - Novo usuário
[Q]  - Sair
-- ''')
    return input(menu)


def depositar(saldo, valor, extrato):

    validacao = str(input(f'Deseja realmente realizar um deposito de R$ {valor:.2f}? S ou N'))

    if validacao.upper() == 'S':
        saldo += valor
        print(f'Deposito de R$ {valor:.2f} realizado com sucesso!')
        extrato += f'Deposito efetuado de R$ {valor:.2f} - Saldo R$ {saldo:.2f}\n'
        return saldo, extrato

    elif validacao.upper() == 'N':
        print('Opereção não realizada')

    else:
        print('Opcão inválida')

    return saldo, extrato


def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):

    if numero_saques == LIMITE_SAQUES:
        print('Você excedeu seu limite de saques hoje.')

    elif valor > limite:
        print('Valor acima do limite de saque.')

    else:
        validacao = str(input(f'Tem certeza que quer efetuar um saque de R$ {valor:.2f}? S ou N'))
        if validacao.upper() == 'S':
            if valor > saldo:
                print('Você não tem saldo suficiente!')

            else:
                saldo -= valor
                print(f'Saque de R$ {valor:.2f} realizado com sucesso!')
                numero_saques += 1
                extrato += f'Saque efetuado de R$ {valor:.2f} - Saldo R$ {saldo:.2f}\n'

        elif validacao == 'N':
            print('Operação não realizada!')

        else:
            print('Opcão inválida')

    return saldo, extrato


def exibir_extrato(saldo, /, *, extrato):
    print('''
========== Extrato ==========
        ''')
    print(extrato)

    print(f'Saldo final: R${saldo:.2f}')
    print('==================')


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    if filtrar_usuario(cpf, usuarios):
        print('Já existe uma conta criada para esse CPF!')
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

    print("Usuário criado com sucesso!")


def filtrar_usuario(cpf, usuarios):
    usuarios_filtrados = [usuario for usuario in usuarios if usuario['cpf'] == cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Digite seu cpf: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print('Conta criada!')
        return {'agencia': agencia, 'numero_conta': numero_conta, 'usuario': usuario}

    print('Usuário não encontrado!')

def listar_contas(contas):
    for conta in contas:
        linha = f"""\
Agência:{conta['agencia']}
C/C:{conta['numero_conta']}
Titular:{conta['usuario']['nome']}
        """
        print("=" * 50)
        print(linha)


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            valor = float(input("Informe o valor do depósito: "))

            saldo, extrato = depositar(saldo, valor, extrato)

        elif opcao == "s":
            valor = float(input("Informe o valor do saque: "))

            saldo, extrato = sacar(
                saldo=saldo,
                valor=valor,
                extrato=extrato,
                limite=limite,
                numero_saques=numero_saques,
                LIMITE_SAQUES=LIMITE_SAQUES,
            )

        elif opcao == "e":
            exibir_extrato(saldo, extrato=extrato)

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()