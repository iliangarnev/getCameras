import subprocess
import os

# Run the first Python file
subprocess.run(["python", "getCamerasPhotoPavilion.py"], check=True)

# Run the second Python file
subprocess.run(["python", "getCamerasPhotoSynthesis.py"], check=True)

# Run the third Python file
subprocess.run(["python", "combineBothTextFiles.py"], check=True)

# Open a .txt file in the default text editor
os.startfile("listOfCameras.txt")