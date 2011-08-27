#!/usr/bin/python2.7
import pycurl, json

class TwitterUser:
        def __init__(self):
                self.Name = raw_input("Username> ")
                self.Password = raw_input("Password> ")         

        def setName(self, name):
                self.Name = name

        def getName(self):
                return self.Name

        def setPassword(self, passw):
                self.Password = passw
        
        def getPassword(self):
                return self.Password

STREAM_URL = "http://stream.twitter.com/1/statuses/sample.json"

class Client:
	def __init__(self, tuser):
		self.buffer = ""
		self.conn = pycurl.Curl()
		self.conn.setopt(pycurl.USERPWD, "%s:%s" % (tuser.getName(), tuser.getPassword()))
		self.conn.setopt(pycurl.URL, STREAM_URL)
		self.conn.setopt(pycurl.WRITEFUNCTION, self.on_receive)
		self.conn.perform()

	def on_receive(self, data):
		self.buffer += data
		if data.endswith("\r\n") and self.buffer.strip():
			try:
				content = json.loads(self.buffer)
			except ValueError:
				self.buffer = ""
				return

			self.buffer = ""
			if "text" in content:
				try:
					print u"{0[text]}".format(content)
				except:
					return

tuser = TwitterUser()
try:
	client = Client(tuser)
except (KeyboardInterrupt, SystemExit):
	print "Exiting..."
