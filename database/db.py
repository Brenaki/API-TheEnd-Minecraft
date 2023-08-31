import sqlite3
import time

def connection_DB():
    conn = sqlite3.connect('./database/database.db')
    return conn

def create_tables():
    conn = connection_DB()
    conn.execute('''CREATE TABLE Access
                 (
                 id_acc INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                 description TEXT NOT NULL
                 );
                 ''')
    conn.execute('''CREATE TABLE Environment(
                 id_en INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                 name VARCHAR(255) NOT NULL
                 );
                ''')
    conn.execute('''CREATE TABLE biomes(
                 id_bio INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL
                 );''')
    conn.execute('''CREATE TABLE generated_structured(
                 id_struct INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                 name VARCHAR(255) NOT NULL
                );''')
    conn.execute('''CREATE TABLE terrain_features(
                id_features INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL,
                description TEXT NOT NULL 
                );''')
    conn.execute('''CREATE TABLE mob(
                id_mob INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL,
                life INTEGER,
                health INTEGER,
                behavior TEXT NOT NULL,
                behavior_peaceful TEXT,
                spawn TEXT NOT NULL,
                drop_0 TEXT NOT NULL,
                drop_1 TEXT NOT NULL,
                drop_2 TEXT NOT NULL,              
                );''')
    conn.execute('''CREATE TABLE damage_mob(
                id_damage INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                damage_for_life_peaceful INTEGER,
                damage_for_life_easy INTEGER,
                damage_for_life_normal INTEGER NOT NULL,
                damage_for_life_hard INTEGER,
                damage_for_hearts_peaceful INTEGER,
                damage_for_hearts_easy INTEGER,
                damage_for_hearts_normal INTEGER NOT NULL,          
                damage_for_hearts_hard INTEGER
                );''')
    conn.execute('''CREATE TABLE special_attack(
                id_special_attack INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL,
                damage_life INTEGER NOT NULL,
                damage_heart INTEGER NOT NULL,
                duration INTEGER,
                );''')
    conn.execute('''CREATE TABLE blocks(
                id_category INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL
                );''')
    conn.execute('''CREATE TABLE naturally_generated(
                id_generated INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL
                );''')
    conn.execute('''CREATE TABLE naturally_created(
                id_created INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL
                );''')
    conn.execute('''CREATE TABLE structures(
                id_structs INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL
                );''')
    conn.execute('''CREATE TABLE Technical_information(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL,
                id_JE TEXT NOT NULL,
                numeric_id INTEGER NOT NULL
                );''')
    conn.execute('''CREATE TABLE Achievements(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL,
                description TEXT NOT NULL
                );''')
    conn.execute('''CREATE TABLE Advancements(
                id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
                name VARCHAR(255) NOT NULL,
                description VARCHAR(255),
                Requirements VARCHAR(255) NOT NULL,
                id_mine VARCHAR(255) NOT NULL
                );''')
    print('Created tables')
    conn.close()
def drop_tables():
    conn = connection_DB()
    conn.execute('''DROP TABLE Access''')
    conn.execute('''DROP TABLE Environment''')
    conn.execute('''DROP TABLE biomes''')
    print('Droped tables')
    conn.close()

drop_tables()
create_tables()
time.sleep(10)
drop_tables()