from flask import Flask,request ,render_template
from src.pipeline.prediction_pipeline import CustomEntry,PredictionPipeline

app = Flask(__name__)

@app.route("/")
def get_welcome():
    return render_template('index.html')


@app.route("/prediction_result",methods=['GET','POST'])
def get_prediction_result():

    if request.method=="GET":
        return render_template('form.html')
    else:
        data  = request.form
        custom_obj = CustomEntry(data['carat'],
                                 data['cut'],data['color'],data['clarity'],
                                 data['depth'],data['table'],data['x'],
                                 data['y'],data['z'])
        df = custom_obj.get_data_frame()
        predict_obj = PredictionPipeline()
        prediction_result = predict_obj.get_predict(df)
        print()
        return render_template("result.html",final_result = round(prediction_result[0],2))
        


if __name__=="__main__":
    # app.run(debug=True,host='172.20.12.162',port=5001)
    app.run(host='0.0.0.0',port=5001)
