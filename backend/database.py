# TODO: conexão com o banco de dados (ex.: MySQL)
#
# - Conexão: usar variáveis de ambiente (MYSQL_HOST, MYSQL_PORT, MYSQL_USER, MYSQL_PASSWORD, MYSQL_DATABASE)
# - init_db(): criar tabelas (sessions, messages com session_id, role, content)
# - get_history(session_id): buscar mensagens da sessão ordenadas por id
# - save_message(session_id, role, content): inserir mensagem (role = 'user' ou 'assistant')
# - ensure_session(session_id): garantir que a sessão existe antes de ler/escrever mensagens


def init_db():
    pass


def get_history(session_id: int):
    return []


def save_message(session_id: int, role: str, content: str):
    pass
