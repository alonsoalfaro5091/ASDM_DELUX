import sqlite3

def obtain_data(table_name, question_id):

	if table_name == 	 'PRIMERO_MEDIO':	column_name_id = 'id_question_pr'
	elif table_name == 'SEGUNDO_MEDIO':	column_name_id = 'id_question_sg'
	elif table_name == 'TERCERO_MEDIO':	column_name_id = 'id_question_trc'
	elif table_name == 'CUARTO_MEDIO':	column_name_id = 'id_question_cr'

	conn = sqlite3.connect('BASE_ASMD.db')
	cursor = conn.cursor()

	query = f"SELECT * FROM {table_name} WHERE {column_name_id} = ? "
	
	cursor.execute(query, (question_id,)) 
	data = cursor.fetchone()
	conn.close()
	return data


def max_id():
  conn = sqlite3.connect('BASE_ASMD.db')
  cursor =  conn.cursor()

  cursor.execute("SELECT MAX(id_pl) FROM PLAYER")
  
  max = cursor.fetchone()

  conn.close()
  
  if max and max[0] is not None: max_id=max[0]
  else: max_id=0
  
  return max_id
  

def insert_player(name, score):
	new_id = max_id() + 1

	player_data = (new_id, name, score)

	conn = sqlite3.connect("BASE_ASMD.db")
	cursor = conn.cursor()

	sql_insert = "INSERT INTO PLAYER (id_pl, name_pl, score_pl) VAlUES (?, ?, ?)"

	cursor.execute(sql_insert, player_data)
	conn.commit()

	print(f"Jugador {name} insertado en el ID {new_id} con {score} puntos.")

	conn.close()


def show_player():
	conn = sqlite3.connect('BASE_ASMD.db')
	cursor = conn.cursor()

	query = "SELECT name_pl, score_pl FROM PLAYER ORDER BY score_pl DESC"

	cursor.execute(query)

	player_data=cursor.fetchall()

	conn.close()

	name=[data[0] for data in player_data]
	score=[data[1] for data in player_data]

	return name, score