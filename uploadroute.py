from fastapi import FastAPI , File, UploadFile ,  HTTPException , status , APIRouter
from fastapi.responses import StreamingResponse
from typing import Union
import pandas as pd
import numpy as np
from io import BytesIO
import math

from helperfunctions import annualizedVolatility , get_std_deviation

fileUploadRoute = APIRouter(prefix = "")


@fileUploadRoute .post("/uploadfile/")
async def upload_file(fileUploaded: UploadFile=File(...)):
    try : 
        filetype = fileUploaded.filename
        filetype = filetype.split('.')[-1]

        print(filetype)
        
        if filetype.strip() != 'xlsx' and filetype != 'csv' : 
            print(filetype)
            raise HTTPException(status_code= status.HTTP_400_BAD_REQUEST , detail = "Invalid File Type")

        content = fileUploaded.file.read()
        byte_data = BytesIO(content)
        data = pd.read_excel(byte_data) if filetype == 'xlsx' else pd.read_csv(byte_data)

        # cleaning filenames to remove spaces
        data.columns = data.columns.str.strip()
    except Exception as error : 
        raise(error)
    


    closingPriceList = data['Close'].values
    firstdayopening = data['Open'][0]

    previousPrice = firstdayopening
    dailyreturns = []
    for currentPrice in closingPriceList : 
        currreturn = currentPrice/previousPrice - 1
        previousPrice = currentPrice
        dailyreturns.append(currreturn)

    stdDeviation = get_std_deviation(dailyreturns)

    daily_volatility = stdDeviation
    annualized_volatility = annualizedVolatility(stdDeviation , len(dailyreturns))

    return {"daily_volatility" : daily_volatility , "annualized_volatility" : annualized_volatility}