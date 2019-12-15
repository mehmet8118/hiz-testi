import requests
import time
import os


baslangic = int(time.time())
istek = requests.get("http://ipv4.download.thinkbroadband.com/5MB.zip",allow_redirects=True)
end = int(time.time())
print("%d saniye sürede 5MB dosya indirildi. Hızınız: %s" % (end - baslangic,(str(int((5*1024) / (end - baslangic))) + "kb/s")))
