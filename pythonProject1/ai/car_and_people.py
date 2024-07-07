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


def detect_people_and_vehicles(img):
    access_token = get_access_token(api_key, secret_key)

    # Vehicle detection
    vehicle_request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/vehicle_detect"
    _, encoded_image = cv.imencode('.jpg', img)
    base64_image = base64.b64encode(encoded_image).decode('utf-8')
    vehicle_params = {"image": base64_image}
    vehicle_request_url = vehicle_request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    vehicle_response = requests.post(vehicle_request_url, data=vehicle_params, headers=headers)
    vehicle_info = []
    vehicle_num = {'car': 0, 'tricycle': 0, 'motorbike': 0, 'bus': 0, 'truck': 0, 'carplate': 0}
    if vehicle_response:
        vehicle_data = vehicle_response.json()
        vehicle_num.update(vehicle_data.get('vehicle_num', {}))
        vehicle_info = vehicle_data.get('vehicle_info', [])
        for item in vehicle_info:
            location = item['location']
            x1 = location['left']
            y1 = location['top']
            x2 = x1 + location['width']
            y2 = y1 + location['height']
            cv.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
            text = item['type']
            position = (x1, y1 - 2)
            font = cv.FONT_HERSHEY_SIMPLEX
            font_scale = 1
            color = (0, 0, 255)  # Red
            thickness = 2
            img = cv.putText(img, text, position, font, font_scale, color, thickness, cv.LINE_AA)

    # People detection
    people_request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_attr"
    people_params = {"image": base64_image}
    people_request_url = people_request_url + "?access_token=" + access_token
    people_response = requests.post(people_request_url, data=people_params, headers=headers)
    people_num = 0
    if people_response:
        people_data = people_response.json()
        print(people_data)
        person_info = people_data.get('person_info', [])
        people_num = len(person_info)
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

    return img, vehicle_num, people_num, vehicle_info

# Example usage
# img = cv.imread('path_to_your_image.jpg')
# result_img, people_count, vehicle_count = detect_people_and_vehicles(img)
# cv.imshow('Detected People and Vehicles', result_img)
# cv.waitKey(0)
# cv.destroyAllWindows()
