import time
import urllib3
from stem import Signal
from stem.control import Controller
from urllib3.contrib.socks import SOCKSProxyManager
from fake_useragent import UserAgent


class TorProxy:
    def __init__(self):
        self.proxy = SOCKSProxyManager('socks5://127.0.0.1:9050')

    def new_ip(self):
        with Controller.from_port(port=9051) as controller:
            controller.authenticate(password="4444")
            controller.signal(Signal.NEWNYM)
            controller.close()

    def request(self, url):
        self.new_ip()
        headers = { 'User-Agent': UserAgent().random }
        rq = self.proxy.request('GET', url, headers=headers)
        return rq


cm = TorProxy()
s = cm.request("https://api.myip.com/")
print(s.data.decode('utf-8'))
