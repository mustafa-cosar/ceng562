import os

import pandas

FILES = [
    "../.data/accidents_2005_to_2007.csv",
    "../.data/accidents_2009_to_2011.csv",
    "../.data/accidents_2012_to_2014.csv",
]

def preprocess_accident_data():
    for csv_file in FILES:
        df = pandas.read_csv(csv_file)
        data = df[['Date', 'Day_of_Week', 'Time', '1st_Road_Class', 'Road_Type', 'Speed_limit',
        'Junction_Control', '2nd_Road_Class', 'Pedestrian_Crossing-Human_Control',
        'Pedestrian_Crossing-Physical_Facilities', 'Light_Conditions', 'Weather_Conditions', 'Road_Surface_Conditions',
        'Special_Conditions_at_Site', "Urban_or_Rural_Area"]]
        labels = df[['Police_Force', 'Accident_Severity', 'Number_of_Vehicles', 'Number_of_Casualties',]]

        with open(os.path.splitext(csv_file)[0] + "_data.csv", "w") as data_file:
            data.to_csv(data_file, sep=",", encoding="utf-8")
        with open(os.path.splitext(csv_file)[0] + "_labels.csv", "w") as labels_file:
            labels.to_csv(labels_file, sep=",", encoding="utf-8")

