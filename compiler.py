import PyInstaller.__main__
import os
import shutil

# --- CONFIGURATION ---
script_name = "main.py"
exe_name = "ToiletLocker"
# Using 'r' to prevent the unicodeescape error you got earlier
icon_path = r"C:\Users\Owner\Downloads\BlooketFlooder-master\ToiletLocker-main\resources\111.ico"

# Ensure the 'resources' folder exists before trying to bundle it
if not os.path.exists('resources'):
    print("ERROR: 'resources' folder not found! Make sure it is in the same folder as this script.")
    exit()

params = [
    script_name,
    '--onefile',         # Single EXE output
    '--noconsole',       # Hides the background CMD window
    f'--name={exe_name}',
    '--clean',           # Clears temp files before building
    # This bundles the folder: 'source_folder;destination_folder_inside_exe'
    '--add-data=resources;resources', 
]

# Add the icon only if it actually exists
if icon_path and os.path.exists(icon_path):
    params.append(f'--icon={icon_path}')
else:
    print("WARNING: Icon file not found. Compiling without custom icon.")

if __name__ == "__main__":
    print(f"--- Starting Build for {exe_name} ---")
    try:
        PyInstaller.__main__.run(params)
        print(f"\nSUCCESS! Your EXE is in the 'dist' folder.")
    except Exception as e:
        print(f"\nBUILD FAILED: {e}")