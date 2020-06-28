from Connection import Connection
# from nama_file import nama_class

class ModelMobo:

	__connection = Connection()
	__db = __connection.open()

	def insertMobo(self, data):
		cursor = self.__db.cursor()

		sql = """INSERT INTO Mobo (id_mobo, jumlah_slot_memory, jumlah_slot_harddisk) VALUES (%s, %s, %s)"""
		val = (data['id_mobo'], data['jumlah_slot_memory'], data['jumlah_slot_harddisk'])
		
		cursor.execute(sql, val)
		cursor.close()
		self.__db.commit()

		print("{} record inserted".format(cursor.rowcount))

	def selectAllMobo(self):
		cursor = self.__db.cursor()

		sql = """SELECT * FROM Mobo"""
		
		cursor.execute(sql)
		results = cursor.fetchall()
		cursor.close()

		return results

	def selectMobo(self, id_Mobo):
		cursor = self.__db.cursor()

		sql = """SELECT * FROM Mobo WHERE id_Mobo = %s"""
		val = (id_Mobo,)
		
		cursor.execute(sql, val)
		results = cursor.fetchall()
		cursor.close()

		return results

	def updateMobo(self, id_Mobo, jumlah_slot_memory, jumlah_slot_harddisk):
		cursor = self.__db.cursor()

		sql = """UPDATE Mobo SET jumlah_slot_memory=%s, jumlah_slot_harddisk=%s WHERE id_Mobo=%s"""
		val = (jumlah_slot_memory, jumlah_slot_harddisk, id_Mobo)
		
		cursor.execute(sql, val)
		cursor.close()
		self.__db.commit()
		
		print("{} record updated".format(cursor.rowcount))

	def deleteMobo(self, id_Mobo):
		cursor = self.__db.cursor()

		sql = """DELETE FROM Mobo WHERE id_Mobo = %s"""
		val = (id_Mobo,)
		
		cursor.execute(sql, val)
		cursor.close()
		self.__db.commit()

		print("{} record removed".format(cursor.rowcount))