from src.exception import CustomException
from src.logging import logging
from sklearn.metrics import mean_absolute_error,mean_squared_error,mean_absolute_percentage_error,r2_score
import numpy as np
import sys
import os
from src.utils.utils import load_model
from urllib.parse import urlparse
import mlflow.sklearn 

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
            X_train,y_train = train_arr[:,:-1],train_arr[:,-1:]
            preprocessor_object  = os.path.join('artifact','preprocessor.pkl')
            model_path  = os.path.join('artifact','model.pkl')
            
            # preprocessor = load_model(preprocessor_object) # preprocessor object not need because we already done preprocessing and store in train test array
            model = load_model(model_path)

            logging.info("model has register")
            tracking_url_type_score = urlparse(mlflow.get_tracking_uri()).scheme
            print(tracking_url_type_score)  # output is file

            with mlflow.start_run():
                prediction = model.predict(X_train)

                # get evalution matrix result
                rmse,mae,r2 = self.eval_metrics(y_train,prediction)
                mlflow.log_param("rmse",rmse)
                mlflow.log_param("mae",mae)
                mlflow.log_param("r2",r2)

                if tracking_url_type_score!="file":
                    # Register the model
                    # There are other ways to use the Model Registry, which depends on the use case,
                    # please refer to the doc for more information:
                    # https://mlflow.org/docs/latest/model-registry.html#api-workflow
                    mlflow.sklearn.log_model(model, "model", registered_model_name="ml_model")
                else:
                    mlflow.sklearn.log_model(model, "model")

            


            
        
            
            
        except Exception as e:
            raise CustomException(e,sys)



