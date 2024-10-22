"""Orchestrate the workflow of the core module, first calls the 
wf_dataprocessing.py first and then wf_visualization.py after the 
data is processed."""

import subprocess
import os
import sys

print("Installing dependencies from requirements.txt...")
try:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])
    print("Dependencies installed successfully!")
except subprocess.CalledProcessError as e:
    print("Failed to install dependencies. Error:", e)
    sys.exit(1)

base_dir = os.path.dirname(os.path.abspath(__file__))

# Ensure that the scripts exist
dataprocessing_path = os.path.join(base_dir, 'wf_dataprocessing.py')
visualization_path = os.path.join(base_dir, 'wf_visualization.py')

# Check if the scripts exist at the specified paths
if not os.path.exists(dataprocessing_path):
    print(f"Error: {dataprocessing_path} not found.")
    sys.exit(1)

if not os.path.exists(visualization_path):
    print(f"Error: {visualization_path} not found.")
    sys.exit(1)

def main():
    
    print("Starting data processing...")
    try:
        # Using sys.executable ensures we use the current Python interpreter
        subprocess.run([sys.executable, dataprocessing_path], check=True)
        print("Data processing completed.")
    except subprocess.CalledProcessError as e:
        print("Error during data processing. Error:", e)
        sys.exit(1)

    print("Starting data visualization and analysis...")
    try:
        subprocess.run([sys.executable, visualization_path], check=True)
        print("Data visualization completed.")
    except subprocess.CalledProcessError as e:
        print("Error during data visualization. Error:", e)
        sys.exit(1)

if __name__ == "__main__":
    main()



