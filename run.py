#run.py
import os
import eel
from engine import waterlvl   # 👈 import with package path

eel.init("www")

# Launch Chrome in app mode
os.system(r'start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" --app="http://localhost:8000/index.html"')

# Start eel without blocking so we can still run Python code
eel.start("index.html", mode=None, host='localhost', port=8000, block=False)

# Example test: update water level after frontend loads
import time
time.sleep(2)
waterlvl.update_water_level(67)

# Keep alive
while True:
    eel.sleep(1)
