from flask import Flask

# Hi, I'm Victor and I'm creating a API for accessing a dimension The End, of minecraft. And the code is in two languages,
# English and Portuguese. So if you don't understand Portuguese, you're going to read the API in English.  

# Olá, sou o Victor e estou criando uma API para acessar a dimensão do Fim, do minecraft. E o código está em dois idiomas,
# Inglês e Português. Então, se você não entende inglês, Você vai ler a API em português.

def APIonline():
    # cria os jsons - create the jsons
    app = Flask(__name__)

    # Welcome - Bem-vindo
    @app.route('/')
    def index():
        return {'W': 'Welcome to API of The End!', 'B': 'Bem-vindo a API do Fim!'}
    
    @app.route('/pt')
    def pt():
        return True
    @app.route('/en')
    def en():
        return True

    # Accessing - Acesso
    @app.route('en/accessing')
    def access():
        return {'A': 'B'}
    @app.route('pt/acesso')
    def accesso():
        return {'A': 'B'}
    
    # Environment - Ambiente
    @app.route('en/environment')
    def environment():
        return {'B': 'Biomes', 'G': 'Generated Structured','T': 'Terrain Features', 'M': 'Mobs', 'Bl': 'Blocks'}
    @app.route('pt/ambiente')
    def ambiente():
        return {'B': 'Biomas', 'E': 'Estruturas Geradas', 'R': 'Recursos de Terreno', 'M': 'Mobs', 'Bl': 'Blocos'}

    # Technical Information - Informações Técnicas
    @app.route('en/technical_information')
    def technical_information():
        return {'C': 'D'}
    @app.route('pt/informacoes_tecnicas')
    def informacoes_tecnicas():
        return {'C': 'D'}
    
    # Achievements - Conquistas
    @app.route('en/achievements')
    def achievement():
        return {'TE': 'The End?', 'te': 'The'}


    # Start a API - Inicia a API
    app.run()

    