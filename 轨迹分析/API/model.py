from fx import db


class target_rec(db.Document):
    Pin_ID= db.StringField()
    Target_IP= db.StringField()
    Target_ID= db.StringField()
    Target_Access_DT= db.StringField()
    Target_Web_live_long= db.StringField()
    Target_Rec_DT= db.StringField()
    Target_Signal= db.StringField()


class Pins_rec(db.Document):
    Pin_ID = db.StringField()
    Users = db.StringField()
    Pin_Live_long = db.StringField()
    Pin_Date_time = db.StringField()

class save(db.Document):
    name = db.StringField()
    p100 = db.StringField()
    p101 = db.StringField()
    p102 = db.StringField()
    p103 = db.StringField()
    p104 = db.StringField()
    p105 = db.StringField()
    p106 = db.StringField()
    p107 = db.StringField()
    p108 = db.StringField()
    p109 = db.StringField()
    p110 = db.StringField()
    p111 = db.StringField()
    p112 = db.StringField()
    p114 = db.StringField()
    p115 = db.StringField()
    p116 = db.StringField()
    p117 = db.StringField()
    p118 = db.StringField()

