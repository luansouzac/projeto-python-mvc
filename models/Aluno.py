from db.db_connection import get_db_connection

class Aluno:
    def __init__(self, nome, matricula):
        self.nome = nome
        self.matricula = matricula

    @staticmethod
    def criar(nome, matricula):
        db = get_db_connection()
        if db is None:
            return None
        
        cursor = db.cursor()

        query = "INSERT INTO alunos (nome, matricula) VALUES (%s, %s)"
        try:
            cursor.execute(query, (nome, matricula))
            db.commit()
            return cursor.lastrowid
        except Exception as e:
            db.rollback()
            print(f"Erro ao criar aluno {e}")
        finally:
            cursor.close()
            db.close()

    @staticmethod
    def procurar_por_nome(nome):
        db = get_db_connection()
        if db is None:
            return None
        
        cursor = db.cursor(dictionary=True)

        query = "SELECT * FROM alunos WHERE nome = %s"
        aluno_encontrado = None

        try:
            cursor.execute(query, (nome,))
            aluno_encontrado = cursor.fetchone()
        except Exception as e:
            print(f"Erro ao procurar aluno: {e}")
        finally:
            cursor.close()
            db.close()

        return aluno_encontrado


        


    
