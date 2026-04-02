from database.connection import get_connection


class UserRepository:
    def __init__(self):
        self.conexao = get_connection()
        self.cursor = self.conexao.cursor()

    def insert(self, name, password):
        sql = "INSERT INTO `user` (name, password) VALUES (%s, %s)"
        self.cursor.execute(sql, (name, password))
        self.conexao.commit()
 
    def get_by_name(self, name):
        sql = "SELECT id, name, password FROM `user` WHERE name = %s"
        self.cursor.execute(sql, (name,))
        return self.cursor.fetchone()

    def get_by_id(self, user_id):
        sql = "SELECT id, name, password FROM `user` WHERE id = %s"
        self.cursor.execute(sql, (user_id,))
        return self.cursor.fetchone()

    def get_all(self):
        sql = "SELECT id, name, password FROM `user`"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update_name(self, user_id, new_name):
        sql = "UPDATE `user` SET name = %s WHERE id = %s"
        self.cursor.execute(sql, (new_name, user_id))
        self.conexao.commit()

    def update_password(self, user_id, new_password):
        sql = "UPDATE `user` SET password = %s WHERE id = %s"
        self.cursor.execute(sql, (new_password, user_id))
        self.conexao.commit()

    def delete(self, user_id):
        sql = "DELETE FROM `user` WHERE id = %s"
        self.cursor.execute(sql, (user_id,))
        self.conexao.commit()

    def close(self):
        if self.cursor:
            self.cursor.close()
        if self.conexao:
            self.conexao.close()