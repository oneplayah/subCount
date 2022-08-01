import os
import requests
from colors import *

user = os.environ["REPL_OWNER"]

import threading

global yo;
yo = 0;

def printit():
  threading.Timer(2.0, printit).start()
  profile = requests.get(f"https://vk.com/yeezqwa").text
  global yo;
  
  yo = profile[profile.find('followerCount')+15: profile.find('followerCount')+30].lower().replace('a','').replace('b','').replace('c','').replace('d','').replace('e','').replace('f','').replace('g','').replace('h','').replace('i','').replace('j','').replace('k','').replace('l','').replace('m','').replace('n','').replace('o','').replace('p','').replace('q','').replace('r','').replace('s','').replace('t','').replace('u','').replace('v','').replace('w','').replace('x','').replace('y','').replace('z','').replace(',','').replace('"','')
  
  print(f"{bright_blue}e {Blue}e{bright_blue}:{bright_yellow}",yo,reset,"\n")

printit()

from flask import Flask, send_file
app = Flask(__name__)

@app.route("/codergautamyt")
def yekyahai():
    global yo;
    return str(yo)

@app.route("/")
def mujhepythonpasandnahihaikesehua():
  entry = os.path.join('index.html')
  return send_file(entry)

if __name__ == "__main__":
    app.run(host='0.0.0.0')
