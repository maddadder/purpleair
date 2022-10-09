from purpleAirData import purpleAirData
import time
import os
beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)

def main():
    conditions = []
    for condition in purpleAirData.conditions:
        conditions.append(condition)
    pad = purpleAirData("http://192.168.1.129/json", 30, conditions)

    while (1==1):
        try:
            readings = pad.readings
            aqi = readings["pm2.5_aqi"]
            print(aqi)
            beep(int(aqi // 10))
            print(readings)
        except:
            print(readings)
            beep(10)
        finally:
            time.sleep(60)
    
if __name__ == "__main__":
    main()
