from typing import Dict, Any
import json

def carregar_dados() -> Dict[Any, Any]:
    try:
        with open("agenda.json", 'r') as f:
            agenda = json.load(f)
            print(f'Carregando {len(agenda)} contatos')
            return agenda
    except FileNotFoundError:
        print('Iniciando uma agenda vazia')
    except json.JSONDecodeError:
        print('Agenda corrompida, inicinando com uma agenda vazia')    
    agenda = dict()
    return agenda

def salvar_dados(agenda):
    with open('agenda.json', 'w') as f:
        json.dump(agenda, f)
    print('Salvando contatos...')

def menu():
    print('AGENDA TELEFÔNICA '.center(40, '='))
    print()
    print('1. Cadastrar contato')
    print('2. Listar contatos')
    print('3. Remover contato')
    print('4. Buscar contato')
    print('0. Finalizar')
    print()
    try:
        opcao = int(input('Qual a opção? '))
    except ValueError:
        opcao = 99
    return opcao

def confirma():
    resposta = input('Confirma a operação (S/N)?')
    if resposta.lower() in ['s', 'sim', 'y', 'yes']:
        return True
    else:
        return False
    
def cadastrar(agenda):
    print(' Adicionar novo contato '. center(40, '-'))
    nome = input('Qual o nome do contato? ')
    telefone = input('Qual o número do telefone? ')
    email = input('Qual o email? ')
    if confirma():
        agenda[nome] = { 'telefone': telefone, 'email': email}
        print('Cadastro realizado')
    else:
        print('Operação cancelada')
        pass

def listar(agenda):
    print(' Meus contatos '.center(40, '-'))
    if len(agenda) == 0:
        print('Não tenho contatos... 😿')
        return
    print('Nome'.ljust(40) + ' ' + 'Telefone'.rjust(15) \
        + ' ' + 'Email')
    print('-' * 40 + ' ' + '-' * 15 + ' ' + '-' * 30)
    
    for contato in agenda.items():
        print(f'{contato[0].ljust(40)}'
            f'{contato[1]['telefone'].rjust(15)}'
            f'  {contato[1]['email']}')
        print()
    pass
    
def remover(agenda):
    nome = input('Qual contato deseja remover?')
    try:
        del agenda[nome]
        print('Contato removido')
    except KeyError:
        print('Contato inexistente')

def buscar(agenda):
    nome = input('Qual o contato deseja detalhar? ')
    dados = agenda.get(nome)
    if dados is not None:
        print(f'Telefone: {dados['telefone']}')
        print(f'Email: {dados['email']}')
    else:
        print('Contato inexistente')

if __name__ == '__main__':
    print('Bem vindo à agenda telefônica')
    
    agenda = carregar_dados()
    
    while True:
        opcao = menu()
        
        if opcao == 0:
            print('Tchau!')
            salvar_dados(agenda)
            exit()
        elif opcao == 1:
            cadastrar(agenda)
        elif opcao == 2:
            listar(agenda)
        elif opcao == 3:\
            remover(agenda)
        elif opcao == 4:
            buscar(agenda)
        else:
            print('Opção inválida!')
