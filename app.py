from flask import Flask ,request,json
from facepplib import FacePP
app = Flask(__name__)

def face_comparing(app,url1,url2):

  img_url1 = url1
  img_url2 = url2
  cmp_ = app.compare.get (image_url1 = img_url1, image_url2=img_url2)
  if cmp_.confidence > 80:
    return True

def creatFacePP():
    api_key ='incwWD-Q-ILQaZJoaGXZpoC6858HuzOP'
    api_secret ='X_c2GBme53nfsBjuOd90Tldg2j0g2wWc'
    app_=FacePP(api_key=api_key,api_secret=api_secret)
    return app_
@app.route('/face',methods=['GET','POST'])
def index1():
    app_=creatFacePP()
    data = request.get_json(True,True)
    image = app_.image.get(image_url = data['photo'])
    if(len(image.faces)==0 or len(image.faces)>1):
        a=False
    else:
        a=True
    response = app.response_class(
        response=json.dumps(a),
        status=200,
        mimetype='application/json')
    return response

@app.route('/search', methods = ['GET','POST'])
def index():
    app_=creatFacePP()
    data = request.get_json(True,True)
    a=[]
    for i in  range (1,len(data)):
        x=face_comparing(app_,data[0]['photoSearch'],data[i]['photo'])
        if(x==True):
            a.append(data[i])
            
    response = app.response_class(
        response=json.dumps(a),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__== '__main__':
    app.run(debug=True)