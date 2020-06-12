from flask import Flask, render_template, g, request
import pickle
import pandas as pd
import numpy as np

app = Flask(__name__)



@app.route('/', methods=['POST'])
def index():
    new_data=request.get_json()
    t=new_data['t']
    dis=new_data['dis']
    f=new_data['f']
    my=new_data['my']
    data = {'Distance(km)':[float(dis)],'Fuel':[float(f)],'Manufacturing Year':[float(my)]}
    df = pd.DataFrame(data)
    name="model_"+t
    with open('./models/'+name,'rb') as f:
        mp=pickle.load(f)
    ans=mp.predict(df)[0]
    return '{}'.format(ans)

if __name__ == '__main__':
    app.run(debug=True)