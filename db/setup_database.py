import mysql.connector
from mysql.connector import errorcode

DB_NAME = 'projeto_faculdade'

try:

    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
    )
    cursor = db.cursor()

    cursor.execute(f"CREATE DATABASE IF NOT EXISTS {DB_NAME} DEFAULT CHARACTER SET 'utf8'")
    print(f"Banco de dados '{DB_NAME}' criado ou já existente.")

    cursor.close()
    db.close()


except mysql.connector.Error as err:
    print('Erro ao criar o banco de dados: {err}')
    exit(1)

try:
    db = mysql.connector.connect(
        host = 'localhost',
        user = 'root',
        password = '',
        database = DB_NAME
    )

    cursor = db.cursor()

    TABLES = {}
    TABLES['alunos'] = (
        "CREATE TABLE IF NOT EXISTS `alunos` ("
        "  `id` int(11) NOT NULL AUTO_INCREMENT,"
        "  `nome` varchar(100) NOT NULL,"
        "  `matricula` varchar(20) NOT NULL UNIQUE,"
        "  PRIMARY KEY (`id`)"
        ") ENGINE=InnoDB"
    )

    for table_name in TABLES:
        table_description = TABLES[table_name]
        try:
            print(f'Criando tabela {table_name}')
            cursor.execute(table_description)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                print("já existe.")
            else:
                print(err.msg)
        else:
            print("OK")

except mysql.connector.Error as err:
    print(f"Erro ao configurar as tabelas: {err}")
