class editor:
	def __init__(self, filename=""):
		import os.path
		self.fd = filename
		self.cursor = 0
		if  self.fd!="" and os.path.exists(self.fd):  # Not ""
				self.source = self.read(filename,caller=1)
		else:
				self.source = [""]
	def read(self, fn, caller=0):
		try:
				return open(fn, 'r').read().split('\n')
		except FileNotFoundError:
				if caller == 1:
						print("No such file or directory")
						self.source = [""]
				else:
						return 1
	def append(self, arr):
		for item in arr:
				self.source.insert(self.cursor, item)
				self.cursor +=1

	def write(self, pwd, fn="NAN"):
		if fn == "NAN":
			f = open(self.fd, 'w')
		else:
			f = open(pwd + '/' + fn, 'w')
		payload = ""
		for item in self.source:
				payload += (item + '\n')
		f.write(payload)
		f.close()
	def getline(self, lineno):
		if lineno <= len(self.source):
				return self.source[lineno]
		else: 
				return 1
	def goto(self, pos):
		if not self.isint(pos):
				return 1
		pos = int(pos)
		if pos <= len(self.source):
			self.cursor = pos
			return 0
		else:
				return 1
	def isint(self, test):
		try:
				int(test)
				return True
		except ValueError:
				return False
	def getln(self, loc="NAN"):
		if loc == "NAN":
				loc = self.cursor
		if not self.isint(loc):
				return 1
		else:
			loc = int(loc)-1
		return self.source[loc]
	def getpos(self):
		return self.cursor
	def getlen(self):
		return len(self.source)
	def delline(self, loc="NAN"):

		if loc == "NAN":
				loc = self.cursor
		if not self.isint(loc):
				return 1
		else:
			loc = int(loc)-1
		try:
		  del self.source[loc]
		except: 
			return
	def list(self):
		for line in self.source:
			print(line)
	def changeline(self, content, loc="NAN"):
		if loc == "NAN":
			loc = self.cursor
		if self.isint(loc):
			if loc-1 >= 0 and loc-1 < len(self.source):
				self.source[loc] = content
