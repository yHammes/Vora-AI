from dotenv import load_dotenv
import os
import mysql.connector

print("CONNECTION CERTO")


def get_connection():
    load_dotenv()

    conexao = mysql.connector.connect(
        host=os.getenv("DATABASE_IP"),
        user=os.getenv("DATABASE_LOGIN"),
        password=os.getenv("DATABASE_PASSWORD"),
        database=os.getenv("DATABASE_HOST"),
        port=3306
    )

    return conexao