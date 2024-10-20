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

dataprocessing_path = os.path.join(base_dir, 'wf_dataprocessing.py')
visualization_path = os.path.join(base_dir, 'wf_visualization.py')

def main():
    print("Starting data processing...")
    subprocess.run(["python", dataprocessing_path])
    print("Data processing completed.")
    
    print("Starting data visualization and analysis...")
    subprocess.run(["python", visualization_path])
    print("Data visualization completed.")

if __name__ == "__main__":
    main()



