import time
import subprocess

while True:
    # Call first script
    subprocess.run(["python3", "getCamerasPhotoPavilion.py"])
    
    # Wait for one hour
    time.sleep(10)
    
    # Call second script
    subprocess.run(["python3", "getCamerasPhotoSynthesis.py"])
    
    # Wait for one hour
    time.sleep(3600)