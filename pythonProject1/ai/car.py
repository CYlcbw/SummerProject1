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

def vehicle_detect(img):
    request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image).decode('utf-8')
    params = {"image": base64_image}
    access_token = get_access_token(api_key, secret_key)
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    vehicle_num = {'car': 0, 'tricycle': 0, 'motorbike': 0, 'bus': 0, 'truck': 0, 'carplate': 0}
    vehicle_info = []
    if response:
        data = response.json()
        vehicle_num.update(data.get('vehicle_num', {}))
        vehicle_info = data.get('vehicle_info', [])
        for item in vehicle_info:
            location = item['location']
            x1 = location['left']
            y1 = location['top']
            x2 = x1 + location['width']
            y2 = y1 + location['height']
            color = (0, 0, 255)  # Red for all vehicles

            cv.rectangle(img, (x1, y1), (x2, y2), color, 2)
            text = item['type']
            position = (x1, y1 - 2)
            font = cv.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            thickness = 2
            img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)
    return img, vehicle_num, vehicle_info

def detect_plate_from_image(img, target_plate):
    access_token = get_access_token(api_key, secret_key)
    if not access_token:
        print("Failed to obtain access token")
        return False

    url = "https://aip.baidubce.com/rest/2.0/ocr/v1/license_plate"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image).decode('utf-8')
    payload = {
        'image': base64_image,
        'multi_detect': 'false'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded',
        'Accept': 'application/json'
    }

    request_url = f"{url}?access_token={access_token}"
    response = requests.post(request_url, headers=headers, data=payload)
    print("Response JSON:", response.json())
    if response:
        result = response.json()
        if 'words_result' in result:
            plate_info = result['words_result']
            if plate_info['number'] == target_plate:
                return True
    return False