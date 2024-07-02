class Livro:
    def __init__(self, titulo, autor, ano, genero):
        self.titulo = titulo
        self.autor = autor
        self.ano = ano
        self.genero = genero
        self.disponibilidade = True

class Usuario:
    def __init__(self, nome, usuario_id):
        self.nome = nome
        self.usuario_id = usuario_id

class Biblioteca:
    def __init__(self):
        self.livros = []
        self.usuarios = []

    def adicionar_livro(self, livro):
        self.livros.append(livro)
        print(f'O livro "{livro.titulo}" foi adicionado ao acervo.')

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)
        print(f'O usuário "{usuario.nome}" foi cadastrado.')

    def emprestar_livro(self, livro, usuario):
        if livro in self.livros and livro.disponibilidade and usuario in self.usuarios:
            livro.disponibilidade = False
            print(f'O livro "{livro.titulo}" foi emprestado para {usuario.nome}.')
        else:
            print('Não foi possível emprestar o livro. Verifique se o livro está disponível e o usuário está cadastrado.')

    def listar_livros_disponiveis(self):
        print('Livros disponíveis:')
        for livro in self.livros:
            if livro.disponibilidade:
                print(f'- {livro.titulo} ({livro.autor})')

    def listar_livros_emprestados(self):
        print('Livros emprestados:')
        for livro in self.livros:
            if not livro.disponibilidade:
                print(f'- {livro.titulo} ({livro.autor})')

    def listar_usuarios(self):
        print('Usuários cadastrados:')
        for usuario in self.usuarios:
            print(f'- {usuario.nome}')

biblioteca = Biblioteca()

def inicio():
        print('''
            
        ██████╗░██╗██████╗░██╗░░░░░██╗░█████╗░████████╗███████╗░█████╗░░█████╗░
        ██╔══██╗██║██╔══██╗██║░░░░░██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗
        ██████╦╝██║██████╦╝██║░░░░░██║██║░░██║░░░██║░░░█████╗░░██║░░╚═╝███████║
        ██╔══██╗██║██╔══██╗██║░░░░░██║██║░░██║░░░██║░░░██╔══╝░░██║░░██╗██╔══██║
        ██████╦╝██║██████╦╝███████╗██║╚█████╔╝░░░██║░░░███████╗╚█████╔╝██║░░██║
        ╚═════╝░╚═╝╚═════╝░╚══════╝╚═╝░╚════╝░░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝

        ███████╗░█████╗░████████╗███████╗░█████╗░
        ██╔════╝██╔══██╗╚══██╔══╝██╔════╝██╔══██╗
        █████╗░░███████║░░░██║░░░█████╗░░██║░░╚═╝
        ██╔══╝░░██╔══██║░░░██║░░░██╔══╝░░██║░░██╗
        ██║░░░░░██║░░██║░░░██║░░░███████╗╚█████╔╝
        ╚═╝░░░░░╚═╝░░╚═╝░░░╚═╝░░░╚══════╝░╚════╝░
            ''')
def execucao():
        while True:
            print('\nMenu:')
            print('1. Adicionar livro')
            print('2. Adicionar usuário')
            print('3. Emprestar livro')
            print('4. Listar livros disponíveis')
            print('5. Listar livros emprestados')
            print('6. Listar usuários')
            print('7. Sair')

            opcao = input('Escolha uma opção: ')

            if opcao == '1':
                titulo = input('Digite o título do livro: ')
                autor = input('Digite o autor do livro: ')
                ano = input('Digite o ano de publicação do livro: ')
                genero = input('Digite o gênero do livro: ')
                novo_livro = Livro(titulo, autor, ano, genero)
                biblioteca.adicionar_livro(novo_livro)

            elif opcao == '2':
                nome = input('Digite o nome do usuário: ')
                usuario_id = input('Digite o ID do usuário: ')
                novo_usuario = Usuario(nome, usuario_id)
                biblioteca.adicionar_usuario(novo_usuario)

            elif opcao == '3':
                titulo = input('Digite o título do livro a ser emprestado: ')
                usuario_nome = input('Digite o nome do usuário que vai pegar o livro emprestado: ')
                livro_emprestado = None
                usuario_emprestado = None

                for livro in biblioteca.livros:
                    if livro.titulo == titulo:
                        livro_emprestado = livro
                        break

                for usuario in biblioteca.usuarios:
                    if usuario.nome == usuario_nome:
                        usuario_emprestado = usuario
                        break

                if livro_emprestado and usuario_emprestado:
                    biblioteca.emprestar_livro(livro_emprestado, usuario_emprestado)
                else:
                    print('Livro ou usuário não encontrado.')

            elif opcao == '4':
                biblioteca.listar_livros_disponiveis()

            elif opcao == '5':
                biblioteca.listar_livros_emprestados()

            elif opcao == '6':
                biblioteca.listar_usuarios()

            elif opcao == '7':
                print('Saindo do programa. Até mais!')
                break

            else:
                print('Opção inválida. Tente novamente.')

inicio()
execucao()
