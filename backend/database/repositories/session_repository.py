from database.connection import get_connection


class SessionRepository:
    def __init__(self):
        self.conexao = get_connection()
        self.cursor = self.conexao.cursor()

    def insert(self, session_user_id):
        sql = "INSERT INTO `session` (session_user_id) VALUES (%s)"
        self.cursor.execute(sql, (session_user_id,))
        self.conexao.commit()

    def get_by_id(self, session_id):
        sql = """
        SELECT id, created_at, updated_at, session_user_id
        FROM `session`
        WHERE id = %s
        """
        self.cursor.execute(sql, (session_id,))
        return self.cursor.fetchone()

    def get_by_user_id(self, user_id):
        sql = """
        SELECT id, created_at, updated_at, session_user_id
        FROM `session`
        WHERE session_user_id = %s
        """
        self.cursor.execute(sql, (user_id,))
        return self.cursor.fetchall()

    def get_all(self):
        sql = "SELECT id, created_at, updated_at, session_user_id FROM `session`"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update_user(self, session_id, new_user_id):
        sql = """
        UPDATE `session`
        SET session_user_id = %s
        WHERE id = %s
        """
        self.cursor.execute(sql, (new_user_id, session_id))
        self.conexao.commit()

    def delete(self, session_id):
        sql = "DELETE FROM `session` WHERE id = %s"
        self.cursor.execute(sql, (session_id,))
        self.conexao.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()
            
