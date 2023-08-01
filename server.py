import urllib

site = urllib.urlopen("https://ferrazdevasconcelos.sp.gov.br/web/")
server = site.info()

print ("O Servidor WEB está Rodando")
print (server['Server'])
