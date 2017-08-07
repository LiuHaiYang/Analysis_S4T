from flask import Flask,jsonify,request
from flask_restful import Resource
import pandas as pd
from flask_script import Manager
from flask_restful import Api
from flask_mongoengine import MongoEngine
from model import *

app = Flask(__name__)
app.config['MONGODB_SETTINGS'] = {
    "host": '172.16.100.54',
    "port": 27017,
    "db": 'song'
}

db = MongoEngine(app)
manager = Manager(app)
api = Api(app)


class TrackAPI1(Resource): #获取数据库
    def get(self,source,start,end):
        if source=='target_rec':
            print('GET start！！！')
            l=[]
            f = []
            users = target_rec.objects.all()
            it=0
            for data in users:
                 if pd.to_datetime(data.Target_Access_DT)>pd.to_datetime(start)  and pd.to_datetime(data.Target_Access_DT) < pd.to_datetime(end):
                     l.append(data)
                 elif  pd.to_datetime(data.Target_Access_DT) > pd.to_datetime(end):
                     it +=1
                     if it>50:
                         break
            print('GET  OK！！')
            return jsonify(l)
        elif source=='Pins_rec':
            t=[]
            pins = Pins_rec.objects.all()
            for pin in pins:
                if pd.to_datetime(pin.Pin_Date_time) > pd.to_datetime(start) and pd.to_datetime(pin.Pin_Date_time) < pd.to_datetime(end):
                    t.append(pin)
            return jsonify(t)

api.add_resource(TrackAPI1,'/v1.0/data/input/<string:source>/<string:start>/<string:end>')


class TrackAPI2(Resource):
    def post(self):
        data = pd.DataFrame(request.json)
        print('POST start!!!')
        data1 = data[data['Target_Signal'] != '0']
        data2 = data1.groupby([data1['Target_ID'], data1['Pin_ID']]).size().unstack().fillna(value=0)
        q = []
        k = []
        t = []
        for i in data2.columns:
            q.append(i)
        for i in data2.index:
            k.append(i)
        it = 0
        for i in data2.values:
            l = {}
            for raw in range(0, len(i)):
                l[q[raw]] = i[raw]
            l['name'] = k[it]
            it += 1
            t.append(l)
        print('POST  OK!!')
        return jsonify(t)

api.add_resource(TrackAPI2, '/v1.0/data/trace')
if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
