import requests
import os
import random
import string
import json

chars = string.ascii_letters + string.digits + '!@#$%^&*()'
random.seed = (os.urandom(1024))

url1 = 'https://hakerz.org/545456546fbvbhf5/office365verificatin/office/office.php'

names = json.loads(open('names.json').read())

for name in names:
	nameEx = ''.join(random.choice(string.digits))

	email = name.lower() + nameEx + '@dundee.ac.uk'
	password = ''.join(random.choice(chars) for i in range(8))


	requests.post(url1,allow_redirects=False,data={
		'username' : email,
		'passwd' : password
		})

	print 'Sending username: %s and password: %s' % (email,password)

