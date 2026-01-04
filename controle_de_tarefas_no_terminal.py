import os
import json

def exibir_nome():
    print('''
█▀▀ █▀█ █▄ █ ▀█▀ █▀█ █▀█ █   █▀▀   █▀▄ █▀▀   ▀█▀ ▄▀█ █▀█ █▀▀ █▀▀ ▄▀█ █▀
█▄▄ █▄█ █ ▀█  █  █▀▄ █▄█ █▄▄ ██▄   █▄▀ ██▄    █  █▀█ █▀▄ ██▄ █▀  █▀█ ▄█
''')
    
def exibir_subtitulo(subtitulo):
    print(subtitulo)

def redirecionar_menu():
    print('Para voltar ao menu principal, aperte uma tecla')
    input()
    main()

def opcoes():
    print('1 - Criar Tarefas')
    print('2 - Listar Tarefas')
    print('3 - Alterar Título da Tarefa')
    print('4 - Alterar Status da Tarefa')
    print('5 - Sair')

def criar_tarefa():

    titulo = input('Digite o título da sua tarefa: ')

    if titulo.strip() == '':
        print('Não é possível adicionar tarefas sem titulo, por favor, informe um título.')
        redirecionar_menu()

    else:
        titulo_normalizado = normalizar_caracteres(titulo)
        flag_titulo = True

        for tarefa in tarefas:
            tarefa_normalizada = normalizar_caracteres(tarefa['titulo'])
            if tarefa_normalizada == titulo_normalizado:
                flag_titulo = False
                break  # deixar mais rápido, caso encontre antes.

        if flag_titulo:

            status = input('Digite o status da sua tarefa (pendente / concluida): ').strip().lower()

            while status not in ['pendente','concluida']:
                print('Status da sua tarefa está incorreto, por favor, escolha um dos dois: (pendente / concluída)')
                status = input('Digite o status da sua tarefa (pendente / concluída): ').strip().lower()

            nova_tarefa = {'titulo':titulo, 'status':status}
            tarefas.append(nova_tarefa)
            salvar_json()

        else:
            limpar_terminal()
            print('O título da sua tarefa já existe, por favor, informar outro titulo.\nCaso precise revisar as tarefas existentes, aperte a tecla 2 no menu de opções.')
            redirecionar_menu()
            
        redirecionar_menu()
# def criar_tarefa():

#     titulo = input('Digite o título da sua tarefa: ')

#     if titulo.strip() == '':
#         print('Não é possível adicionar tarefas sem titulo, por favor, informe um título.')
#         redirecionar_menu()

#     else:
#         titulo_normalizado = normalizar_caracteres(titulo)
#         flag_titulo = True

#         for tarefa in tarefas:
#             tarefa_normalizada = normalizar_caracteres(tarefa['titulo'])
#             if tarefa_normalizada == titulo_normalizado:
#                 flag_titulo = False
#                 break  # deixar mais rápido, caso encontre antes.

#         if flag_titulo:

#             status = input('Digite o status da sua tarefa (pendente / concluída): ').strip().lower()
#             if status == 'pendente' or 'concluida':
#                 nova_tarefa = {'titulo':titulo, 'status':status}
#                 tarefas.append(nova_tarefa)
#                 salvar_json()
#             else:
#                 print('Status da sua tarefa está incorreto, por favor, escolha um dos dois: (pendente / concluída)')
#                 redirecionar_menu() # Mudar a lógica
#         else:
#             limpar_terminal()
#             print('O título da sua tarefa já existe, por favor, informar outro titulo.\nCaso precise revisar as tarefas existentes, aperte a tecla 2 no menu de opções.')
#             redirecionar_menu()
            
#         redirecionar_menu()

def listar_tarefas():

    limpar_terminal()
    print(f'{'Título da Tarefa'.ljust(23)} | {'Status'.ljust(20)}')

    for tarefa in tarefas:
        titulo = tarefa['titulo']
        status = tarefa['status']

        print(f' - {titulo.ljust(20)} | {status.ljust(20)}')

    redirecionar_menu()  

def normalizar_caracteres(tarefa):
    return tarefa.strip().lower()

def alterar_titulo_tarefa():

    nome_tarefa = input('Digite o titulo da tarefa: ').strip().lower()
    tarefa_encontrada = False

    for tarefa in tarefas:
        tarefa_normalizada = normalizar_caracteres(tarefa['titulo'])
        if tarefa_normalizada == nome_tarefa:
            tarefa_encontrada = True
            novo_titulo = input('Digite o novo título a tarefa: ')
            tarefa['titulo'] = novo_titulo
            salvar_json()
            print('Tarefa renomeada com sucesso!')
    if not tarefa_encontrada:
        print('Não foi encontrado a sua tarefa, por favor, tente novamente.')
    
    redirecionar_menu()

def alterar_status_tarefa():
    nome_tarefa = input('Digite o nome da tarefa que deseja alterar: ').strip().lower()
    tarefa_encontrada = False

    for tarefa in tarefas:

        tarefa_normalizada = normalizar_caracteres(tarefa['titulo'])
        if tarefa_normalizada == nome_tarefa:
            tarefa_encontrada = True 
            tarefa['status'] = 'concluída' if tarefa['status'] == 'pendente' else 'pendente'
            salvar_json()
            print('Tarefa alterada com sucesso!')

    if not tarefa_encontrada:
        print('Não foi encontrado a sua tarefa, por favor, tente novamente.')

    redirecionar_menu()

def sair():
    limpar_terminal()
    exibir_subtitulo('''
▄▀█ █▀█ █▀█   █▀▀ █▄ █ █▀▀ █▀▀ █▀█ █▀█ ▄▀█ █▀▄ █▀█ 
█▀█ █▀▀ █▀▀   ██▄ █ ▀█ █▄▄ ██▄ █▀▄ █▀▄ █▀█ █▄▀ █▄█ ▄
''')

def escolha_opcao():

    while True:
    
        try:
            escolha = int(input('Digite um número que corresponda as opções: '))
            break
        except ValueError:
            limpar_terminal()
            print('O valor informado está incorreto, por favor, escolha uma das nossas opções em valor númerico.')
            opcoes()


    match escolha:

        case 1:
            return criar_tarefa()
        
        case 2:
            return listar_tarefas()
        
        case 3:
            return alterar_titulo_tarefa()
        
        case 4:
            return alterar_status_tarefa()
        
        case 5:
            return sair()
        
        case _:
            print(f'Valor digitado está incorreto, por favor, tente novamente com uma das nossas opções.')
            redirecionar_menu()

def limpar_terminal():
    os.system('cls')

def salvar_json():
    with open('tarefas.json', 'w', encoding='utf-8') as arquivo:
        json.dump(tarefas, arquivo, ensure_ascii=False, indent=4)

def carregar_json():
    global tarefas
    try:
        with open('tarefas.json', 'r', encoding='utf-8') as arquivo:
            tarefas = json.load(arquivo)
    except FileNotFoundError:
        tarefas = []

def main():
   carregar_json()
   limpar_terminal()
   exibir_nome()
   opcoes()
   escolha_opcao()

if __name__ == '__main__':
    main()
