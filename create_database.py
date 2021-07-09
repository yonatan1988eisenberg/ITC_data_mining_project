import csv
import pymysql

# Make Connection
conn = pymysql.connect(host='localhost', user='root',
                       password='Weasil123', cursorclass=pymysql.cursors.DictCursor)  # give ur username, password

# Make Cursos
cursor = conn.cursor()

# Create Database
cursor.execute("CREATE DATABASE IF NOT EXISTS trial_1")

# Use Database
cursor.execute('USE trial_1')

list_of_tables = [
    'CREATE TABLE IF NOT EXISTS Publisher (Publisher_id int AUTO_INCREMENT PRIMARY KEY, Publisher_name varchar(250), UNIQUE (Publisher_name))',
    'CREATE TABLE IF NOT EXISTS Developer (Developer_id int AUTO_INCREMENT PRIMARY KEY, Developer_name varchar(250), UNIQUE (Developer_name))',
    'CREATE TABLE IF NOT EXISTS Age_Rating (Age_Rating_id int AUTO_INCREMENT PRIMARY KEY, Age_Rating_name varchar(250), UNIQUE (Age_Rating_name))',
    'CREATE TABLE IF NOT EXISTS Consoles (Console_id int AUTO_INCREMENT PRIMARY KEY, Console_name varchar(250), UNIQUE (Console_name))',
    'CREATE TABLE IF NOT EXISTS Genre (Genre_id int AUTO_INCREMENT PRIMARY KEY, Genre_name varchar(250), UNIQUE (Genre_name))',
    '''
    CREATE TABLE IF NOT EXISTS Game(Game_id int AUTO_INCREMENT PRIMARY KEY, Game_name varchar(250) UNIQUE, Publisher_id int,
    Developer_id int, Age_rating_id int, num_players varchar(250), Release_date varchar(250), FOREIGN KEY(Publisher_id) REFERENCES Publisher(Publisher_id),
    FOREIGN KEY(Developer_id) REFERENCES Developer(Developer_id), FOREIGN KEY(Age_rating_id) REFERENCES Age_Rating(Age_Rating_id))
    ''',
    '''
    CREATE TABLE IF NOT EXISTS game_to_console
    ( Game_id INT NOT NULL references Console(Console_id), Console_id INT NOT NULL references Game(Game_id),
    PRIMARY KEY(Game_id, Console_id))''',
    '''
    CREATE TABLE IF NOT EXISTS Main_Scores(
    Game_id int, Console_id int, Metascore int, Userscore float, Num_Metascore int, num_Userscore int, FOREIGN KEY(Game_id) REFERENCES Game(Game_id),
    FOREIGN KEY(Console_id) REFERENCES Consoles(Console_id)) ''',
    '''
    CREATE TABLE IF NOT EXISTS PMN_user_scores(
    Game_id int, Num_positive int, Num_mixed int, Num_negative int, FOREIGN KEY(Game_id) REFERENCES Game(Game_id))''',
    '''
    CREATE TABLE IF NOT EXISTS PMN_critic_scores(
    Game_id int, Num_positive int, Num_mixed int, Num_negative int,FOREIGN KEY(Game_id) REFERENCES Game(Game_id))
    ''']
# Create Tables
for i in range(len(list_of_tables)):
    cursor.execute(list_of_tables[i])

# List of Insert Commands
list_of_inserts = [ 'INSERT INTO Publisher (Publisher_name) VALUE (%s)',
                    'INSERT INTO Developer (Developer_name) VALUE (%s)',
                    'INSERT INTO Age_rating (Age_Rating_name) VALUE (%s)',
                    'INSERT INTO Consoles (Console_name) VALUE (%s)',
                    'INSERT INTO Genre (Genre_name) VALUE (%s)',
                    'SELECT Publisher_id FROM Publisher WHERE Publisher_name = %s',
                    'SELECT Developer_id FROM Developer WHERE Developer_name = %s',
                    'SELECT Age_Rating_id FROM Age_rating WHERE Age_Rating_name = %s',
                    'INSERT INTO Game (Game_name, Publisher_id, Developer_id, Age_rating_id, num_players, Release_date) VALUE (%s,%s, %s,%s, %s, %s)',
                    'SELECT Console_id From Consoles WHERE Console_name = %s',
                    'INSERT INTO game_to_console (Game_id, Console_id) Value (%s,%s)',
                    'INSERT INTO main_scores (Game_id, Console_id, Metascore, Userscore, Num_Metascore, num_Userscore) VALUE (%s,%s,%s,%s,%s,%s)',
                    'INSERT INTO PMN_user_scores (Game_id, Num_positive, Num_mixed, Num_negative) VALUES (%s,%s,%s,%s)',
                    'INSERT INTO PMN_critic_scores (Game_id, Num_positive, Num_mixed, Num_negative) VALUES (%s,%s,%s,%s)'
                    ]

# Insert Values
with open('db_2.csv') as csvfile:
    reader = csv.DictReader(csvfile, delimiter=',')

    #Insert Value into Publisher,Developer and Age_rating tables
    for row in reader:
        list_of_paramaters = [(row['publisher'],), (row['developer'],),(row['age rating'],), (row['main platform'],) ]
        console_id_list = []
        console_id_list.append(row['main platform'])
        for i in range(4):
            try:
                cursor.execute(list_of_inserts[i], list_of_paramaters[i] )
            except Exception as e:
                pass

        #Insert values into COnsoles and Genres
        list_of_paramaters_two = [row['Other Consoles'],row['Genres']]
        for j in range(3,5):
            for k in list_of_paramaters_two[j-3].split(','):
                console_id_list.append(k.strip("']['"))
                try:
                    cursor.execute(list_of_inserts[j], (k.strip("'][' '"),))
                except:
                    pass

        #Fetch id of Publisher,Developer and Age_rating
        save_fetch = []
        for i in range(3):
            cursor.execute(list_of_inserts[i+5], list_of_paramaters[i])
            save_fetch.append(cursor.fetchone())


        #Insert into Game
        try:
            cursor.execute('INSERT INTO Game (Game_name, Publisher_id, Developer_id, Age_rating_id, num_players, Release_date) VALUE (%s,%s, %s,%s, %s, %s)', (
                row['name of game'], save_fetch[0]['Publisher_id'], save_fetch[1]['Developer_id'], save_fetch[2]['Age_Rating_id'],
                row['num players'], row['release date']))
            g_id = cursor.lastrowid
        except Exception as e:
            pass

        #Insert into game_to_Console table
        try:
            for i in console_id_list:
                cursor.execute(list_of_inserts[9], i)
                Console_id_fetch = cursor.fetchone()
                cursor.execute(list_of_inserts[10], (g_id,Console_id_fetch['Console_id'])
                )
        except:
            pass

        #Insert Values into main_scores
        try:
            cursor.execute('SELECT Console_id From Consoles WHERE Console_name = %s', row['main platform'])
            Console_id_fetch = cursor.fetchone()
            cursor.execute(list_of_inserts[11], (g_id, Console_id_fetch['Console_id'], row['metascore'], row['user score'],
                                row['number of metascore reviewers'], row['number of user reviews']))
        except:
            pass

        #Insert Values into PMN_user_table
        try:
            cursor.execute(list_of_inserts[12],
                           (g_id, row['user review positive'], row['user review mixed'], row['user review negative']))
        except:
            pass

        #Insert values into PMN_critic_table
        try:
            cursor.execute(list_of_inserts[13], (
            g_id, row['critic review_positive'], row['critic review mixed'], row['critic review negative']))
        except:
            pass

    conn.commit()
