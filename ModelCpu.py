import pymysql
from Connection import Connection
from ModelRam import ModelRam
from ModelProsessor import ModelProsessor
from ModelMobo import ModelMobo

class ModelCpu:
	__connection = Connection()
	__db = __connection.open()


	def addCpu(self, data):
		cursor = self.__db.cursor()

		sql = """INSERT INTO Cpu (id_cpu, warna, id_ram, id_mobo, id_prosessor) VALUES (%s, %s, %s, %s, %s)"""
		val = (data['id_cpu'], data['warna'], data['id_ram'], data['id_mobo'], data['id_prosessor'])
		
		cursor.execute(sql, val)
		cursor.close()
		self.__db.commit()

		ModelProsessor.insertProsessor(ModelProsessor(), data)
		ModelMobo.insertMobo(ModelMobo(), data)
		ModelRam.insertRam(ModelRam(), data)

		print("berhasil")

	def getCpuById(self, id_cpu):
		cursor = self.__db.cursor(pymysql.cursors.DictCursor)

		sql = """SELECT a.id_cpu, a.warna, b.kapasitas, b.kecepatan_ram, c.jumlah_slot_memory, c.jumlah_slot_harddisk, d.core, d.kecepatan
				FROM Cpu a, ram b, mobo c, prosessor d
				WHERE a.id_ram = b.id_ram and a.id_mobo = c.id_mobo and a.id_prosessor = d.id_prosessor and a.id_cpu = %s"""

		val = (id_cpu,)
		
		cursor.execute(sql, val)
		results = cursor.fetchall()
		cursor.close()

		return results

	def getAllCpu(self):
		cursor = self.__db.cursor(pymysql.cursors.DictCursor)

		sql = """SELECT a.id_cpu, a.warna, b.kapasitas, b.kecepatan_ram, c.jumlah_slot_memory, c.jumlah_slot_harddisk, d.core, d.kecepatan
				FROM Cpu a, ram b, mobo c, prosessor d
				WHERE a.id_ram = b.id_ram and a.id_mobo = c.id_mobo and a.id_prosessor = d.id_prosessor"""

		
		cursor.execute(sql)
		results = cursor.fetchall()
		cursor.close()

		return results

	def deleteById(self, id_cpu):
		cursor = self.__db.cursor()

		sql = """DELETE a.*, b.*, c.*, d.* FROM Cpu a, ram b, mobo c, prosessor d WHERE a.id_cpu = %s and a.id_ram = b.id_ram and a.id_mobo = c.id_mobo and a.id_prosessor = d.id_prosessor"""
		val = (id_cpu)
		
		cursor.execute(sql, val)
		cursor.close()
		self.__db.commit()

		print("{} record removed".format(cursor.rowcount))

	def deleteAllCpu(self):
		cursor = self.__db.cursor()

		sql = """DELETE a.*, b.*, c.*, d.* FROM Cpu a, ram b, mobo c, prosessor d WHERE a.id_ram = b.id_ram and a.id_mobo = c.id_mobo and a.id_prosessor = d.id_prosessor"""
		
		cursor.execute(sql)
		cursor.close()
		self.__db.commit()

		print("{} record removed".format(cursor.rowcount))