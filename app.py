from flask import Flask, request, jsonify
import pickle
import numpy as np
import pandas as pd





#Create a flask instance
app = Flask(__name__)
print(__name__)

model_pickle = open('./artifacts/xgb_model.pkl', 'rb')
model = pickle.load(model_pickle)

means_pkl = open('./artifacts/other_feature_means.pkl', 'rb')
other_feature_means = pickle.load(means_pkl)

service_te_map_pkl = open('./artifacts/service_te_map.pkl', 'rb')
service_te_map = pickle.load(service_te_map_pkl)

feature_names_pkl = open('./artifacts/feature_names.pkl', 'rb')
feature_names = pickle.load(feature_names_pkl)
    
top_5_features = ['service', 'total_bytes', 'lastflag', 'log_srcbytes', 'count']

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json(force=True)
    service_name = data['service']
    data['service'] = service_te_map[service_name]
    
    srcbytes_value = data['log_srcbytes']
    data['log_srcbytes'] = np.log1p(srcbytes_value)
    
    full_data = {**data, **other_feature_means}
    
    
    df_input = pd.DataFrame(full_data, index=[0])
    df_input = df_input[feature_names]
    
    prediction = model.predict(df_input)
    
    if prediction == 0:
        pred = 'Normal'
    else:
        pred = 'Attack'
    
    return {'prediction': pred}
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)