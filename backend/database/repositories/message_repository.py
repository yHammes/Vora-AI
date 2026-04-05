from database.connection import get_connection


class MessageRepository:
    def __init__(self):
        self.conexao = get_connection()
        self.cursor = self.conexao.cursor()

    def insert(self, role, content, session_id):
        sql = """
        INSERT INTO `message` (role, content, session_id)
        VALUES (%s, %s, %s)
        """
        self.cursor.execute(sql, (role, content, session_id))
        self.conexao.commit()

    def get_by_id(self, message_id):
        sql = """
        SELECT id, role, content, created_at, update_at, session_id
        FROM `message`
        WHERE id = %s
        """
        self.cursor.execute(sql, (message_id,))
        return self.cursor.fetchone()

    def get_messages_by_session_id(self, session_id):
        sql = """
        SELECT role, content
        FROM `message`
        WHERE session_id = %s
        ORDER BY created_at ASC
        """
        self.cursor.execute(sql, (session_id,))
        return self.cursor.fetchall()

    def get_all(self):
        sql = """
        SELECT id, role, content, created_at, update_at, session_id
        FROM `message`
        """
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update_content(self, message_id, new_content):
        sql = """
        UPDATE `message`
        SET content = %s
        WHERE id = %s
        """
        self.cursor.execute(sql, (new_content, message_id))
        self.conexao.commit()

    def delete(self, message_id):
        sql = "DELETE FROM `message` WHERE id = %s"
        self.cursor.execute(sql, (message_id,))
        self.conexao.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()
