from mariadb import connect
from mariadb.connections import Connection
from config import settings

def _get_connection() -> Connection:
    return connect(
        host=settings.host,
        user=settings.user,
        password=settings.password,
        port=settings.port,
        database=settings.database
    )


def insert_query(sql: str, sql_params=()):
    with _get_connection() as conn:
        cursor = conn.cursor()
        cursor.execute(sql, (sql_params))
        conn.commit()

        return cursor.lastrowid
