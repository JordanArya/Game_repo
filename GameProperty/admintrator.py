import os


class Admintrator:

	def __init__(self,parrent):
		self.app = parrent
		self.execute = parrent.Db
		self.message_execute  = parrent.MsgDb

	def clear_screen(self):

		if os.name == 'nt':
			os.system('cls')
		else:
			os.system('clear')

	def mainloop(self):

		self.clear_screen()

		print("""
			(1) SHOW ALL ACCOUNT
			(2) FIND ACCOUNT BY NAME
			(3) VIEW MESSAGE
			(4) SEND MESSAGE
			(5) LOOK SENDING HISTORY
			(6) REMOVE ACCOUNT
			(Q) QUIT
			""")
		option = input("OPTION : ").lower()

		if option == 'q':
			self.app.admin = False
			self.clear_screen()
			print("PYGAME-NYA SUDAH BENAR LAGI, MAAF UNTUK KETIDAKNYAMANAN-NYA")

		elif option == '1':
			data = self.execute.get_all_data()
			self.clear_screen()
			print('ID\t\tUsername\t\t Created \t\t\t\t Last Login \t\t Status\r')
			for all_data in data:
				print(f'{all_data[0]}\t\t{all_data[1]} \t\t {all_data[4]} \t\t {all_data[5]} \t {all_data[8]}')
			self.after_command()

		elif option == '2':
			Username = input('Input the Username : ').upper()
			data = self.execute.getdata(Username)
			if data:
				self.clear_screen()
				print('Username\t\t Created \t\t\t\t Last Login')
				print(f'{data[1]}\t\t {data[4]} \t\t {data[5]}')
			else:
				print('Data is not found')
			self.after_command()

		elif option == '3':
			data = self.message_execute.get_message('ADMIN')
			if data:
				print('ID\t\tUsername\tMessage')
				for all_data in data:
					print(f'{all_data[0]}\t\t{all_data[1]}\t\t{all_data[2]}')

			else:
				print('NO MESSAGE')
			self.after_command()
			
		elif option == '4':
			Message = str(input('MESSAGE : '))
			to = str(input('TO : ').upper())
			if not self.execute.check_new_data(to):
				self.message_execute.savedata(0,'ADMIN',Message,to,'ADMIN')
			elif to == 'ALL':
				self.message_execute.savedata(0,'ADMIN',Message,to,'ADMIN')
			else:
				print('Username is not found')
			self.after_command()

		elif option == '5':
			data = self.message_execute.get_send_history('ADMIN')
			if data:
				print('ID\t\tTO\t\tMessage')
				for all_data in data:
					print(f'{all_data[0]}\t\t{all_data[3]}\t\t{all_data[2]}')
			else:
				print('NO HISTORY')
			self.after_command()


		elif option == '6':
			Username = input('Input the Username : ').upper()
			data = self.execute.check_new_data(Username)
			if not data:
				self.clear_screen()
				self.execute.delete_user(Username)
			else:
				print('Data is not found')
			self.after_command()


	def after_command(self):
		print('')
		print('')
		input('press any button to continue')

			

