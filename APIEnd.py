from flask import Flask

# Hi, I'm Victor and I'm creating a API for accessing a dimension The End, of minecraft. And the code is in two languages,
# English and Portuguese. So if you don't understand Portuguese, you're going to read the API in English.  

# Olá, sou o Victor e estou criando uma API para acessar a dimensão do Fim, do minecraft. E o código está em dois idiomas,
# Inglês e Português. Então, se você não entende inglês, Você vai ler a API em português.

# Create the JSONs - Cria os JSONs
app = Flask(__name__)

# Welcome - Bem-vindo
@app.route('/')
def index():
    return {'W': 'Welcome to API of The End!', 'B': 'Bem-vindo a API do Fim!'}

# Portuguese - Português
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
             'Ilha_principal': 'Na ilha principal, há dez torres de obsidiana com cristais do End no topo, que regeneram a saúde do dragão. O jogador deve destruir os cristais para enfraquecer o dragão e poder atacá-lo. Quando o dragão é derrotado, ele explode e deixa cair muita experiência e um ovo de dragão. O portal de saída é ativado e permite ao jogador voltar ao mundo normal ou explorar as ilhas externas do End, onde há cidades do End e navios do End com tesouros e elytras. O dragão pode ser renascido quantas vezes o jogador quiser, colocando quatro cristais do End ao redor do portal de saída.',
             'Ilhas_externas': 'As ilhas externas do End são lugares misteriosos e isolados que só podem ser acessados após derrotar o dragão do End. Elas são compostas por ilhas flutuantes de variados tamanhos e formas, cobertas por plantas do coro que produzem frutas do coro. Nessas ilhas, o jogador pode encontrar cidades do End, que são estruturas raras e complexas que abrigam shulkers e baús com tesouros. Algumas cidades do End têm navios do End ancorados perto delas, que contêm itens ainda mais valiosos, como elytras e cabeça de dragão.'
         },
         'mobs': {
             # Mobs
             '1':{
                 # Enderman
                 'Enderman': {
                    # Vida
                    'vida': 40,
                    'coracoes': 20,

                    # Informações

                    ## Compotamento
                    'comportamento': 'Neutro',
                    'comportamento_pacifico': 'Neutro',

                    ## Geração
                    'geracao': 'Em todo Fim, com níveis de iluminação 0',

                    ## Dano por vida
                    'dano_por_vida_facil': 4.5,
                    'dano_por_vida_normal': 7,
                    'dano_por_vida_dificil': 10.5,

                    ## Dano por coração
                    'dano_por_coracoes_facil': 2.25,
                    'dano_por_coracoes_normal': 3.5,
                    'dano_por_coracoes_dificil': 5.25,

                    ## Efeito após o dano e duração efeito
                    'dano_efeito': None,
                    'duracao_dano_efeito': None,

                    # Drops
                    'drop1': 'Pérola de ender',
                    'drop2': '5 XP',
                    'drop3': 'Qualquer bloco que está segurando'
                }
            },
             '2':{
                # Shulker
                 'Shulker': {
                    # Vida
                    'vida': 30,
                    'coracoes': 15,

                    # Informações

                    ## Comportamento
                    'comportamento': 'Hostil',
                    'comportamento_pacifico': 'Passivo',

                    ## Geração
                    'geracao': 'Cidade do End',

                    ## Dano por vida
                    'dano_por_vida': 4,

                    ## Dano por corações
                    'dano_por_coracoes': 2,

                    ## Efeito após o dano e duração efeito
                    'dano_efeito': 'Levitação',
                    'duracao_dano_efeito': '10 segundos',

                    # Drops
                    'drop1': 'Casco de shulker',
                    'drop2': '5 XP'     
                 
                }
            },
             '3':{
                # Dragão do Ender
                'Dragão_Ender': {
                    # Vida
                    'vida': 200,
                    'coracoes': 100,

                    # Informações

                    ## Comportamento
                    'comportamento': 'Hostil',
                    'comportamento_pacifico': 'Hostil',

                    ## Geração
                    'geracao': 'O Fim',

                    ## Dano por vida
                    'dano_por_vida_pacifico': 0,
                    'dano_por_vida_facil': 6,
                    'dano_por_vida_normal': 10,
                    'dano_por_vida_dificil': 15,

                    ## Dano por corações
                    'dano_por_coracoes_pacifico': 0,
                    'dano_por_coracoes_facil': 3,
                    'dano_por_coracoes_normal': 5,
                    'dano_por_coracoes_dificil': 7.5,

                    ## Atque especial
                    'ataque_especial': {
                        '1': {
                            'nome': 'Ataque de respiração',
                            'dano_vida': 6,
                            'dano_coracoes': 3, 
                            'duracao': '0,5 segundos'
                        },
                        '2': {
                            'nome': 'Ataque bola de fogo explosiva',
                            'dano_vida': 12,
                            'dano_coracoes': 6, 
                            'duracao': '0,5 segundos'
                        }
                    },

                    ## Efeito após o dano e duração efeito
                    'dano_efeito': None,
                    'duracao_dano_efeito': None,

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
                'Nome': 'A nova geração',
                'Descricao': 'Obtenha o Ovo de Dragão',
                'Requisitos': 'Pegue o ovo de dragão no seu inventário.',
                'ID': 'minecraft:end/dragon_egg'
            },
            '4': {
                'Nome': 'O começo do fim',
                'Descricao': 'Escape da ilha',
                'Requisitos': 'Jogue uma pérola de ender através de uma passagem do End.',
                'ID': 'minecraft:end/enter_end_gateway'
            },
            '5': {
                'Nome': 'Aceita uma pastilha?',
                'Descricao': 'Recolha o bafo do dragão em um frasco de vidro.',
                'Requisitos': 'Pegue uma garrafa de bafo do dragão no seu inventário',
                'ID': 'minecraft:end/dragon_breath'
            },
            '6': {
                'Nome': 'A cidade no fim do jogo',
                'Descricao': 'Entre, o que poderia acontecer?',
                'Requisitos': 'Entre em uma cidade do End.',
                'ID': 'minecraft:end/find_end_city'
            },
            '7': {
                'Nome': 'Ao infinito... e além!',
                'Descricao': 'Encontre os elytras',
                'Requisitos': 'Pegue um par de elytras no seu inventário.',
                'ID': 'minecraft:end/elytra'
            },
            '8': {
                'Nome': 'Ótima vista daqui de cima',
                'Descricao': 'Levite até 50 blocos de altura pelos ataques de um Shulker',
                'Requisitos': 'Tenha o efeito Levitação aplicado, e se mova a uma distância vertical de 50 blocos.',
                'ID': 'minecraft:end/levitate'
            }
        }
    }

# English - Inglês
@app.route('/en')
def en():
    return {
        # Accessing
        'Access': 'To reach the End, the player needs to find a stronghold using eyes of ender and locate the portal room. The room has an End portal with 12 frames, some with eyes already inserted. The player needs to complete the portal with any remaining ender eyes. When activating the portal, a loud sound is emitted and the portal replaces the center blocks with End portal blocks. The player can enter the portal to go to the End, along with other entities that were teleported before.',
        # Environment
        'Environment': {
                        'biomes': {
                            # Biomes
                            '1': 'The End',
                            '2': 'Small End islands',
                            '3': 'End midlands',
                            '4': 'End highlands',
                            '5': 'End barrens',
                        },
                        'generated_structured': {
                            # Generated Structures
                            '1': 'Central island',
                            '2': 'Outer islands',
                            '3': 'End spike',
                            '4': 'Obsidian plataform',
                            '5': 'Exit portal',
                            '6': 'End gateway',
                            '7': 'End city',
                            '8': 'End ship',
                            '9': 'Chorus tree'
                        },
                        'terrain_features': {
                            # Terrain Features
                            'Main_island': 'On the main island, there are ten obsidian towers with Ender crystals on top, which regenerate the dragon\'s health. The player must destroy the crystals to weaken the dragon and be able to attack it. When the dragon is defeated, it explodes and drops a lot of experience and a dragon egg. The exit portal is activated and allows the player to return to the normal world or explore the outer islands of the End, where there are cities of the End and ships of the End with treasure and elytra. The dragon can be respawned as many times as the player wants by placing four Ender crystals around the exit portal.',
                            'Outer_island': 'The outer islands of the End are mysterious and isolated places that can only be accessed after defeating the dragon of the End. They are made up of floating islands of varying sizes and shapes, covered with chorus plants that produce chorus fruits. On these islands, the player can find End Cities, which are rare and complex structures that house shulkers and treasure chests. Some End cities have End ships docked near them, which contain even more valuable items, such as elytra and dragon\'s head.'
                        },
                        'mobs': {
                            # Mobs
                            '1':{
                                # Enderman
                                'Enderman': {
                                # Life
                                'life': 40,
                                'hearts': 20,

                                # Information

                                ## Behavior
                                'behavior': 'Neutral',
                                'behavior_peaceful': 'Neutral',

                                ## Spawn
                                'spawn': 'The End with 0 level light',

                                ## Damage for life
                                'damage_for_life_easy': 4.5,
                                'damage_for_life_normal': 7,
                                'damage_for_life_hard': 10.5,

                                ## Damage for coração
                                'damage_for_hearts_easy': 2.25,
                                'damage_for_hearts_normal': 3.5,
                                'damage_for_hearts_hard': 5.25,

                                ## Effect after a damage and effect duration
                                'damage_effect': None,
                                'duration_damage_effect': None,

                                # Drops
                                'drop1': 'Ender pearl',
                                'drop2': '5 XP',
                                'drop3': 'Any block being held'
                                }
                            },
                            '2':{
                                # Shulker
                                'Shulker': {
                                    # Life
                                    'life': 30,
                                    'hearts': 15,

                                    # Information

                                    ## Behavior
                                    'behavior': 'Hostile',
                                    'behavior_peaceful': 'Passive',

                                    ## Spawn
                                    'spawn': 'End city',

                                    ## Damage for life
                                    'damage_for_life': 4,

                                    ## Damage for hearts
                                    'damage_for_hearts': 2,

                                    ## Effect after a damage and effect duration
                                    'damage_effect': 'Levitation',
                                    'duration_damage_effect': '10 seconds',

                                    # Drops
                                    'drop1': 'Shulker shell',
                                    'drop2': '5 XP'     
                                }
                            },
                            '3':{
                                # Ender Dragon
                                'Ender_Dragon': {
                                    # Life
                                    'life': 200,
                                    'hearts': 100,

                                    # Information

                                    ## Behavior
                                    'behavior': 'Hostile',
                                    'behavior_peaceful': 'Hostile',

                                    ## Spawn
                                    'spawn': 'The End',

                                    ## damage for life
                                    'damage_for_life_peaceful': 0,
                                    'damage_for_life_easy': 6,
                                    'damage_for_life_normal': 10,
                                    'damage_for_life_hard': 15,

                                    ## damage for hearts
                                    'damage_for_hearts_peaceful': 0,
                                    'damage_for_hearts_easy': 3,
                                    'damage_for_hearts_normal': 5,
                                    'damage_for_hearts_hard': 7.5,

                                    ## Special Attack
                                    'special_attack': {
                                    '1': {
                                        'name': 'Dragon\'s Breath',
                                        'damage_life': 3,
                                        'damage_hearts': 1.5, 
                                        'duration': '0,5 segundos'
                                        },
                                    '2': {
                                        'name': 'Dragon Fireball',
                                        'damage_life': 6,
                                        'damage_hearts': 3, 
                                        'duration': '0,5 segundos'
                                        }
                                    },

                                    ## Effect after a damage and effect duration
                                    'damage_effect': None,
                                    'duration_damage_effect': None,

                                    # Drops
                                    'drop1': '12000 XP',
                                    'drop2': 'Dragon egg'

                                }
                            }
                        },
                        'blocks': {
                            # Blocks
                            '1':{
                                # Naturally generated
                                '1': 'Air',
                                '2': 'Bedrock',
                                '3': 'Obsidian',
                                '4': 'End stone',
                                '5': 'Chorus plant',
                                '6': 'Chorus flower'
                            },
                            '2':{
                                # Naturally created
                                '1': 'Air',
                                '2': 'Bedrock',
                                '3': 'Obsidian',
                                '4': 'Wall torch',
                                '5': 'Fire',
                                '6': 'End portal',
                                '7': 'Dragon egg',
                                '8': 'End gateway',
                                '9': 'End crystal',
                                '10': 'Iron bars',
                                '11': 'End stone'
                            },
                            '3':{
                                # Structures
                                '1': 'Air',
                                '2': 'Obsidian',
                                '3': 'Chest',
                                '4': 'Magenta stained Glass',
                                '5': 'Brewing stand',
                                '6': 'Item frame',
                                '7': 'Magenta wall banner',
                                '8': 'End rod',
                                '9': 'Purpur block',
                                '10': 'Purpur pillar',
                                '11': 'Purpur slab',
                                '12': 'Purpur stairs',
                                '13': 'End stone bricks',
                                '14': 'Dragon wall head',
                                '15': 'Ender chest',
                                '16': 'Ladder',
                            }
                        } 
                        },
        # Technical Information
        'Technical_information': {
            # ID
            'ID': {
                'Name': 'The End',
                'ID_JE': 'the_end',
                'Numeric_ID': 1
                }
        },
        # Achievements
        'Achievements': {
            '1': {
                'Name': 'The End?',
                'Description': 'Enter an End Portal'
            },
            '2': {
                'Name': 'The End',
                'Description': 'Kill the Enderdragon'
            },
            '3': {
                'Name': 'You Need a Mint',
                'Description': 'Collect dragons breath in a glass bottle'
            },
            '4': {
                'Name': 'The End... Again...',
                'Description': 'Respawn the Enderdragon'
            },
            '5': {
                'Name': 'Great View From Up Here',
                'Description': 'Levitate up 50 blocks from the attacks of a Shulker'
            }
        }, 
        # Advancements
        'Advancements': {
            '1': {
                'Name': 'The End?',
                'Description': 'Or the beginning?',
                'Requirements': 'Enter the End dimension.',
                'ID': 'minecraft:end/root'
            },
            '2': {
                'Name': 'Free the End',
                'Description': 'Good luck',
                'Requirements': 'Kill the ender dragon. If multiple players are involved in the dragon fight, only the player that deals the final blow to the dragon receives the advancement.',
                'ID': 'minecraft:end/kill_dragon'
            },
            '3': {
                'Name': 'The Next Generation',
                'Description': 'Hold the Dragon Egg',
                'Requirements': 'Have a dragon egg in your inventory.',
                'ID': 'minecraft:end/dragon_egg'
            },
            '4': {
                'Name': 'Remote Getaway',
                'Description': 'Escape the island',
                'Requirements': 'Throw an ender pearl through, fly, or walk into an end gateway.',
                'ID': 'minecraft:end/enter_end_gateway'
            },
            '5': {
                'Name': 'The End... Again...',
                'Description': 'Respawn the Ender Dragon',
                'Requirements': 'Be in a certain radius from the exit portal when an ender dragon is summoned using end crystals.',
                'ID': 'minecraft:end/respawn_dragon'
            },
            '6': {
                'Name': 'You Need a Mint',
                'Description': 'Collect dragon\'s breath in a glass bottle',
                'Requirements': 'Have a bottle of dragon\'s breath in your inventory.',
                'ID': 'minecarft:end/dragon_breath'
            },
            '7': {
                'Name': 'The City at the End of the Game',
                'Description': 'Go on in, what could happen?',
                'Requirements': 'Enter an end city.',
                'ID': 'minecraft:end/find_end_city'
            },
            '8': {
                'Name': 'Sky\'s the Limit',
                'Description': 'Find elytra',
                'Requirements': 'Have a pair of elytra in your inventory.',
                'ID': 'minecraft:end/elytra'
            },
            '9': {
                'Name': 'Great View From Up Here',
                'Description': 'Levitate up 50 blocks from the attacks of a Shulker',
                'Requirements': 'Move a distance of 50 blocks vertically with the Levitation effect applied, regardless of direction or whether it is caused by the effect.',
                'ID': 'minecraft:end/levitate'
            }
        }
        
    }

# Start a API - Inicia a API
if __name__ == '__main__':
    app.run(debug=True)