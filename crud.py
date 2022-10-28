from datetime import date

from db_connection import conn


def init_prefix_table():
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS prefix;

        CREATE TABLE prefix AS SELECT
        *,
        0 as times,
        cast(null as date) as last_day
        FROM generate_series(1, 80) as vocabulary_index;
    """)
    conn.commit()
    cursor.close()


def init_root_table():
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS root;

        CREATE TABLE root AS SELECT
        *,
        0 as times,
        cast(null as date) as last_day
        FROM generate_series(1, 138) as vocabulary_index;
    """)
    conn.commit()
    cursor.close()


def init_suffix_table():
    cursor = conn.cursor()
    cursor.execute("""
        DROP TABLE IF EXISTS suffix;

        CREATE TABLE suffix AS SELECT
        *,
        0 as times,
        cast(null as date) as last_day
        FROM generate_series(1, 80) as vocabulary_index;
    """)
    conn.commit()
    cursor.close()


def select_vocabularies(type, times):
    cursor = conn.cursor()
    cursor.execute(f"""
            SELECT vocabulary_index
            FROM {type}
            WHERE times = {times};
        """)
    res = cursor.fetchall()
    cursor.close()
    return res


def update_times(type, index, times):
    cursor = conn.cursor()
    cursor.execute(f"""
        UPDATE {type}
        SET times = {times}, last_day = '{date.today()}'
        WHERE vocabulary_index = {index};
    """)
    conn.commit()
    cursor.close()
