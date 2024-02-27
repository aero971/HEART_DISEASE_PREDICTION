from asyncore import readwrite
from cProfile import run
from logging import debug
import pickle
from flask import Flask,render_template,request
import numpy as np

app = Flask(__name__)
model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        age = float(request.form['age'])
        sex = float(request.form['sex'])
        chol = float(request.form['chol'])
        thalach = float(request.form['thalachh'])
        
        arr = np.array([[age, sex, chol, thalach]])
        pred = model.predict(arr)
        
        if pred == 0:
            res_Val = "NO heart problem"
        else:
            res_Val = "Heart Problem"

        return render_template('index.html', prediction_text='Patient has {}'.format(res_Val))
    
    except ValueError:
        return render_template('index.html', prediction_text='Please fill all the fields with valid numeric values.')
if __name__=='__main__':
    app.run(debug=True)