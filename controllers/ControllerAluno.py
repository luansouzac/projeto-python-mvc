from models.Aluno import Aluno

def adicionar_novo_aluno():
    print('\n --- Adicionar novo aluno ---')
    nome = input('Digite o nome aluno: ')
    matricula = input('Digite a matricula do aluno: ')

    if nome and matricula:
        aluno = Aluno.criar(nome, matricula)
        if aluno:
            print(f'Aluno {nome} cadastrado!' )
        else:
            print(f'Erro ao cadastrar {aluno}')
    else:
        print('Nome e matricula nao podem estar vazios')


def procurar_aluno_por_nome():
    print('\n --- Procurar aluno ---')
    nome = input('Digite o nome que quer pesquisar: ')

    if nome:
        aluno = Aluno.procurar_por_nome(nome)
        if aluno:
            print(f'Aluno encontrado: {aluno}')
            return aluno
        else:
            print('Erro ao encontrar aluno')
    else:
        print('Obrigatorio o nome do aluno')
    


