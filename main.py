import json
import jpholiday
import datetime
import schedule
import time

from auth import Switchbot_Auth
from celing_light import CelingLight

def load_kyes():
    json_file = open("Switchbot_keys.json", "r")
    key_dict = json.load(json_file)
    return key_dict

def gradually_on(only_holiday:bool):
    today = datetime.datetime.now()
    is_holiday = jpholiday.is_holiday(today)
    if only_holiday != is_holiday:
        return
    
    key_dict = load_kyes()
    token = key_dict["token"]
    secret = key_dict["secret"]
    switchbot_auth = Switchbot_Auth(token, secret)
    apiHeader = switchbot_auth.get_apiHeader()
    celing_light = CelingLight(apiHeader)
    if celing_light.get_power() == "on":
        return
    
    brightness:int = 0
    for i in range(1, 31):
        brightness = int(100/30*i)
        if brightness > 100:
            break
        celing_light.set_brightness(brightness)
        time.sleep(60)

def main():
    schedule.every().day.at("7:00").do(gradually_on, need_holiday=False)
    schedule.every().day.at("8:30").do(gradually_on, need_holiday=True)
    while (True):
        schedule.run_pending()
        time.sleep(60)

if __name__ == "__main__":
    main()