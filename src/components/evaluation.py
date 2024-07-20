from src.exception import CustomException
from src.logging import logging
from sklearn.metrics import mean_absolute_error,mean_squared_error,mean_absolute_percentage_error,r2_score
import numpy as np
import sys

class ModelEvalution():
    def __init__(self) -> None:
        logging.info("Evalution Started")
    
    def eval_metrics(self,actual,pred):
        rmse = np.sqrt(mean_squared_error(actual,pred))
        mae  = mean_absolute_error(actual,pred)
        r2   = r2_score(actual,pred)
        logging.info("Evalution metrics calculated")

        return rmse,mae,r2
    
    def initiate_model_eval(self,train_arr,test_arr):
        try:
            pass
        except Exception as e:
            raise CustomException(e,sys)
