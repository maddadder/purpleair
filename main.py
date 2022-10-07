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
        print(pad.readings["pm2.5_aqi"])
        if pad.readings["pm2.5_aqi"] > 10:
            beep(3)
        print(pad.readings)
        time.sleep(10)
    
if __name__ == "__main__":
    main()
