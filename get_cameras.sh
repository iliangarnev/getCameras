#!/bin/bash

chmod +x get_cameras.sh

# Run the first Python file
python3 getCamerasPhotoPavilion.py

# Run the second Python file
python3 getCamerasPhotoSynthesis.py

# Run the third Python file
python3 combineBothTextFiles.py

# Open a .txt file in the default text editor
xdg-open listOfCameras.txt
