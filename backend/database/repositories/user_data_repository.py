from dataclasses import fields
from database.connection import get_connection


class UserDataRepository:
    def __init__(self):
        self.conexao = get_connection()
        self.cursor = self.conexao.cursor()

    def insert(self, birth_date, height, weight, sex, user_id):
        sql = """
        INSERT INTO user_data (birth_date, height, weight, sex, user_id)
        VALUES (%s, %s, %s, %s, %s)
        """
        values = (birth_date, height, weight, sex, user_id)

        self.cursor.execute(sql, values)
        self.conexao.commit()

    def get_by_id(self, user_data_id):
        sql = """
        SELECT id, birth_date, height, weight, sex, user_id, created_at, updated_at
        FROM user_data
        WHERE id = %s
        """
        self.cursor.execute(sql, (user_data_id,))
        return self.cursor.fetchone()

    def get_by_user_id(self, user_id):
        sql = """
        SELECT id, birth_date, height, weight, sex, user_id, created_at, updated_at
        FROM user_data
        WHERE user_id = %s
        """
        self.cursor.execute(sql, (user_id,))
        return self.cursor.fetchone()

    def get_all(self):
        sql = "SELECT * FROM user_data"
        self.cursor.execute(sql)
        return self.cursor.fetchall()

    def update(self, user_data_id, birth_date =None, height =None, weight=None, sex=None):
        fields = []
        values = []
        
        if birth_date is not None:
            fields.append("birth_date = %s")
            values.append(birth_date)
            
        if height is not None:
            fields.append("height = %s")
            values.append(height)
            
        if weight is not None:
            fields.append("weight = %s")
            values.append(weight)
            
        if sex is not None:
            fields.append("sex = %s")
            values.append(sex)
            
        if not fields:
            print("Nenhum campo para atualizar")
            return
        
        sql = f"""
        UPDATE user_data
        set {", ".join(fields)}
        WHERE id = %s
        """
        
        values.append(user_data_id)
        
        self.cursor.execute(sql, tuple(values))
        self.conexao.commit()

    def delete(self, user_data_id):
        sql = "DELETE FROM user_data WHERE id = %s"
        self.cursor.execute(sql, (user_data_id,))
        self.conexao.commit()

    def close(self):
        self.cursor.close()
        self.conexao.close()