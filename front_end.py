import requests 
from loguru import logger

res = requests.get("http://127.0.0.1:8000/users/all")
logger.info(res.status_code)
logger.info(type(res.text))
logger.info(type(res.json()[0]))