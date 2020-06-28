import pymysql
import DB_Config as config

class Connection:

	def open(self):
		try:
			connect = pymysql.connect(
			  host=config.host,
			  user=config.user,
			  passwd=config.passwd,
			  database=config.database
			)
		except pymysql.Error as err:
			print(err)
		else:
			return connect

	def close(self):
		if self.open.is_connected:
			self.open.close()

# if __name__ == '__main__':
# 	c = Connection()
# 	c.open()