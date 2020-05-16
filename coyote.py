def save_settings(login_user, settings):
	ledger = f'{login_user}.ledger'
	#io.ulock(ledger)
	local_table = open(ledger,'w')
	local_table.write(str(settings))
	local_table.close()
	#io.lock(ledger)
def error(code):
	errors = \
	{
		1 : "Command not implmented" 
	}
	print(f"ERROR: {errors[code]}")
def print_command(commands):
	for item in commands:
		print(item, end='\n')
	print()

def replace_last(source_string, replace_what, replace_with):
	head, _sep, tail = source_string.rpartition(replace_what)
	return head + replace_with + tail

def get_pwd(pwd):
	root = 'os'
	if pwd == root:
		pwd = '/'
	else:
		pwd = pwd.replace('os/Cinco','',1)
	return pwd
def os(settings, login_user, logo):
	root = f'os/{settings["username"]}'
	pwd = root
	while True:
		try:
			from time import sleep
			from termcolor import colored
			from os import remove, listdir, mkdir
			import os.path
			from getch import getch
			import hashlib
			import editor
			dfault = {
				'username' : 'Cinco',
				"password" : 'Coyote',
				'prompt_color' : "green"
			}


			commands =['exit', 'help',  'cconfig', 'logout', 'jedi', 'cat', 'cd', 'ls', 'la', 'man', 'mkdir', 'sysinfo', 'exec']
			try:
				command = input(colored(f"DEV@coyote {get_pwd(pwd)} $ ", settings['prompt_color'])).rstrip().lstrip().split(' ')
			except KeyError:
				print("We don't have that color yet.")
				settings['prompt_color'] = 'green'

				
			if command[0] in commands:
				
				if command[0] == 'exit':
					print('Exiting Coyote')
					sleep(0.314)
					save_settings(login_user, settings)
					exit(0)
				elif command[0] == 'help':
					print_command(commands)
				elif command[0] == 'cconfig':
					print("Your current settings are:")
					print(f"USERNAME:\t{settings['username']}\nPASSWORD HASH:\t{settings['password']}\nPROMPT COLOR:\t{settings['prompt_color']}")
					print('[0] Exit\n[1] Change Username\n[2] Change password\n[3] Change prompt color\n[4] Add a user\n[5] Delete a user')
					setting = getch()
					if setting == '0':
						continue
					if setting == '1':
						user = input("What is the new username? ")
						settings['username'] = user
					elif setting == '2':
						pas = input("What is your new password? ")
						settings['password'] = hashlib.sha256(pas.encode()).hexdigest()
					elif setting == '3':
						print("Colors can be: \ngrey\nred\ngreen\nyellow\nblue\nmagenta\ncyan\nwhite")
						color = input("What is the new color? ")
						try:
							settings['prompt_color'] = color
						except:
							print("Oops... We don't have that color yet.")
					elif setting =='4':
						ledger_new = dfault
						use = input("What will be the new user's username? ")
						ledger_new['username'] = use
						pas = input('What is the new user\'s password? ')
						ledger_new['password'] = hashlib.sha256(pas.encode()).hexdigest()
						led = open(f"{use}.ledger", 'x')
						led.write(str(ledger_new))
						led.close()
						ledger_new = {}
						mkdir(root + '/' + use)
						with open(root + '/' + use, 'w') as f:
							f.write("Hi! Thanks for using Coyote OS, by Scott Little\nVersion Two")
					elif setting == '5':
						confirm = input(colored("Do you what to contine? [Y/N] "))
						if confirm == 'Y' or confirm == 'y':
							pass
						else:
							continue
						use = input("What user do you want to delete?")
						remove(use)


				elif command[0] == 'logout':
					save_settings(login_user, settings)
					break
				elif command[0] == 'jedi':
					if len(command) < 2:
						editor.main(pwd)
					else:
						editor.main(pwd, pwd + "/" + command[1])
							
				elif command[0] == 'cat':
					if len(command) < 2:
						print("Missing required argument")
						continue
					p = f"{pwd}/{command[1]}"
					if os.path.exists(p):
						print(open(p, 'r').read())
					else:
						print(f"{command[1]}: No such file or directory")
					
				if command[0] == 'ls':

					if len(command) == 1:
						p = pwd 
					elif len(command) > 1:
						if not os.path.exists(f'{pwd}/{command[1]}'):
							print(command[1] + ": No such file or directory")
							continue
						p = f'{pwd}/{command[1]}'
					files = [f for f in listdir(p) if os.path.isfile(os.path.join(p, f))]
					for item in files:
						if not item.startswith('.'):
							print(item)
					dirs = [f for f in listdir(p) if os.path.isdir(os.path.join(p, f))]
					for item in dirs:
						if not item.startswith('.'):
							print(colored(item, 'blue'), end=' ')
					print()

				if command[0] == 'la':
					if len(command) == 1:
						p = pwd
					elif len(command) > 1:
						if not os.path.exists(f'{pwd}/{command[1]}'):
							print(command[1] + ": No such file or directory")
							continue
						p = f'{pwd}/{command[1]}'
					files = [f for f in listdir(p) if os.path.isfile(os.path.join(p, f))]
					for item in files:
						print(item)
					dirs = [f for f in listdir(p) if os.path.isdir(os.path.join(p, f))]
					for item in dirs:
						print(colored(item,'blue'), end = ' ')
					print()

				if command[0] == 'cd':
					if len(command) < 2:
						print("Missing required argument")
						continue
					if command[1] == '..':
						pwd = pwd.rsplit('/',1)[0]
					elif os.path.isdir(f"{pwd}/{command[1]}"):
						pwd = f'{pwd}/{command[1]}'

				if command[0] == 'mkdir':
					if len(command) < 2:
						print("Missing required argument")
						continue
					mkdir(f'{pwd}/{command[1]}')
				if command[0] == 'man':
					if len(command) < 2:
						print("Missing required argument")
						continue
					if os.path.exists(f'man/{command[1]}.txt'):
						with open(f'man/{command[1]}.txt') as f:
							print(f.read())
					else:
						print("No manual for " + command[1])
				if command[0] == 'sysinfo':
					with open('sysinfo.txt') as f:
						print(f.read())
				if command[0] == 'exec':
					if os.path.isfile(pwd + '/' + command[1]):
						args = ""
						for i in range(2, len(command)):
							args += command[1] + ""
						os.system(f'python3 {pwd}/{command[1]} {args}')


			if command[0] not in commands:
				error(1)
		except KeyboardInterrupt:
					save_settings(login_user, settings)
		continue