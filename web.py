#!/bin/usr/python
import requests

site= requests.get("https://ferrazdevasconcelos.sp.gov.br/web/")
status = site.status_code

if (status == 200):
	print ("Página Existente")
else:
	print ("Página Inexistente")
