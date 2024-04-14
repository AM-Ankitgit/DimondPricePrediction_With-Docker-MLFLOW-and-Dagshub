import os
from pathlib import Path


package_name = 'mongodb_connect'

list_of_files = [
    '.github/workflows/ci.yaml',# this folder for entire configuration of CI/CD pipeline
     # git keep for to push empty folder over the github
    'src/__init__.py',
    f'src/{package_name}/__init__.py',
    f'src/{package_name}/mongo_crud.py',
    'src/components/__init__.py',
    'src/components/data_ingestion.py',
    'src/components/data_transformation.py',
    'src/components/model_trainer.py',
    'src/components/evaluation.py',
    'src/pipeline/__init__.py',
    'src/pipeline/training_pipeline.py',
    'src/pipeline/prediction_pipeline.py',
    'src/utils/__init__.py',
    'src/utils/utils.py', # for utility
    'src/logger/logging.py',
    'src/exception/exception.py',
    'tests/unit/__init__.py',
    'tests/unit/unit.py',
    'tests/integration/__init__.py',
    'init_setup.sh',
    'requirements.txt', # production
    'requirements_dev.txt', 
    'setup.py',
    'setup.cfg',
    'pyproject.toml',
    'tox.ini',     # test different test-case in local development env 
    'experiment/experiments.ipynb',
]

for filepath in list_of_files:
    filepath = Path(filepath)
    file__dir ,file_name = os.path.split(filepath)

    if file__dir!="": # becuase in above list we mention file name only then file_dir will empty
        #this line code will create folder for files
        os.makedirs(file__dir,exist_ok=True)  

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath))==0:
        # create file with extension (for file folder already crated in above code)
        with open(filepath,'w') as f:
            pass