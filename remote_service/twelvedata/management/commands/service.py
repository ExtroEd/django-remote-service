import json


class ApplicationService:
    BASE_URL = "http://89.116.23.207:8000/api/"

    def __init__(self, service_id):
        self.service_id = service_id

    def create_application(self, requests=None):
        endpoint = f"{self.BASE_URL}/applications/?service_id={self.service_id}"
        request_body = {
            "name": "string",
            "surname": "string",
            "phone_number": "string",
            "email": "user@example.com",
            "address": "string",
            "selected_service_option": 1
        }
        headers = {
            "accept": "application / json",
            "Content-Type": "application/json",
            "X-CSRFToken": "0TOK3AA3n34NMfwpJPiYXD40Jg0Qc8RI1VH0KxmZRtYQMa8DtvmIpjXNrdxMjLCY",
        }
        response = requests.post(endpoint, headers=headers, json=request_body)
        print(response.status_code)
        try:
            response_text = response.content.decode('utf-8-sig')
            response_json = json.loads(response_text)
        except json.JSONDecodeError as e:
            raise Exception(f"Ошибка декодирования JSON: {str(e)}. Raw content: {response_text}")
        print(response_json)
        return response_text
    