from Connection import Connection
# from nama_file import nama_class

class ModelProsessor:

	__connection = Connection()
	__db = __connection.open()

	def insertProsessor(self, data):
		cursor = self.__db.cursor()

		sql = """INSERT INTO Prosessor (id_prosessor, core, kecepatan) VALUES (%s, %s, %s)"""
		val = (data['id_prosessor'], data['core'], data['kecepatan'])
		
		cursor.execute(sql, val)
		cursor.close()
		self.__db.commit()

		print("{} record inserted".format(cursor.rowcount))

	def selectAllProsessor(self):
		cursor = self.__db.cursor()

		sql = """SELECT * FROM Prosessor"""
		
		cursor.execute(sql)
		results = cursor.fetchall()
		cursor.close()

		return results

	def selectProsessor(self, id_prosessor):
		cursor = self.__db.cursor()

		sql = """SELECT * FROM Prosessor WHERE id_prosessor = %s"""
		val = (id_prosessor,)
		
		cursor.execute(sql, val)
		results = cursor.fetchall()
		cursor.close()

		return results

	def updateProsessor(self, id_prosessor, core, kecepatan):
		cursor = self.__db.cursor()

		sql = """UPDATE Prosessor SET core=%s, kecepatan=%s WHERE id_prosessor=%s"""
		val = (core, kecepatan, id_prosessor)
		
		cursor.execute(sql, val)
		cursor.close()
		self.__db.commit()
		
		print("{} record updated".format(cursor.rowcount))

	def deleteProsessor(self, id_prosessor):
		cursor = self.__db.cursor()

		sql = """DELETE FROM Prosessor WHERE id_prosessor = %s"""
		val = (id_prosessor,)
		
		cursor.execute(sql, val)
		cursor.close()
		self.__db.commit()

		print("{} record removed".format(cursor.rowcount))