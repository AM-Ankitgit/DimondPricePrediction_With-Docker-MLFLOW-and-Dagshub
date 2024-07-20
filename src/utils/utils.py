import pickle
from src.exception import CustomException
from src.logging import logging

from sklearn.metrics import r2_score, mean_absolute_error,mean_squared_error
import os,sys


def save_object(file_path,model):
    print(file_path)
    # if file_path not in os.path.exists(file_path)
    with open(file_path,'wb') as file:
        pickle.dump(model,file)

def load_model(file_path):
    with open(file_path,'rb') as f: 
        return pickle.load(f)







def evaluate_model(X_train,y_train,X_test,y_test,models):
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            # Train model
            model.fit(X_train,y_train)

            

            # Predict Testing data
            y_test_pred =model.predict(X_test)

            # Get R2 scores for train and test data
            #train_model_score = r2_score(ytrain,y_train_pred)
            test_model_score = r2_score(y_test,y_test_pred)

            report[list(models.keys())[i]] =  test_model_score

        return report

    except Exception as e:
        logging.info('Exception occured during model training')
        raise CustomException(e,sys)