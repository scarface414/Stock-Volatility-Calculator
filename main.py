from fastapi import FastAPI
from uploadroute import fileUploadRoute

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
app.include_router(fileUploadRoute)

origins = [
    "http://localhost.tiangolo.com",
    "https://localhost.tiangolo.com",
    "http://localhost",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
