import os
import json
import shutil

# Set the path to the directory containing the .info files
path = "d:/Lora"

# Create subfolders if they don't exist
locon_folder = os.path.join(path, "LoCon")
if not os.path.exists(locon_folder):
    os.mkdir(locon_folder)

filelist = []
# Loop through all files in the directory
for filename in os.listdir(path):
    if filename.endswith(".info"):
        # Open the .info file and load the JSON data
        with open(os.path.join(path, filename), "r") as f:
            data = json.load(f)
        #print(filename.split(".")[0])
        # Check if the "model" field has a "type" of "LoCon"
        if "model" in data and data["model"].get("type") == "LoCon":
            # Get the base filename (without the extension)
            base_filename = filename.split(".")[0]
            
            print(f"Found LoCon model: {base_filename}")
            # Move the .info file to the LoCon subfolder
            #shutil.move(os.path.join(path, filename), os.path.join(locon_folder, filename))
            filelist.append(base_filename + ".civitai.info")
            # Check for and move the other required files
            for extension in [".preview.png", ".png", ".safetensors", ".ckpt"]:
                source_file = os.path.join(path, base_filename + extension)
                #print(f"Checking for {source_file}")
                if os.path.exists(source_file):
                    filelist.append(base_filename + extension)
                # else:
                #     print(f"File {source_file} not found")
                #     pass
                    #shutil.move(source_file, os.path.join(locon_folder, base_filename + extension))
            #         shutil.move(source_file, os.path.join(locon_folder, base_filename + extension))
            #     else:
            #         print(f"File {source_file} not found")

for file in filelist:
    shutil.move(os.path.join(path, file), os.path.join(locon_folder, file))
