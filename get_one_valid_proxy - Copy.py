from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import os
import sys
import time

ua = UserAgent() # From here we generate a random user agent
proxies = [] # Will contain proxies [ip, port]
is_enabled_proxy = True

def internet_on():
    try:
        Request('http://ehrajat.com/p.php')
        return True
    except: 
        return False

# Main function
# Retrieve a random index proxy (we need the index to delete it if not working)
def random_proxy():
  return random.randint(0, len(proxies) - 1)
def main():
    # Our code here
    # Retrieve latest proxies
    connection = internet_on()
    if connection != True:#may last proxy set failed so no net conection
      #disable proxy
      os.system("disableproxy.vbs")
      is_enabled_proxy = False
      time.sleep(30)
      main()
    
    proxies_req = Request('http://ehrajat.com/p.php')
    proxies_req.add_header('User-Agent', ua.random)
    proxies_doc = urlopen(proxies_req).read().decode('utf8')
    soup = BeautifulSoup(proxies_doc, 'html.parser')
    proxies_table = soup.find(id='proxylisttable')

    # Save proxies in the array
    for row in proxies_table.tbody.find_all('tr'):
      if (row.find_all('td')[2].string=="FR" or
          row.find_all('td')[2].string=="GB" or
          row.find_all('td')[2].string=="US" or
          row.find_all('td')[2].string=="CA" or
          row.find_all('td')[2].string=="DE" or
          row.find_all('td')[2].string=="AU" or
          row.find_all('td')[2].string=="ES"
          
          ):
          proxies.append({
            'ip':   row.find_all('td')[0].string,
            'port': row.find_all('td')[1].string,
            'code': row.find_all('td')[2].string,
            'country': row.find_all('td')[3].string,
            'anonymity': row.find_all('td')[4].string,
            'google': row.find_all('td')[5].string,
            'https': row.find_all('td')[6].string,
            'last_checked': row.find_all('td')[7].string,
          })
      print(proxies)
    

if __name__ == '__main__':
  main()
proxy_index = random_proxy()
proxy = proxies[proxy_index]
  
for n in range(1, 100):
    req = Request('http://icanhazip.com')
    req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')
    #req.update_proxy(proxy['ip'] + ':' + proxy['port'])
    # Every 10 requests, generate a new proxy
    #if n % 10 == 0:
    #  proxy_index = random_proxy()
    #  proxy = proxies[proxy_index]
    
# Make the call
    try:
      my_ip = urlopen(req).read().decode('utf8')
      print('#' + str(n) + ': ' + my_ip)
      break
    except: # If error, delete this proxy and find another one
      del proxies[proxy_index]
      print('Proxy ' + proxy['ip'] + ':' + proxy['port'] + ' deleted.')
      proxy_index = random_proxy()
      proxy = proxies[proxy_index]
print(proxy)
os.system("enableproxy.vbs")
is_enabled_proxy = True
time.sleep(30)

f = open("changeproxy.vbs", "w")
f.write('''
option Explicit
Function wait(sec)
	Dim dteWait
  	dteWait = DateAdd("s", sec, Now())
	Do Until (Now() > dteWait)
	Loop
End Function
Dim obj
set obj = CreateObject("wscript.shell")
obj.run("cmd")
wait(4)
obj.sendkeys"inetcpl.cpl"
wait(1)
obj.sendkeys"{ENTER}"
wait(1)
obj.sendkeys"^{Tab}"
wait(1)
obj.sendkeys"^{Tab}"
wait(1)
obj.sendkeys"^{Tab}"
wait(1)
obj.sendkeys"^{Tab}"
wait(1)
obj.sendkeys"L"
wait(1)
obj.sendkeys"x"
wait(1)
obj.sendkeys"x"
wait(1)
obj.sendkeys"{Tab}"
wait(1)
obj.sendkeys"'''+proxy['ip']+'''"
wait(1)
obj.sendkeys"{Tab}"
wait(1)
obj.sendkeys"'''+str(proxy['port'])+'''"
wait(1)
obj.sendkeys"{Tab}"
wait(1)
obj.sendkeys"{Tab}"
wait(1)
obj.sendkeys"{Tab}"
wait(1)
obj.sendkeys"{ENTER}"
wait(1)
obj.sendkeys"{Tab}"
wait(1)
obj.sendkeys"{Tab}"
wait(1)
obj.sendkeys"{Tab}"
wait(1)
obj.sendkeys"{Tab}"
wait(1)
obj.sendkeys"{Tab}"
wait(1)
obj.sendkeys"{ENTER}"
''')
f.close()

#open and read the file after the appending:
f = open("changeproxy.vbs", "r")
print(f.read())
import os
import sys
os.system("changeproxy.vbs")

