from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import json
import logging
from datetime import datetime
import random

# JSONResponse с отключённым ASCII
class CustomJSONResponse(JSONResponse):
    def render(self, content: any) -> bytes:
        return json.dumps(content, ensure_ascii=False).encode("utf-8")

app = FastAPI(default_response_class=CustomJSONResponse)

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

@app.get("/")
async def root(request: Request):
    logging.info(f"Request to / from {request.client.host}")
    return {"message": "Привет! Сейчас " + datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

@app.get("/random")
async def get_random():
    number = random.randint(1, 100)
    logging.info(f"Generated random number: {number}")
    return {"random_number": number}
