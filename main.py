from time import sleep
from colorama import Fore, Style
from termcolor import colored
import platform
from os import system
from getch import getch
import hashlib
from ast import literal_eval
def cdls():


	#Definintons for bootloader and CDLS [Coyote Data Load System]
	logo = """
	            .-'''''-.
             .'         `.
            :             :
           :               :
           :      _/|      :
            :   =/_/      :
             `._/ |     .'
          (   /  ,|...-'
           \_/^\/||__
        _/~  `\"\"~`\"` \_
     __/  -'/  `-._ `\_\__
   /     /-'`  `\   \  \-.\
	"""
	def get_os():
		plat = platform.system()
		if plat == 'Linux':
			return 'linux'
		elif plat == 'Darwin':
			return 'mac'
		elif plat == 'Windows':
			return  'nt'

	def clear():
		pass
		os = get_os()
		if os == 'linux' or os == 'mac':
			system('clear')
		else:
			system('cls')

	def get_settings(filename):
		#ulock(filename)
		with open(filename,'r') as inf:
			settings = literal_eval(inf.read())
		#lock(filename)
		return settings
	#Begin actual code execution
	clear()
	print(Fore.CYAN, logo)
	print(Style.RESET_ALL)
	print("Welcome to Coyote.")
	print("Press any key to log in")
	key = ''
	while key == '':
		key = getch()
	clear()

		
		

	time = 0.3
	version = '2.5.0'
	clear()
	while True:
		clear()

		print(colored(logo, 'green'))
		user = input(colored("Username ", "green"))
		try:
			settings = get_settings(f'{user}.ledger')

		except:
			print('Ooops.')
			print("Invalid username. Press ENTER to continue")
			getch()
			continue


		use = settings['username']
		pas = settings['password']

		#Check for username and password
		clear()
		print(colored(logo, 'red'))
		hash  = hashlib.sha256()
		paas = input( Fore.RED + 'Password ' + Style.RESET_ALL ).encode()
		print(Style.RESET_ALL)
		hash.update(paas)
		if user == use:
			if hash.hexdigest() == pas:
				#clear screen
				break


			else:

				print("I'm sorry, I'm afraid I can't let you do that.")
				print("Press ENTER to retry.")
				getch()
				continue

	clear()
	sleep(time)
	print('Authentication success!')
	#Load kernel
	try:
		import coyote
	except ImportError:
		print("Primary kernel not found. Coyote cannot boot.")	
	print('Loading Coyote kernel ')
	sleep(time*2)
	print(f'Version {version}')
	sleep(time/2)
	#Start kernel
	try:
		coyote.os(settings, user, logo)
	except:
		print("Fatal Error. Abort.")
		raise
	cdls()
cdls()
	

