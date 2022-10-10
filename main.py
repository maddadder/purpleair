from purpleAirData import purpleAirData
import time
import os
beep = lambda x: os.system("echo -n '\a';sleep 0.2;" * x)

def main():

    conditions = []
    for condition in purpleAirData.conditions:
        conditions.append(condition)
    pad = purpleAirData("http://192.168.1.129/json", 30, conditions)

    from datetime import datetime
    from matplotlib import pyplot
    from matplotlib.animation import FuncAnimation

    def update(frame):
        try:
            readings = pad.readings
            sample = readings["pm2.5_aqi"]
            print(sample)
            beep(int(sample // 10))
            print(readings)
            x_data.append(datetime.now())
            y_data.append(sample)
            line.set_data(x_data, y_data)
            figure.gca().relim()
            figure.gca().autoscale_view()
            return line,
        except:
            beep(10)

        
    x_data, y_data = [], []

    figure = pyplot.figure()
    line, = pyplot.plot_date(x_data, y_data, '-')
    # update every 10 minutes
    animation = FuncAnimation(figure, update, interval=(1000 * 60))
    pyplot.show()
    
if __name__ == "__main__":
    main()
