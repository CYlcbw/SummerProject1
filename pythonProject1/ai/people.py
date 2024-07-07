import requests
import base64
import cv2 as cv

api_key = "Mzd6LXIklApGihcI0VqrBl2Z"
secret_key = "r5mdaJ2tPHI51CT6nsPdHCar1KCiVzJB"

def get_access_token(api_key, secret_key):
    token_url = "https://aip.baidubce.com/oauth/2.0/token"
    params = {
        "grant_type": "client_credentials",
        "client_id": api_key,
        "client_secret": secret_key
    }
    response = requests.post(token_url, params=params)
    if response:
        return response.json().get("access_token")
    return None

def people_detect(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image).decode('utf-8')
    params = {"image": base64_image}
    access_token = get_access_token(api_key, secret_key)
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    num = 0
    if response:
        data = response.json()
        print(data)
        if 'person_info' in data:
            person_info = data['person_info']
            num = len(person_info)
            for item in person_info:
                location = item['location']
                x1 = location['left']
                y1 = location['top']
                x2 = x1 + location['width']
                y2 = y1 + location['height']
                cv.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                text = "Person"
                position = (x1, y1 - 2)
                font = cv.FONT_HERSHEY_SIMPLEX
                font_scale = 1
                color = (0, 255, 0)  # Green
                thickness = 2
                img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)
        else:
            print("No people detected")
    return img, num
