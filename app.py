from flask import Flask

app = Flask(__name__)

def face_comparing(app,url1,url2):

  img_url1 = url1
  img_url2 = url2

  cmp_ = app.compare.get (image_url1 = img_url1, image_url2=img_url2)
 

  if cmp_.confidence > 80:
    return True

@app.route('/in', methods = ['GET''POST'])
def index():
    api_key ='incwWD-Q-ILQaZJoaGXZpoC6858HuzOP'
    api_secret ='X_c2GBme53nfsBjuOd90Tldg2j0g2wWc'
    app_=FacePP(api_key=api_key,api_secret=api_secret)
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