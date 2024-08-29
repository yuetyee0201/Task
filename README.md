# logo_detector

## Run the code in the terminal
To run the provided Python code in the terminal, you need to ensure the following preparations are met:

Install Python: Make sure Python is installed on your system.

Install Required Libraries:

Install the google-cloud-vision library to utilize the Google Cloud Vision API.
Install the tqdm library to provide progress bar functionality.
Ensure argparse is installed, which usually comes as part of Python’s standard library.
Set Up Google Cloud Service Account Key:

Ensure you have a service account key file (JSON) for Google Cloud Platform and that it is either properly set as an environmental variable or specified directly in the code.
Save the Python Script:

Save the code as a Python script file, for example, logo_recognition.py.
Prepare Command Line Arguments in the Terminal:

Prepare appropriate command line arguments to run the script, including the path to the image file (or directory), the path to the JSON key, and the optional output file path.
Based on these preparations, here are the specific steps and commands you need to input in the terminal:


## Install necessary libraries
pip install google-cloud-vision tqdm


## Run the script (ensure the code is saved as logo_recognition.py and replace paths and filenames in the command below accordingly)
python logo_recognition.py /path/to/images -k /path/to/your/service_account.json -o /path/to/output.csv
These commands will start the script, processing all images in the file or directory specified, identifying and recording logo information found within the images.

