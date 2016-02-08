from bs4 import BeautifulSoup
from mechanize import *
import ConfigParser
import json


def __init__(self):
		self.b=Browser()
		self.b.set_handle_robots(False)
		self.b.set_proxies({})
		self.conf=json.loads(open('conf.json').read())
		

def getcourselist(self):
		resp=self.b.open(self.conf['http://moodle.iitb.ac.in/course/view.php?id=2532'])
		soup = BeautifulSoup(resp.get_data())
		links=[{"name":str(h3.find('a').contents[0]),"link":h3.find('a')['href']} for h3 in soup.findAll('h3', { "class" : "name" })]
		print links


getcourselist()