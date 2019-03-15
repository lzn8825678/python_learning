import json
import requests
import base64


def get_token():
    host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=XU7gG2ogGrqG69L3RGBQmwEq&client_secret=UUo2ltfe8PS7odOimMx4S9z6m1Tq1iH1'
    request = requests.get(host).content.decode()
    request =eval(request[:-1])
    return request['access_token']

def imgdata(file1,file2):
    with open(file1,"rb") as f:
        pic1 = base64.b64encode(f.read())
    with open(file2,"rb") as f:
        pic2 = base64.b64encode(f.read())

    params = json.dumps([
        {"image":str(pic1,'utf-8'),"image_type":"BASE64","face_type":"LIVE","quality_control":"LOW"},
        {"image":str(pic2,'utf-8'),"image_type":"BASE64","face_type":"IDCARD","quality_control":"LOW"},
    ])
    return params.encode()

def img(file1,file2):
    print("开始识别")
    token = get_token()
    params = imgdata(file1,file2)
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/match" + "?access_token=" + token
    content = requests.post(request_url,data=params).content
    content = eval(content)
    score = content['result']['score']
    if score > 70:
        return "相似度" + str(score) + ",同一个人"
    else:
        return "相似度" + str(score) + ",不是同一个人"


if __name__ == "__main__":
    print(get_token())
    print(imgdata("img1.jpg","img2.jpg"))
    print(img("img1.jpg","img2.jpg"))