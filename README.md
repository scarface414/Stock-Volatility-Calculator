## Overview
Creating a http endpoint using FastAPI implementing the following Functionality:
1. Accept a csv file or xlsx file with which data can be fetched. 
2. Compute Daily, Annualized volatility and return these values

## Project Structure
- ** stockvolatility -- folder
- **main.py:** The main FastAPI application file.
- **requirements.txt:** all required library in this file.

  ### Installation

1. Clone the repository:
    git clone git@github.com:scarface414/Stock-Volatility-Calculator.git
   
3. Create the python virtual environment.
    python -m venv env
   
4. Activate the virtual environment.
    env\Scripts\activate

5. Install dependencies:
    pip install -r requirements.txt

### Running the Application
    uvicorn main:app --reload

Result:
Once application runs on http://127.0.0.1:8000/ 
You can visit the API documentation at http://127.0.0.1:8000/docs
with the uploadfile endpoint you can upload the file and get the desired results.

### Uploading a NIFTY50.xlsx file
![image](https://github.com/scarface414/Stock-Volatility-Calculator/assets/80483279/cb54e0da-2c07-4da2-9b88-5bea86d7aa15)


### Uploading an unsupported file
![image](https://github.com/scarface414/Stock-Volatility-Calculator/assets/80483279/6e697fc5-34a4-4de1-9a43-c225b7ecc628)


### Frontend Integration 

In order to integrate the front-end
1. Download and Install NPM and Node on your device:
2. Install the Node Modules
   npm -i
3. Start the Application using
   npm start

You can visit the WebPage at http://127.0.0.1:3000 
Note : Make Sure that your backedn webserver is running.


