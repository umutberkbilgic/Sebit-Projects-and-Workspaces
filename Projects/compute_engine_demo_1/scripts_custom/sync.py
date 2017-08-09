import urllib2
import os

response_html = urllib2.urlopen("https://pastebin.com/raw/3paX0y4S")
file_html = open("/var/www/html/index.html", "w")
file_html.write(response_html.read())
file_html.close()

response_script = urllib2.urlopen("https://pastebin.com/raw/3EwG486f")
file_script = open("/usr/lib/cgi-bin/script.py", "w")
file_script.write(response_script.read())
file_script.close()

response_cars = urllib2.urlopen("https://pastebin.com/raw/7b1MnRxb")
file_cars = open("/usr/lib/cgi-bin/cars.py", "w")
file_cars.write(response_cars.read())
file_cars.close()

# depending on the raw data, unix may havbe problems with new line escapes
os.system("dos2unix /usr/lib/cgi-bin/script.py")
os.system("dos2unix /usr/lib/cgi-bin/cars.py")
