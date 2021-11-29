import simplejson
import urllib3
import requests

def init_tor():
    # Verify Tor
    ip = simplejson.loads(requests.get('https://api.ipify.org/?format=json').text)['ip']
    tor = requests.get('https://check.torproject.org/exit-addresses', stream=True)

    is_tor = False
    for ip_tor in tor.iter_lines():
            ip_tor = str(ip_tor)
            ip_tor = ip_tor.strip()
            
            if 'ExitAddress' in ip_tor:
                    ip_tor = ip_tor.split(' ')[1]

                    if ip_tor == ip:
                            is_tor = True
                            break
    
    return is_tor