from flask import Flask,request,render_template,jsonify
#calling prediction_pipeline.py,training_pipeline.py by importing
# calling customdata, predictpipeline classes from prediction_pipeline.py
from src.pipeline.prediction_pipeline import CustomData,PredictPipeline

#create flask app
application=Flask(__name__)
# intitialize app
app=application

#create route for home page
@app.route('/')
def home_page():
    return render_template('index.html') #create templates folder for render_template to make index,result.html for files

# create methods/fun by create route
@app.route('/predict',methods=['GET','POST'])

def predict_datapoint():
    if request.method=='GET':
        return render_template('form.html')
    
    else:
        # creating dict vth numerical,catagerical values
        #using typecasting for numerical values by convert into float and no need to convert categorical values
        data=CustomData(
            carat=float(request.form.get('carat')),
            depth = float(request.form.get('depth')),
            table = float(request.form.get('table')),
            x = float(request.form.get('x')),
            y = float(request.form.get('y')),
            z = float(request.form.get('z')),
            cut = request.form.get('cut'),
            color= request.form.get('color'),
            clarity = request.form.get('clarity')
        )
        final_new_data=data.get_data_as_dataframe()
        predict_pipeline=PredictPipeline()
        pred=predict_pipeline.predict(final_new_data)

        results=round(pred[0],2)

        return render_template('results.html',final_result=results)
        





#execute flask 
if __name__=="__main__":
    app.run(host='0.0.0.0',debug=True) #default host:0.0.0.0
# we run this app.py by using and importing predict_pipeline.py,training_pipeline.py,templates files.
# browse webpage vth http://127.0.0.1:5000,and http://127.0.0.1:5000/predict.     