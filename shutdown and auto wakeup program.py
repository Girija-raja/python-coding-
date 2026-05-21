import os
import time
from datetime import datetime, timedelta
wake_time = datetime.now() + timedelta(minutes=2)
timestamp = int(wake_time.timestamp())

print(f"System will shut down and wake up at: {wake_time.strftime('%H:%M:%S')}")
os.system("echo 0 | sudo tee /sys/class/rtc/rtc0/wakealarm")
os.system(f"echo {timestamp} | sudo tee /sys/class/rtc/rtc0/wakealarm")

os.system("sudo shutdown -h now")
