import os
import sys
from PIL import Image

def delete_files_with_specific_dimensions(directory, dimensions):
        for filename in os.listdir(directory):
            file_path = os.path.join(directory, filename)
            try:
                with Image.open(file_path) as img:
                    if img.size in dimensions:
                        os.remove(file_path)
                        print(f"Deleted {file_path}")
            except Exception as e:
                print(f"Failed to process {file_path}. Reason: {e}")

def delete_files_with_prefix(directory, prefix):
    for filename in os.listdir(directory):
        if filename.startswith(prefix) and (filename.endswith('.ppm') or filename.endswith('.jpg')):
            file_path = os.path.join(directory, filename)
            try:
                os.remove(file_path)
                print(f"Deleted {file_path}")
            except Exception as e:
                print(f"Failed to delete {file_path}. Reason: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python delete-some-files.py <directory> <prefix>")
        sys.exit(1)

    directory = sys.argv[1]
    prefix = sys.argv[2]

    dimensions_to_delete = [(974, 251), (1536, 1152), (395, 72), (217, 1094), (1769, 148)]
    delete_files_with_specific_dimensions(directory, dimensions_to_delete)