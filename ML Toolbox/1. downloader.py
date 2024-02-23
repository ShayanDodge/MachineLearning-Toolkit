# Import necessary modules
import os  # Operating system module for file and directory operations
import tarfile  # Module for working with tar archives
import urllib.request  # Module for opening and reading URLs


# Define a function to fetch housing data
def fetch_housing_data(housing_url, housing_path):
    # Create the local directory if it doesn't exist
    os.makedirs(housing_path, exist_ok=True)
    
    # Construct the full path for the downloaded tar file
    tgz_path = os.path.join(housing_path, "housing.tgz")
    
    # Download the tar file from the specified URL and save it locally
    urllib.request.urlretrieve(housing_url, tgz_path)
    
    # Open the downloaded tar file
    housing_tgz = tarfile.open(tgz_path)
    
    # Extract all contents from the tar file to the specified directory
    housing_tgz.extractall(path=housing_path)
    
    # Close the tar file
    housing_tgz.close()

# Call the function to fetch housing data
    if __name__=="__main__":
        # Define the local path where the housing dataset will be stored
        HOUSING_PATH = os.path.join("datasets", "housing")

        # Define the complete URL of the housing dataset
        HOUSING_URL = "https://raw.githubusercontent.com/ageron/handson-ml2/master/datasets/housing/housing.tgz"

        fetch_housing_data(HOUSING_URL, HOUSING_PATH)