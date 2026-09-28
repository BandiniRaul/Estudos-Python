import sqlite3

conn = sqlite3.connect('escola.db')
cursor = conn.cursor()

# cursor.execute( 
#     """
#         SELECT * FROM estudantes
#     """
# )

cursor.execute( 
    """
        SELECT * FROM disciplinas
    """
)

conn.commit()

disciplinas = cursor.fetchall()

for disciplina in disciplinas:
    print(disciplina)

# estudantes = cursor.fetchall()

# for estudante in estudantes:
#     print(estudante)

conn.close()
