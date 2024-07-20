import logging
import os
from datetime import datetime

log_file_name = os.path.join(datetime.now().strftime("%Y-%m-%d-%H-%M-%S")+".log")

folder_path = os.path.join(os.getcwd(),"LOG")
os.makedirs(folder_path,exist_ok=True)

log_file_full_path = os.path.join(folder_path,log_file_name)

logging.basicConfig(
    level= logging.INFO,
    filename=log_file_full_path,
    format= "[%(asctime)s] %(lineno)d %(name)s - %(levelname)s - %(message)s",
    
)



