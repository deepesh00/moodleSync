import subprocess 
import mechanize
from sys import argv

from bs4 import BeautifulSoup
import urllib3
import re

script, u, p  = argv

us = open(u)
udata = us.read()

pw = open(p)
pdata = pw.read()

br = mechanize.Browser()
br.set_handle_robots(False)
sign_in = br.open("http://moodle.iitb.ac.in/login/index.php")
br.select_form(nr = 0)

br["username"] = udata
br["password"] = pdata

logged_in = br.submit()
logincheck = logged_in.read()




soup = BeautifulSoup(logincheck , "lxml")
print type(soup)


courses = soup.fetch("div", {"class" : re.compile("coursename")})
print courses

