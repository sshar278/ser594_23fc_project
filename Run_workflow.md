### Instructions on running this project : 
1. Extract the zip and open the project folder with the IDE of your choice. 
2. Navigate to the directory where the requirements.txt file is located (cd ser594_23fc_project-master)
3. Creating a virtual environment : In terminal -> python -m venv venv (this creates a folder venv in the directory) or python3 -m venv venv
4. Activate the virtual environment : 
    For windows : type in terminal venv\Scripts\activate and press enter
    For mac/unix : type in terminal source venv/bin/activate and press enter
5. In the terminal, type python wf_core.py (or its better that for newer versions, you can do python3 wf_core.py in order to avoid any dependency issues). This includes the code to first install all the project dependencies, plus 
contains the subprocess to run both the wf_dataprocessing.py and then wf_visualization.py. A merged_data.db file will be generated which contains 
all the processed and cleaned data (this file can be viewed in the sqlite db browser). apart from that, the correlation.txt, summary.txt and the processed data files get stored in the data_processed folder. And finally the visuals get stored inside the visuals folder.
6. After this is done, you can type python wf_ml_evaluation.py (or python3 wf_ml_evaluation.py), the second entry point to the workflow. (run the wf_ml_evaluation file). This is responsible for handling everything. It first splits the data into training and testing sets, after that wf_training is invoked which then trains on the training data and generates a model file. After that the wf_prediction.py is called which then uses the model .pkl file as well as the test data in order to make predicitions (saved as predictions.csv in the evaluation folder). 
7. Apart from that, the wf_evaluation.py file also contains the code for the training and prediction outputs for the alternate KNN models, and it also contains some code in order to experiment with features (by varying A and B differently). And at last running this file shall also generate three visuals, the feature importance plot for the random classifier model, the confusion matrix and the model comparison (f1 score vs accuracy) for the random forest as well as the other 3 alternate KNN models.
8. In addition to this, all the evaluation metrics get stored as a summary.txt file in evaluation folder.
9. After folllowing all the steps, you can type deactivate in the terminal to exit 