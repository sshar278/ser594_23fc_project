"""Orchestrate the workflow of the core module, first calls the 
wf_dataprocessing.py first and then wf_visualization.py after the 
data is processed."""

import subprocess

def main():
    print("Starting data processing...")
    subprocess.run(["python", "ser594_23fc_project/wf_dataprocessing.py"])
    print("Data processing completed.")
    
    print("Starting data visualization and analysis...")
    subprocess.run(["python", "ser594_23fc_project/wf_visualization.py"])
    print("Data visualization completed.")

if __name__ == "__main__":
    main()

