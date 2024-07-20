import mlflow

def get_cal(a,b,operation=None):
    if operation=='sum':
        return (a+b)
    if operation=='mul':
        return a*b

if __name__ =="__main__":

    a,b,opt = 2,6,'sum'
    with mlflow.start_run():
        result = get_cal(a,b,opt)
        mlflow.log_param("value of a",a)
        mlflow.log_param("value of b",b)
        mlflow.log_param("value of opt",opt)
        mlflow.log_param("Result of opt",result)


