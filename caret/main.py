# 1. Library imports
import pandas as pd
from pycaret.classification import load_model, predict_model
from fastapi import FastAPI
import uvicorn

# 2. Create the app object
app = FastAPI()

#. Load trained Pipeline
model = load_model('telescope')

# Define predict function
@app.get('/telescope')
def predict(fLength, fWidth, fSize, fConc, fConcl, fAsym, fM3Long, fM3Trans, fAlpha, fDist):
    data = pd.DataFrame([[fLength, fWidth, fSize, fConc, fConcl, fAsym, fM3Long, fM3Trans, fAlpha, fDist]])
    data.columns = ['fLength', 'fWidth', 'fSize', 'fConc', 'fConcl', 'fAsym', 'fM3Long', 'fM3Trans', 'fAlpha', 'fDist']

    predictions = predict_model(model, data=data) 
    return {'prediction': int(predictions['prediction_label'][0])}

if __name__ == '__main__':
    uvicorn.run(app, host='127.0.0.1', port=8787)