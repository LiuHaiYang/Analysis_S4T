from flask import Flask,jsonify,request
from flask_restful import Resource
import pymongo
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
# client = pymongo.MongoClient('172.16.100.54',27017)
# song = client['song']
# save = song['save']
db = MongoEngine(app)
manager = Manager(app)
api = Api(app)


class TrackAPI1(Resource):
    def get(self):
        print('GET start！！！')
        l=[]
        data = target_rec.objects.all().limit(5000)
        for d in  data:
            l.append(d)
        print('GET  OK！！')
        return jsonify(l)

api.add_resource(TrackAPI1,'/v1.0/data/get')


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
        print(t[0])
        for i in range(0,len(t)-1):
            save.insert_one({'name':t[i]['name'],'p100':t[i]['100'],'p101':t[i]['101'],'p102':t[i]['102'],'p103':t[i]['103'],'p104':t[i]['104'],
                             'p105':t[i]['105'],'p106':t[i]['106'],'p107':t[i]['107'],'p108':t[i]['108'],'p109':t[i]['109'],'p110':t[i]['110'],
                             'p111':t[i]['111'],'p112':t[i]['112'],'p114':t[i]['114'],'p115':t[i]['115'],'p116':t[i]['116'],'p117':t[i]['117'],
                             'p118':t[i]['118']})
        print('POST  OK!!')

api.add_resource(TrackAPI2, '/v1.0/data/save')

class TrackAPI3(Resource):
    def get(self):
        print('GET start！！！')
        l=[]
        data = save.objects.all()
        for d in  data:
            l.append(d)
        print('GET  OK！！')
        return jsonify(l)

api.add_resource(TrackAPI3,'/v1.0/data/getdata')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000)
