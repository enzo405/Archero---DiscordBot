import psycopg2
import psycopg2.extensions

class DatabaseHandler():
	def __init__(self):
		self.connect = psycopg2.connect(database ="d2gm319ojamf98" , user = "wiycckcyrozefh", password = "1d6e3b493a710e19a35a695cd1640b31e5abf38cf2dfb4487a1d86d8c011a707", host = "ec2-54-228-32-29.eu-west-1.compute.amazonaws.com", port = "5432")
		query1 ="DROP TABLE Stats" 
		query = f"CREATE TABLE IF NOT EXISTS Stats(id BIGINT NOT NULL,username VARCHAR(33) NOT NULL,attaque INTEGER NOT NULL,pv INTEGER NOT NULL, F2P VARCHAR(8), ChapterNm INTEGER, ChapterHm INTEGER);"
		cur = self.connect.cursor()
		cur.execute(query)
		self.connect.commit()

	def create_person(self, id: int,name: str, attaque: int, pv: int):
		cursor = self.connect.cursor()
		query = f"INSERT INTO Stats (id, username, attaque, pv) VALUES ({id}, '{name}' ,{attaque} , {pv});"
		cursor.execute(query)
		self.connect.commit()
		print("User a bien été créer")

	def free_to_play(self, id: int, f2p):
		cursor = self.connect.cursor()
		query = f"UPDATE Stats SET F2P = '{f2p}' WHERE id = {id};"
		cursor.execute(query)
		self.connect.commit()
		print("User a bien été asigné en tant que F2P")

	def set_chapter(self, id: int, nm: int, hm: int):
		cursor = self.connect.cursor()
		query = f"UPDATE Stats SET ChapterNm = {nm}, ChapterHm = {hm} WHERE id = {id};"
		cursor.execute(query)
		self.connect.commit()
		print("Les chapitres des Users ont bien été assigné")

	def change_stats(self, id:int ,name : str, attaque : int, pv : int):
		cursor = self.connect.cursor()
		query = f"UPDATE Stats SET attaque = {attaque} , pv = {pv} , username = '{name}' WHERE id = {id};"
		cursor.execute(query)
		cursor.close()
		self.connect.commit()
		print("Les stats ont bien été changé")

	def delete_person(self, id: int):
		cursor = self.connect.cursor()
		query = f"DELETE FROM Stats WHERE id={id};"
		cursor.execute(query)
		self.connect.commit()
		print("Les stats ont bien été supprimé")

	def column(self, command, *values):
		cursor = self.connect.cursor()
		cursor.execute(command, tuple(values))
		return [item[0] for item in cursor.fetchall()]