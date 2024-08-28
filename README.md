# logo_detector


# Before you run the code in the terminal
Setting the working directory in the terminal (i.e., changing the current working directory) depends on the operating system you are using. Here are common methods to set the working path in different operating systems:

For Windows Users:
Open Command Prompt or PowerShell.

Use the cd (Change Directory) command to change the current working directory. For example, if you want to switch to the directory D:\Projects\MyProject, you can type:

cd D:\Projects\MyProject


If the path contains spaces, you need to enclose the path in double quotes:

cd "D:\My Projects\MyProject"
For macOS and Linux Users:
Open Terminal.


Also use the cd command to change directories. For example, if you want to switch to the directory /home/user/projects/myproject, you can type:

cd /home/user/projects/myproject


If the path contains spaces, you also need to enclose the path in double quotes:

cd "/home/user/projects/My Project"


Some Useful Additional Commands:
cd .. (the same across all operating systems): This command moves the current directory up one level.
cd or cd ~ (in macOS and Linux): Both commands switch the current directory to the user's home directory.
cd \ (in Windows) or cd / (in macOS and Linux): This moves the current directory to the root directory.
Using these commands can help you navigate quickly between directories in the terminal.


# Run the code in the terminal
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


# Install necessary libraries
pip install google-cloud-vision tqdm


# Run the script (ensure the code is saved as logo_recognition.py and replace paths and filenames in the command below accordingly)
python logo_recognition.py /path/to/images -k /path/to/your/service_account.json -o /path/to/output.csv
These commands will start the script, processing all images in the file or directory specified, identifying and recording logo information found within the images.


# p.s.: 
1. Google APIs:

These refer to a set of interfaces provided by Google that allow developers to access specific functions and data of Google services. For example, the Google Maps API allows developers to embed maps and perform map-related data operations in their applications, while the Google Drive API enables developers to manage and manipulate files stored on Google Drive.
Developers use these APIs to enhance their applications, enabling them to interact with services offered by Google.

2. Google Cloud Service Account Keys:

These are keys used to authenticate applications or instances that use Google Cloud Platform (GCP) services. A service account is a special type of account on Google Cloud, mainly used for non-interactive authentication between services.
Service account keys can be in JSON or P12 format and provide an authentication mechanism for API calls. When your application needs to interact with Google Cloud services, such as Google Cloud Storage or Google Compute Engine, you can use these keys to authenticate and authorize your requests.

2.1 To obtain a Google service account key, you can follow these steps:

Access Google Cloud Console:

Open your browser and navigate to the Google Cloud Console.
Select or Create a Project:

If you don't already have a Google Cloud project, you will need to create a new one. If you already have a project, select the project for which you want to generate a service account key.
Enable APIs:

In the project dashboard, go to "APIs & Services" under the "Library" menu, then search and enable the APIs you need. For example, if you need access to Google Cloud Vision API, you would find and enable it.
Create a Service Account:

In the navigation menu, select "IAM & Admin" followed by "Service Accounts", then click "Create Service Account".
Enter a name and description for the service account, then click "Create".
Choose the appropriate role. For instance, if you need access to Google Cloud Storage, you might select a role like "Storage Object Viewer" or a role with more permissions.
Click "Continue" and then "Done" to create the service account.
Generate Service Account Key:

On the "Service Accounts" page, find the service account you just created and click to enter its details page.
Go to the "Keys" tab, click "Add Key", and choose "Create New Key".
Select the key type (JSON is recommended), then click "Create".
The key file will automatically download to your computer. This is your private key file used to authenticate your application, so keep it secure.
Security Considerations:

Do not upload your key file to public code repositories or share it with non-essential personnel.
Regularly rotate keys, i.e., periodically replace old keys with new ones and deactivate the old keys.
After completing these steps, you will have a service account key that can be used to authenticate and authorize your application to access specified Google Cloud resources.


# For security and other well-known reasons, I will not disclose the keys I use. Please ask anyone who needs to use this code to request their own key for all operations to work.
