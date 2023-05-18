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
    return {
        # Acesso
        'Acesso': 'Para chegar ao End, o jogador precisa encontrar uma fortaleza usando olhos de ender e localizar a sala do portal. A sala tem um portal do End com 12 molduras, algumas com olhos já inseridos. O jogador precisa completar o portal com olhos de ender restantes. Ao ativar o portal, um som alto é emitido e o portal substitui os blocos centrais por blocos de portal do End. O jogador pode entrar no portal para ir ao End, junto com outras entidades que foram teleportadas antes.',
        # Ambiente
        'Ambiente':{
         'biomas': {
            # Biomas
            '1': 'O End',
            '2': 'Pequenas ilhas do End',
            '3': 'Zona média do End',
            '4': 'Zona elevada do End',
            '5': 'Zona árida do End'
            }, 
         'estruturas_geradas': {
             # Estruturas Geradas
             '1': 'Ilha central',
             '2': 'Ilhas externas',
             '3': 'Pilar do End',
             '4': 'Plataforma de obsidiana',
             '5': 'Portal de saida',
             '6': 'Passagem do End',
             '7': 'Cidade do End',
             '8': 'Barco do End',
             '9': 'Árvore do coro'
         },
         'recursos_de_terreno': {
             # Recursos de Terreno
             'ilha_principal': 'Na ilha principal, há dez torres de obsidiana com cristais do End no topo, que regeneram a saúde do dragão. O jogador deve destruir os cristais para enfraquecer o dragão e poder atacá-lo. Quando o dragão é derrotado, ele explode e deixa cair muita experiência e um ovo de dragão. O portal de saída é ativado e permite ao jogador voltar ao mundo normal ou explorar as ilhas externas do End, onde há cidades do End e navios do End com tesouros e elytras. O dragão pode ser renascido quantas vezes o jogador quiser, colocando quatro cristais do End ao redor do portal de saída.',
             'ilhas_externas': 'As ilhas externas do End são lugares misteriosos e isolados que só podem ser acessados após derrotar o dragão do End. Elas são compostas por ilhas flutuantes de variados tamanhos e formas, cobertas por plantas do coro que produzem frutas do coro. Nessas ilhas, o jogador pode encontrar cidades do End, que são estruturas raras e complexas que abrigam shulkers e baús com tesouros. Algumas cidades do End têm navios do End ancorados perto delas, que contêm itens ainda mais valiosos, como elytras e cabeça de dragão.'
         },
         'mobs': {
             # Mobs
             '1':{
                 # Enderman
                 'Enderman': {
                     # Drops
                     'drop1': 'Pérola de ender',
                     'drop2': '5 XP',
                     'drop3': 'Qualquer bloco que está segurando'
                }
            },
             '2':{
                # Shulker
                 'Shulker': {
                    # Drops
                    'drop1': 'Casco de shulker',
                    'drop2': '5 XP'     
                 
                }
            },
             '3':{
                # Dragão do Ender
                'Dragão_Ender': {
                    # Drops
                    'drop1': '12000 XP',
                    'drop2': 'Ovo de dragão'

                }
            }
         },
         'blocos': {
             # Blocos
             '1':{
                # Gerados Naturalmente
                    '1': 'Ar',
                    '2': 'Rocha-mãe',
                    '3': 'Obsidiana',
                    '4': 'Pedra do End',
                    '5': 'Planta do coro',
                    '6': 'Flor do coro'
            },
             '2':{
                # Criados naturalmente
                '1': 'Ar',
                '2': 'Rocha-mãe',
                '3': 'Obsidiana',
                '4': 'Tocha na parede',
                '5': 'Fogo',
                '6': 'Portal do End',
                '7': 'Ovo do dragão',
                '8': 'Passagem do End'
            },
             '3':{
                # Estruturas
                '1': 'Ar',
                '2': 'Obsidiana',
                '3': 'Bau',
                '4': 'Vidro roxo',
                '5': 'Suporte de porções',
                '6': 'Moldura',
                '7': 'Estandarte magenta na parede',
                '8': 'Lâmpada do End',
                '9': 'Bloco de púrpura',
                '10': 'Pilar de púrpura',
                '11': 'Laje de púrpura',
                '12': 'Escadas de púrpura',
                '13': 'Tijolos depedra do End',
                '14': 'Cabeça do dragão'
            }
         }
        },
        # Informações Técnicas
        'Informacoes_tecnicas': {
            # ID
            'ID': {
                'Nome': 'O End',
                'ID_EJ': 'the_end',
                'ID_numerico': 1
                }
        },
        # Conquistas
        'Conquistas': {
            '1': {
                'Nome': 'O End?',
                'Descricao': 'Entre no Portal do End'
            },
            '2': {
                'Nome': 'O Fim.',
                'Descricao': 'Mate o dragão ender'
            },
            '3': {
                'Nome': 'Aceita uma pastilha?',
                'Descricao': 'Colete o bafo do dragão com um frasco de vidro'
            },
            '4': {
                'Nome': 'O Fim... de novo...',
                'Descricao': 'Reviva o dragão ender'
            },
            '5': {
                'Nome': 'A vista é ótima',
                'Descricao': 'Levite 50 blocos de altura, após ser acertado por um shulker'
            }
        },
        # Progressos
        'Progressos': {
            '1': {
                'Nome': 'O End?',
                'Descricao': 'Ou o começo',
                'Requisitos': 'Entre na dimensão do End.',
                'ID': 'minecraft:end/root'
            },
            '2': {
                'Nome': 'Liberte o End',
                'Descricao': 'Boa sorte',
                'Requisitos': 'Mate o dragão ender',
                'ID': 'minecraft:end/kill_dragon'
            },
            '3': {
                'Nome': 'Liberte o End',
                'Descricao': 'Boa sorte',
                'Requisitos': 'Mate o dragão ender',
                'ID': 'minecraft:end/kill_dragon'
            }
        }
        #{'OE': 'O End?', 'LE': '', 'AG':'A nova geracao', 'RG': 'O comeco do fim', 'ON': 'O End.. de novo...', 'AP': 'Aceita uma pastilha?', 'TG': 'A cidade no fim do jogo', 'AA': 'Ao inifinito... e alem!', 'OC': 'Otima vista daqui de cima'}
    }
@app.route('/en')
def en():
    return {
        # Accessing
        'access': {'A': 'B'},
        # Environment
        'environment': {'B': 'Biomes', 'G': 'Generated Structured','T': 'Terrain Features', 'M': 'Mobs', 'Bl': 'Blocks'},
        # Technical Information
        'technical_information': {'C': 'D'},
        # Achievements
        'achievements': {'TE': 'The End?', 'te': 'The End.', 'YM': 'You Need a Mint', 'TA': 'The End... Again...', 'GH': 'Great View From Up Here'},
        # Advancements
        'advancements': {'TE': 'The End?', 'FE': 'Free The End', 'TG':'The Next Generation', 'RG': 'Remote Getaway', 'TA': 'The End... Again...', 'YM': 'You Need a Mint', 'TG': 'The City at the End of the Game', 'SL': 'Sky\'s the Limit', 'GH': 'Great View From Up Here'}
    }

# Start a API - Inicia a API
if __name__ == '__main__':
    app.run(debug=True)