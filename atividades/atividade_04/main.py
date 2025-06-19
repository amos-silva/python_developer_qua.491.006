import os
import time
import datetime

while True:     # looping
    hora = datetime.datetime.now().strftime("%H:%M:%S")
    os.system("cls" if os.name == "nt" else "clear")
    print(f"Hora Atual:>>>  {hora}")
    time.sleep(1)