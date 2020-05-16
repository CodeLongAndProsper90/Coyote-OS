def main(pwd, filename=""):
	from jedi import editor

	def split(word): 
			return [char for char in word] 

	e = editor(filename)
	p = '*'
	while True:
		command = input(p).split(' ')
		if command[0] == 'a':
			data = []
			txt = ""
			while txt != "`":
				data.append(txt) 
				txt = input()
			data.remove(data[0])
			e.append(data)
		elif command[0] == 'w':
			if len(command) == 1:
				e.write(pwd)
			else:
				e.write(pwd, command[1])
		elif e.isint(command[0]):
			e.goto(command[0])
		elif command[0] == 'p':
			if len(command) == 1:
				print( e.getln())
			elif len(split(command)) == 2:
				print(e.getln(int(command[1])))
		elif command[0] == 'd':
			if len(command) == 1:
				e.delline()
			elif len(command) == 2:
				e.delline(command[1])
		elif command[0] == 'l':
			e.list()
		elif command[0] == 'c':
			if len(command) == 1:
				e.changeline(input())
			else:
				e.changeline(input(), command[1])
		elif command[0] == 'q':
			break
		else:
			print("?")