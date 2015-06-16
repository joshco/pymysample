from restnavigator import Navigator

class Osdi:
	def __init__(self,aep,api_token=None):
		self.rn= Navigator.hal(aep)
		if api_token:
			self.rn.headers['OSDI-API-Token']=api_token

	def sync(self):
		results=[]
		people=self.rn['osdi:people']['osdi:people']
		for person in people:
			state=person.state
			print state
			results.append(state)
		
		return results
