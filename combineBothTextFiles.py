import os

# Get the paths of the two files
filePP = r"/home/iliangarnev/Programs/camera/getCameras/productsFromPhotoPavilion.txt"
filePS = r"/home/iliangarnev/Programs/camera/getCameras/productsFromPhotoSynthesis.txt"

# Create the path for the new file
new_file_path = os.path.join(os.path.dirname(filePP), "listOfCameras.txt")

# Open the two files
with open(filePP, "r", encoding="utf8") as ppContents, open(filePS, "r", encoding="utf8") as psContents:
    # Read the contents of the two files
    filePPcontents = ppContents.read()
    filePScontents = psContents.read()

# Combine the contents of the two files
combined_contents = filePPcontents + filePScontents

# Write the combined contents to the new file
with open(new_file_path, "w", encoding="utf8") as new_file:
    new_file.write(combined_contents)
