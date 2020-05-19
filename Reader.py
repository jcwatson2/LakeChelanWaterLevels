
from Data_Parser import Data_Parser
from matplotlib import pyplot as plt
import pandas as pd

# options
print("1: Current Lake Level")
print("2: Lake Level Trends")
option = input("Enter an option: ")

# display the current lake level
if option is '1':
    current_level = Data_Parser('2020-5-18', '2020-5-18')
    current_level.parse()
    print("Date: " + current_level.date_list.__getitem__(len(current_level.date_list)-1))
    print("Time: " + current_level.entry_list.__getitem__(len(current_level.entry_list)-1).time)
    print("Level: " + current_level.entry_list.__getitem__(len(current_level.entry_list)-1).level)

# display trend in lake levels
elif option is '2':
    start_date = input("Start Date: ")
    end_date = input("End Date: ")
    level_trend = Data_Parser(start_date, end_date)
    level_trend.parse()
    levels = list()
    for entry in level_trend.entry_list:
        levels.append(float(entry.level))

    data_frame = pd.DataFrame(list(zip(level_trend.date_list, levels)), columns=['Date', 'Level'])
    data_frame.plot()
    plt.show()
