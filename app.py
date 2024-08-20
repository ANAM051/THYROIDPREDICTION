from flask import Flask,request,render_template,jsonify

from src.pipeline.prediction_pipeline import CustomData,PredictPipeline


application=Flask(__name__)

app=application

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    else:
        data=CustomData(
           Age=int(request.form.get('Age')), # type: ignore
           TSH = float(request.form.get('TSH')), # type: ignore
           T3 = float(request.form.get('T3')), # type: ignore
           T4U = float(request.form.get('T4U')), # type: ignore
           TT4 = float(request.form.get('TT4')), # type: ignore
           FTI= float(request.form.get('FTI')), # type: ignore
           Sex=  request.form.get('Sex'), # type: ignore
           Sick= request.form.get('Sick'), # type: ignore
           Pregnant= request.form.get('Pregnant'), # type: ignore
           ThyroidSurgery= request.form.get('Thyroid Surgery'), # type: ignore
           Goitre = request.form.get('Goitre'), # type: ignore
           Tumor = request.form.get('Tumor') # type: ignore
        ) 
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)

        return render_template('results.html',final_result=results)




if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True)