import mysql.connector

def get_db_connection():
    try:
        conn = mysql.connector.connect(
            host = 'localhost',
            user = 'root',
            password = '',
            database = 'projeto_faculdade'
        )

        if conn is None:
            print('Erro de conexão com o banco')
            return None

        return conn
    except mysql.connector.Error as err:
        print(f'Erro de conexão com o banco de dados: {err}')
        return None