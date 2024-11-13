from typing import Optional
from fastapi import FastAPI
import datetime

app = FastAPI()

@app.get("/")
def now():
    return {"Now": datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}