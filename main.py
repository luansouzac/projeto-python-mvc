import controllers.ControllerAluno

def mostrar_menu():
    print("\n===== Sistema de Gestão de Alunos =====")
    print("1. Adicionar Aluno")
    print("2. Listar Alunos")
    print("3. Procurar aluno")
    print("0. Sair")
    return input("Escolha uma opção: ")

def main():
    while True:
        opcao = mostrar_menu()

        if opcao == '1':
            controllers.ControllerAluno.adicionar_novo_aluno()
        elif opcao == '2':
            controllers.ControllerAluno.listar_alunos()
        elif opcao == '3':
            controllers.ControllerAluno.procurar_aluno_por_nome()
        elif opcao == '0':
            print('Saindo do sistema')
            break
        else:
            print('Opcao invalida, digite outra')
if __name__ == "__main__":
    main()