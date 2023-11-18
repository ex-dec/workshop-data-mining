# 1. Library imports
import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
import uvicorn

# 2. Create the app object
app = FastAPI()

#. Load trained Pipeline
model = load_model('income')

# Define predict function
@app.get('/income')
def predict(age, workclass, education, education_num, marital_status, occupation, relationship, race, sex, capital_gain, capital_loss, hours_per_week, native_country):
    data = pd.DataFrame([[age, workclass, education, education_num, marital_status, occupation, relationship, race, sex, capital_gain, capital_loss, hours_per_week, native_country]])
    data.columns = ['age', 'workclass', 'education', 'education_num', 'marital_status', 'occupation', 'relationship', 'race', 'sex', 'capital_gain', 'capital_loss', 'hours_per_week', 'native_country']

    predictions = predict_model(model, data=data) 
    return {'prediction': int(predictions['prediction_label'][0])}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8787)