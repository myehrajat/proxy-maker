import urllib
import urllib.request, urllib.error
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from fake_useragent import UserAgent
import random
import os
import sys
import time

ua = UserAgent() # From here we generate a random user agent
proxies = [] # Will contain proxies [ip, port]
is_enabled_proxy = False

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
    global is_enabled_proxy
    # Our code here
    # Retrieve latest proxies
    connection = internet_on()
    print("Connection Status:"+str(connection))
    if connection != True:#may last proxy set failed so no net conection
      # no internet
      print("AS Connection Status is "+str(connection)+". We think no internet connection")
    proxies_req = Request('http://ehrajat.com/p.php')
    print("Get Proxy Services")
    proxies_req.add_header('User-Agent', ua.random)
    print("Make Random User-Agent")
    try:
        respons = urlopen(proxies_req)
        ##OUR SERVER DONT ACCEPT PROXY
        is_enabled_proxy = False

    except:
        print('Your proxy setting misconfigured we disable it.')
        os.system("disableproxy.vbs")
        print('Your proxy setting disabled.')
        print('Restart Script.')
        self_file = os.path.abspath(__file__)
        print("Trigger "+self_file )
        f = open("restart.vbs", "w")
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
                wait(2)
                obj.sendkeys"python '''+self_file+'''"
                obj.sendkeys"{ENTER}"
                ''')

        f.close()
        ##OUR SERVER DONT ACCEPT PROXY
        #is_enabled_proxy = False
        os.system("restart.vbs")
        os._exit(0)

    proxies_doc = urlopen(proxies_req).read().decode('utf8')
    print("Create Proxy Doc")     
    soup = BeautifulSoup(proxies_doc, 'html.parser')
    print("Parse Proxy Doc")
    proxies_table = soup.find(id='proxylisttable')
    print("Get Proxy Services Table")
    # Save proxies in the array
    for row in proxies_table.tbody.find_all('tr'):
      print("wait.. Getting proxies")
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
      #print(proxies)
    

if __name__ == '__main__':
  main()
proxy_index = random_proxy()
proxy = proxies[proxy_index]
  
for n in range(1, 100):
    req = Request('http://icanhazip.com')
    req.set_proxy(proxy['ip'] + ':' + proxy['port'], 'http')
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

if(is_enabled_proxy==True):
    print("Proxy right now is "+str(is_enabled_proxy)+" reset it with some other")
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
    #print(f.read())
    os.system("changeproxy.vbs")
else:
    print("Proxy right now is "+str(is_enabled_proxy)+" we set it for you to be free")
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
    #print(f.read())
    os.system("changeproxy.vbs")
