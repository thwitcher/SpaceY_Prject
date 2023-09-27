import requests
import pandas as pd
import numpy as np
import datetime
import json 
from bs4 import BeautifulSoup
import requests
BoosterVersion = []
PayloadMass = []
Orbit = []
LaunchSite = []
Outcome = []
Flights = []
GridFins = []
Reused = []
Legs = []
LandingPad = []
Block = []
ReusedCount = []
Serial = []
Longitude = []
Latitude = []



pd.set_option('display.max_columns', None)
pd.set_option('display.max_colwidth', None)


 

def getBoosterVersion(data):
    global BoosterVersion
    y = []
    for x in data['rocket']:
        try:
            if x:
                if y == x :
                    continue
                else:       

                    print(f"Fetching data for rocket {x}")
                    response = requests.get("https://api.spacexdata.com/v4/rockets/" + str(x)).json()
                    
                   
                    BoosterVersion.append(response['name'])
                    print(f"Appended {response['name']} to BoosterVersion")
                    y = x 
                
        except Exception as e:
            print(f"An error occurred: {e}")
        
def getLaunchSite(data):
    y = []
    global Longitude
    global Latitude
    global LaunchSite
    for x in data['launchpad'] :
        try :
            if x:
                if y == x :
                    continue
                else: 
                    response = requests.get("https://api.spacexdata.com/v4/launchpads/"+str(x)).json()
                    Longitude.append(response['longitude'])
                    Latitude.append(response['latitude'])
                    LaunchSite.append(response['name'])
                    y = x
        except Exception as e:
            print("An error occurred: {e}")
        
def getPayloadData(data):
    global PayloadMass
    y = []
    for load in data['payloads']:
        if load:
            if y == load :
                continue
            else:
                response = requests.get("https://api.spacexdata.com/v4/payloads/"+load).json()
                PayloadMass.append(response['mass_kg'])
                Orbit.append(response['orbit'])
                y = load
                print("YESS")
        
        
def getCoreData(data):
    global Outcome
    global Flights
    global GridFins
    global Reused
    global Legs
    global LandingPad
    for core in data['cores']:
            if core['core'] != None:
                response = requests.get("https://api.spacexdata.com/v4/cores/"+core['core']).json()
                Block.append(response['block'])
                ReusedCount.append(response['reuse_count'])
                Serial.append(response['serial'])
            else:
                Block.append(None)
                ReusedCount.append(None)
                Serial.append(None)
            Outcome.append(str(core['landing_success'])+' '+str(core['landing_type']))
            Flights.append(core['flight'])
            GridFins.append(core['gridfins'])
            Reused.append(core['reused'])
            Legs.append(core['legs'])
            LandingPad.append(core['landpad'])
        
            
            
    




spacex_url="https://api.spacexdata.com/v4/launches/past"
response = requests.get(spacex_url)
print("connection check", response)
df = json.loads(response.text)

data = pd.json_normalize(df)



#cleaning the data

data = data[['rocket', 'payloads', 'launchpad', 'cores', 'flight_number', 'date_utc']]
data = data[data['cores'].map(len)==1]
data = data[data['payloads'].map(len)==1]
data['cores'] = data['cores'].map(lambda x : x[0])
data['payloads'] = data['payloads'].map(lambda x : x[0])
data['date'] = pd.to_datetime(data['date_utc']).dt.date
data = data[data['date'] <= datetime.date(2020, 11, 13)]
print("0000000000000000000000000000000000000000000000000000000000000000")

getBoosterVersion(data)
getLaunchSite(data)
getPayloadData(data)
getCoreData(data)



print("@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")


# Ensure all lists have the same length
data_length = len(data['flight_number'])  # Assuming 'flight_number' is one of your lists

# Define the lists with the correct length
FlightNumber = list(data['flight_number'])
Date = list(data['date'])
BoosterVersion = [''] * data_length  # Placeholder, replace with your actual data
payloads = [0.0] * data_length  # Placeholder, replace with your actual data
Orbit = [''] * data_length  # Placeholder, replace with your actual data
LaunchSite = [''] * data_length  # Placeholder, replace with your actual data
Outcome = [''] * data_length  # Placeholder, replace with your actual data
Flights = [0] * data_length  # Placeholder, replace with your actual data
GridFins = [''] * data_length  # Placeholder, replace with your actual data
Reused = [''] * data_length  # Placeholder, replace with your actual data
Legs = [''] * data_length  # Placeholder, replace with your actual data
LandingPad = [''] * data_length  # Placeholder, replace with your actual data
Block = [0] * data_length  # Placeholder, replace with your actual data
ReusedCount = [0] * data_length  # Placeholder, replace with your actual data
Serial = [''] * data_length  # Placeholder, replace with your actual data
Longitude = [0.0] * data_length  # Placeholder, replace with your actual data
Latitude = [0.0] * data_length  # Placeholder, replace with your actual data

# Create the DataFrame
launch_dict = {
    'FlightNumber': FlightNumber,
    'Date': Date,
    'BoosterVersion': BoosterVersion,
    'PayloadMass': payloads,
    'Orbit': Orbit,
    'LaunchSite': LaunchSite,
    'Outcome': Outcome,
    'Flights': Flights,
    'GridFins': GridFins,
    'Reused': Reused,
    'Legs': Legs,
    'LandingPad': LandingPad,
    'Block': Block,
    'ReusedCount': ReusedCount,
    'Serial': Serial,
    'Longitude': Longitude,
    'Latitude': Latitude
}



data_falcon9 = [] 

# Filter out rows related to "Falcon 1" rocket
data_falcon9 = data[data['rocket'] != 'Falcon 1']
print(data_falcon9)
# Reset the index of the filtered DataFrame
data_falcon9.reset_index(drop=True, inplace=True)

data_falcon9 = pd.DataFrame(data_falcon9)

data_falcon9.loc[:,'FlightNumber'] = list(range(1, data_falcon9.shape[0]+1))
data_falcon9.isnull().sum()
# Calculate the mean of the 'PayloadMass' column on the filtered DataFrame

# Filter out rows where 'PayloadMass' is not numeric
data_falcon9['payloads'] = pd.to_numeric(data_falcon9['payloads'], errors='coerce')

# Calculate the mean of the 'PayloadMass' column
payload_mass_mean = data_falcon9['payloads'].mean()

# Replace NaN values in the 'PayloadMass' column with the calculated mean

data_falcon9['payloads'].fillna(payload_mass_mean, inplace=True)

data_falcon9.to_csv('dataset_part_2.csv', index=False)


