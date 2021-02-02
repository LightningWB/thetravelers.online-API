import signalr
import requests
import json

class lowClient():
	"""
	A low level client connection to the https://travelers.online
	"""
	PLAYAUTH=''
	def __init__(self, accountToken:str):
		self.token=accountToken
	def send(self, packet:dict):
		action = packet['action']
		self.logHub.server.invoke('cl_'+action, packet, self.PLAYAUTH)
	def onMessage(self, packet):
		pass
	def onUpdateImmediate(self, packet:dict):
		pass
	def onEvalJS(self, packet:str):
		pass
	def error(self, err):
		print(err)
	def stop(self):
		self.connection.close()
	def login(self, captcha:str):
		session = requests.Session()
		session.cookies.set('T', self.token)
		response = json.loads(session.post('https://thetravelers.online/default.aspx/GetAutolog', json={'captcha':captcha}).content.decode('utf-8'))['d']
		if response=='39':
			raise Exception('invalid captcha')
		elif response=='1':
			raise Exception('this account no longer exists')
		elif response=='19':
			raise Exception('the server is currently down for maintenance')
		elif response=='49':
			raise Exception('you have too many accounts online from this ip address.')
		elif response=='spam' or response=='':
			raise Exception('spam')
		self.PLAYAUTH=json.loads(response)['data']['PLAY_AUTH']
		self.connection = signalr.Connection('https://thetravelers.online/signalr', session)
		self.logHub:signalr.hubs.Hub = self.connection.register_hub('logHub')
		self.connection.start()
		# I have to do this so you can change later
		def callOnMessage(packet):
			self.onMessage(packet)
		def callOnUpdateImmediate(packet):
			self.onUpdateImmediate(packet)
		def callOnEvalJS(packet):
			self.onEvalJS(packet)
		self.logHub.client.on('getGameObject', callOnMessage)
		self.logHub.client.on('getGameObjectNoCountdown', callOnUpdateImmediate)
		self.logHub.client.on('raw', callOnEvalJS)
		self.connection.error+=self.error
		callOnMessage(json.loads(response)['data'])
		#self.connection.wait(30)