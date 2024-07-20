from src.logging import logging
from src.exception import CustomException
import sys
try:
    1/0
except Exception as e:
    raise CustomException(e,sys)
