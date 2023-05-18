from flask import Flask

# Hi, I'm Victor and I'm creating a API for accessing a dimension The End, of minecraft. And the code is in two languages,
# English and Portuguese. So if you don't understand Portuguese, you're going to read the API in English.  

# Olá, sou o Victor e estou criando uma API para acessar a dimensão do Fim, do minecraft. E o código está em dois idiomas,
# Inglês e Português. Então, se você não entende inglês, Você vai ler a API em português.


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

# Idioma Portuguese
if pt() == True:
    # Acesso
    @app.route('/pt/acesso')
    def accesso():
        return {'A': 'B'}
    
    # Ambiente
    @app.route('/pt/ambiente')
    def ambiente():
        return {'B': 'Biomas', 'E': 'Estruturas Geradas', 'R': 'Recursos de Terreno', 'M': 'Mobs', 'Bl': 'Blocos'}, True
    
    # Informações Técnicas
    @app.route('/pt/informacoes_tecnicas')
    def informacoes_tecnicas():
        return {'C': 'D'}
    
    # Conquistas
    @app.route('/pt/conquistas')
    def conquistas():
        return {'OE': 'O End?', 'of': 'O Fim.', 'AP': 'Aceita uma pastilha?', 'ON': 'O Fim... de novo...', 'AO': 'A vista e otima'}
    
    #Progressos
    @app.route('/pt/progressos')
    def progressos():
        return {'OE': 'O End?', 'LE': 'Liberte o End', 'AG':'A nova geracao', 'RG': 'O comeco do fim', 'ON': 'O End.. de novo...', 'AP': 'Aceita uma pastilha?', 'TG': 'A cidade no fim do jogo', 'AA': 'Ao inifinito... e alem!', 'OC': 'Otima vista daqui de cima'}

    # /Ambientes/
    if ambiente() == True:
        
        # Biomas
        @app.route('/ambientes/biomas')
        def biomas():
            return {}, True

        # Estruturas Geradas
        @app.route('/ambientes/estruturas_geradas')
        def estruturas_geradas():
            return {}, True

        # Recursos de Terreno
        @app.route('/ambientes/recursos_terreno')
        def recursos_terreno():
            return {}, True
        
        # Mobs
        @app.route('/ambientes/mobs')
        def mobs():
            return {}, True
        
        #Blocos
        @app.route('/ambientes/blocos')
        def blocos():
            return {}, True

# Language English
if en() == True:
    # Accessing
    @app.route('/en/accessing')
    def access():
        return {'A': 'B'}

    
    # Environment
    @app.route('/en/environment')
    def environment():
        return {'B': 'Biomes', 'G': 'Generated Structured','T': 'Terrain Features', 'M': 'Mobs', 'Bl': 'Blocks'}

    # Technical Information
    @app.route('/en/technical_information')
    def technical_information():
        return {'C': 'D'}

    
    # Achievements
    @app.route('/en/achievements')
    def achievements():
        return {'TE': 'The End?', 'te': 'The End.', 'YM': 'You Need a Mint', 'TA': 'The End... Again...', 'GH': 'Great View From Up Here'}
    
    # Advancements
    @app.route('/en/advancements')
    def advancements():
        return {'TE': 'The End?', 'FE': 'Free The End', 'TG':'The Next Generation', 'RG': 'Remote Getaway', 'TA': 'The End... Again...', 'YM': 'You Need a Mint', 'TG': 'The City at the End of the Game', 'SL': 'Sky\'s the Limit', 'GH': 'Great View From Up Here'}

# Start a API - Inicia a API
if __name__ == '__main__':
    app.run(debug=True)

    