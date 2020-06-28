from ModelCpu import ModelCpu
import pprint

class Interface:
	def opsi(self):
		while True:
			print("\n1. Add CPU\n2. Show CPU\n3. Show All CPU\n4. Delete CPU\n5. Delete All Cpu\n6. Exit")
			pilih = int(input("Input Your Choice: "))
			if pilih == 1:
				data = {'id_cpu':None, 'warna':None, 'id_ram':None, 'kapasitas':None, 'kecepatan_ram':None, 
				'id_mobo':None, 'jumlah_slot_memory':None, 'jumlah_slot_harddisk':None,
				'id_prosessor':None, 'core':None, 'kecepatan':None}

				for key in list(data):
					data[key] = input('masukan ' + key + ':')

				modelCpu=ModelCpu()
				modelCpu.addCpu(data)

			elif pilih == 2:
				modelCpu=ModelCpu()
				getCpu = input('\nMasukan ID CPU yang dicari: ')
				cpu = modelCpu.getCpuById(getCpu)
				pprint.pprint(cpu)

			elif pilih == 3:
				modelCpu=ModelCpu()
				cpu = modelCpu.getAllCpu()
				pprint.pprint(cpu)

			elif pilih == 4:
				modelCpu=ModelCpu()
				deleteCpu = input('\nMasukan ID CPU yang ingin dihapus: ')
				cpu = modelCpu.deleteById(deleteCpu)

			elif pilih == 5:
				modelCpu=ModelCpu()
				cpu = modelCpu.deleteAllCpu()

			else:
				break
