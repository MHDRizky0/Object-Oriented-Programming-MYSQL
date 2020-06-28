# from ModelClub import ModelClub
# from ModelAchievement import ModelAchievement
# from ModelAgen_Transfer import ModelAgen_Transfer
# from ModelClub import ModelClub
# from Athlete import ModelAthlete
# from interface import Interface
from ModelMobo import ModelMobo
from ModelRam import ModelRam
from ModelProsessor import ModelProsessor
from ModelCpu import ModelCpu
from interface import Interface
import pprint

if __name__ == '__main__':
	# modelRam = ModelRam()
	# modelMobo = ModelMobo()
	# modelProsessor = ModelProsessor()
	# modelCpu = ModelCpu()
	# modelAchievement = ModelAchievement()
	# modelAthlete = ModelAthlete()
	interface = Interface()
	interface.opsi()


	""" Select insert data """
	# data = {'id_Prosessor':"P02", 'core':"7", 'kecepatan':"5Ghz"}
	# modelProsessor.insertProsessor(data)

	# data = {'name_achievement':"TI12", 'year':2012}
	# modelAchievement.insertAchievement(data)

	# """ Select all data """
	# data = modelProsessor.selectAllProsessor()
	# for datum in data:
	# 	print(datum)

	# data = modelAchievement.selectAllAchievement()
	# for datum in data:
	# 	print(datum)

	""" Select one data """
	# data = modelProsessor.selectProsessor('P02')
	# print(data)

	# """ Remove Club """
	# modelProsessor.deleteProsessor('P02')
	
	# """ Update Club """
	# modelProsessor.updateProsessor('M02', "8", "16")
	# data = modelProsessor.selectProsessor('M02')
	# print(data)

	# data = {'id_cpu':None, 'warna':None, 'id_ram':None, 'kapasitas':None, 'kecepatan':None, 
	# 		'id_mobo':None, 'jumlah_slot_memory':None, 'jumlah_slot_harddisk':None,
	# 		'id_prosessor':None, 'core':None, 'kecepatan':None}

	# for key in list(data):
	# 	data[key] = input('masukan ' + key + ':')

	# modelCpu.addCpu(data)

	# getPlayer = input('masukan id_cpu: ')
	# player = modelAthlete.getPlayer(getPlayer)
	# pprint.pprint(player)

	# # # dataa = modelAthlete.getAllPlayer()
	# # # pprint.pprint(dataa)