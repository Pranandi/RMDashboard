# run all the file under the uploaded folder
import os
def run_all_files(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith(".py"):
            file_path = os.path.join(folder_path, filename)
            print(f"Running {file_path}...")
            os.system(f"python {file_path}")
# specify the folder path
folder_path = "Uploader"
run_all_files(folder_path)