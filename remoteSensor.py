
#import time
import json
import logging
from purpleair import PurpleAir
from dotenv import load_dotenv
import os
load_dotenv()
api_key = os.getenv("READ_KEY")
sensor_id = str(152624)

# api_base_url = 'https://www.purpleair.com/json?show='
# api_url = 'https://www.purpleair.com/json?show=104402'

p = PurpleAir(api_key)


def calcAQ(Cp, Ih, Il, BPh, BPl):
    a = (Ih - Il)
    b = (BPh - BPl)
    c = (Cp - BPl)
    aq = ((a/b) * c + Il)
    return aq


def purpleAir():
    aqiColor = "#00FF00"
    api_data = ""
    error = None

    # concat base_url with selected sensor_id
    
    
    # api_url = api_base_url+sensor_id
    logging.info('retrieved sensor_id from database: ' + sensor_id)

    # PurpleAir data!
    try:
        # api_data = requests.get(api_url)
        api_data = p.get_sensor_data(sensor_id)
        logging.info('aqistore - New data received from PurpleAir api.')

        # data = json.loads(api_data.text)
        # results = data['results'][0]
        results = api_data['sensor']
        sensor_label = results['name']
        PM25 = results['pm2.5_atm']
        humidity = results['humidity']
        temp = results['temperature']
        pressure = results['pressure']

        # http://tech.thejoestory.com/2020/09/air-quality-calculation-purple-air-api.html
        pm2 = PM25

        # for row in data["results"]:
        #     pm2 = float(row["PM2_5Value"])
        #     pm2 = pm2 + pm2
        # pm2 = pm2 / 2

        if (pm2 > 350.5):
            aq = calcAQ(pm2, 500, 401, 500, 350.5)
            aqiColor = "#FF0000"
        elif (pm2 > 250.5):
            aq = calcAQ(pm2, 400, 301, 350.4, 250.5)
            aqiColor = "#FF0000"
        elif (pm2 > 150.5):
            aq = calcAQ(pm2, 300, 201, 250.4, 150.5)
            aqiColor = "#FF0000"
        elif (pm2 > 55.5):
            aq = calcAQ(pm2, 200, 151, 150.4, 55.5)
            aqiColor = "#FF0000"
        elif (pm2 > 35.5):
            aq = calcAQ(pm2, 150, 101, 55.4, 35.5)
            aqiColor = "#FF4500"
        elif (pm2 > 12.1):
            aq = calcAQ(pm2, 100, 51, 35.4, 12.1)
            aqiColor = "#FFFF00"
        elif (pm2 > 0):
            aq = calcAQ(pm2, 50, 0, 12, 0)
            aqiColor = "#00FF00"
        aqi = str(round(aq))
    except Exception as e:
        error = 'aqistore - Error getting data from PurpleAir api.'
        logging.warning(error, e)
        return

    return aqi

import time
import os
beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)

def main():

    while (1==1):
        test = int(purpleAir())
        if test > 175:
            beep(3)
            beep(3)
            beep(3)
        print(test)
        time.sleep(10)
    
if __name__ == "__main__":
    main()



