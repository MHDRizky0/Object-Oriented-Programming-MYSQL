from Connection import Connection
# from nama_file import nama_class

class ModelRam:

	__connection = Connection()
	__db = __connection.open()

	def insertRam(self, data):
		cursor = self.__db.cursor()

		sql = """INSERT INTO Ram (id_ram, kapasitas, kecepatan_ram) VALUES (%s, %s, %s)"""
		val = (data['id_ram'], data['kapasitas'], data['kecepatan_ram'])
		
		cursor.execute(sql, val)
		cursor.close()
		self.__db.commit()

		print("{} record inserted".format(cursor.rowcount))

	def selectAllRam(self):
		cursor = self.__db.cursor()

		sql = """SELECT * FROM Ram"""
		
		cursor.execute(sql)
		results = cursor.fetchall()
		cursor.close()

		return results

	def selectRam(self, id_ram):
		cursor = self.__db.cursor()

		sql = """SELECT * FROM Ram WHERE id_ram = %s"""
		val = (id_ram,)
		
		cursor.execute(sql, val)
		results = cursor.fetchall()
		cursor.close()

		return results

	def updateRam(self, id_ram, kapasitas, kecepatan_ram):
		cursor = self.__db.cursor()

		sql = """UPDATE Ram SET kapasitas=%s, kecepatan_ram=%s WHERE id_ram=%s"""
		val = (kapasitas, kecepatan_ram, id_ram)
		
		cursor.execute(sql, val)
		cursor.close()
		self.__db.commit()
		
		print("{} record updated".format(cursor.rowcount))

	def deleteRam(self, id_ram):
		cursor = self.__db.cursor()

		sql = """DELETE FROM Ram WHERE id_ram = %s"""
		val = (id_ram,)
		
		cursor.execute(sql, val)
		cursor.close()
		self.__db.commit()

		print("{} record removed".format(cursor.rowcount))