import requests

host_domain = "https://api.switch-bot.com"
device_path = host_domain + "/v1.1/devices/"
device_id = 'F833A4954FEB'

class CelingLight:
    def __init__(self, apiHeader:dict) -> None:
        self.apiHeader = apiHeader

    def get_status(self):
        status_path = device_path + device_id + '/status'
        response = requests.get(status_path, headers=self.apiHeader)
        json_data = response.json()
        device_stat = json_data['body']
        return device_stat
    
    def get_power(self):
        device_stat = self.get_status()
        return device_stat["power"]

    def get_brightness(self):
        device_stat = self.get_status()
        return device_stat["brightness"]
    
    def get_color_temperatures(self):
        device_stat = self.get_status()
        return device_stat["colorTemperature"]
    
    def turn_on(self):
        conrtol_path = device_path + device_id + '/commands'
        post_json = {
            'command': "turnOn",
            "parameter": "default",
            "commandType": "command"
        }
        respone = requests.post(url=conrtol_path, headers=self.apiHeader, json=post_json)
    
    def turn_off(self):
        conrtol_path = device_path + device_id + '/commands'
        post_json = {
            'command': "turnOff",
            "parameter": "default",
            "commandType": "command"
        }
        respone = requests.post(url=conrtol_path, headers=self.apiHeader, json=post_json)
    
    def set_color_temperatures(self, degree:int):
        conrtol_path = device_path + device_id + '/commands'
        degree = str(degree)
        if degree < 2700 or degree > 6500:
            print("invalid color temperature")
            return
        post_json = {
            'command': "setColorTemperature",
            "parameter": degree,
            "commandType": "command"
        }
        respone = requests.post(url=conrtol_path, headers=self.apiHeader, json=post_json)
    
    def set_brightness(self, degree:int):
        conrtol_path = device_path + device_id + '/commands'
        if degree < 1 or degree > 100:
            print("invalid brightnes")
            return
        degree = str(degree)
        post_json = {
            'command': "setBrightness",
            "parameter": degree,
            "commandType": "command"
        }
        respone = requests.post(url=conrtol_path, headers=self.apiHeader, json=post_json)