## Overview
Creating a http endpoint using FastAPI implementing the following Functionality:
1. Accept a csv file or xlsx file with which data can be fetched. 
2. Compute Daily, Annualized volatility and return these values

## Project Structure
- ** template -- folder
        - **index.html** for rendering the html page.
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