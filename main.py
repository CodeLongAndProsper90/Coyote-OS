def cdls():
	from time import sleep
	from termcolor import colored
	import platform
	from os import system
	from getch import getch
	eme = False
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
		os = get_os()
		if os == 'linux' or os == 'mac':
			system('clear')
		else:
			system('cls')

	def get_settings(filename):
		from ast import literal_eval
		#ulock(filename)
		with open(filename,'r') as inf:
			settings = literal_eval(inf.read())
		#lock(filename)
		return settings
	#Begin actual code execution
	clear()
	print(colored(logo, 'cyan'))
	print("Welcome to Coyote.")
	print("Press any key to log in")
	key = ''
	while key == '':
		key = getch()
	clear()

		
		

	time = 0.3
	version = '1.0.0'
	clear()
	#Define users and passwords from our settings file

	#Get the users username
	print(colored(logo, 'green'))
	user = input(colored("Username ", "green"))
	try:
		settings = get_settings(f'{user}.ledger')

	except:
		print('Ooops.')
		print('\n')
		print(f'We could not find your ledger file. It should be named: {user}.ledger')
		sleep(time)
		print('Loading default configuration')
		settings = get_settings('def.ledger')
		eme = True
	clear()	
	use = settings['username']
	pas = settings['password']

	#Check for username and password
	print(colored(logo, 'red'))
	password = input(colored('Password ', 'red'))
	if user == use:
		if password == pas:
			#clear screen 
			clear


	else:

		print("You are not in the list of Comrades!")
		exit()

	clear()
	sleep(time)
	print('Authentication success!')
	#Load kernel
	try:
		import coyote
	except ImportError:
		print("Primary kernel not found. Coyote cannot boot.")	
	if eme == True:
		print("Warning! Using default config. U: Cinco. P:Coyote. Pleaes use \"Config\" to fix the problem")
	print('Loading Coyote kernel ')
	sleep(time*2)
	print(f'Version {version}')
	sleep(time/2)
	#Start kernel
	coyote.os(settings, user, logo, get_os())
	cdls()
cdls()
	
