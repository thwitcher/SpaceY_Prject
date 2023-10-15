import sqlite3
import csv
import pandas as pd
import re
con = sqlite3.connect("my_data1.db")
cur = con.cursor()
df = pd.read_csv("https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBM-DS0321EN-SkillsNetwork/labs/module_2/data/Spacex.csv")
df.to_sql("SPACEXTBL", con, if_exists='replace', index=False,method="multi")
cur.execute('''CREATE TABLE IF NOT EXISTS SPACEXTABLE as select * from SPACEXTBL where Date is not null''')

cur.execute('SELECT DISTINCT Launch_Site from SPACEXTABLE ')
launch_site = cur.fetchall()

for row in launch_site:
    print(row)

print("second result begins with CCA")
for row in launch_site:
    if row[0].startswith('CCA') :
        print(row)

cur.execute('SELECT PAYLOAD_MASS__KG_ from SPACEXTABLE ')
payload_mass = cur.fetchall()
totalPM=0
for number in payload_mass:
    totalPM += int(number[0])
print("total payload mass =")
print(totalPM)
cur.execute('''SELECT PAYLOAD_MASS__KG_ from SPACEXTABLE where Booster_version = 'F9 v1.1' ''')
F9_numb = cur.fetchall()
averageF9=0
lenght = 0
for number in F9_numb:
    lenght +=1
    averageF9 += int(number[0])
print("average F9=")
print(int(averageF9/lenght))
cur.execute('''SELECT  Date from SPACEXTABLE WHERE Landing_Outcome='Success (ground pad)' LIMIT 1 ''')
dateF = cur.fetchall()
if dateF:
    # Access the first element of the list
    first_success_date = dateF[0][0]
    print("First success date is:", first_success_date)
else:
    print("No success date found.")
cur.execute('''SELECT DISTINCT Booster_Version from SPACEXTABLE WHERE (PAYLOAD_MASS__KG_ > 4000 and PAYLOAD_MASS__KG_ < 6000)''')
SpeBosst = cur.fetchall()
for speboost in SpeBosst:
    print(speboost)

cur.execute('SELECT Landing_Outcome from SPACEXTABLE')
sucR=0
failR=0
landing_outcome=cur.fetchall()
patternS= r'^Success*'
patternF= r'^Failure*'
for i in landing_outcome:
  
    if re.match(patternS, str(i[0])):
        sucR +=1
    elif re.match(patternF, str(i[0])):
        failR +=1
    else : 
        continue
print("sucess rate")
print(sucR)
print("fail rate")
print(failR)
cur.execute('SELECT MAX(PAYLOAD_MASS__KG_) FROM SPACEXTABLE')
maxPLM = cur.fetchall()
maxx=maxPLM[0][0]
cur.execute('''SELECT DISTINCT Booster_Version from SPACEXTABLE WHERE PAYLOAD_MASS__KG_ = ?''',(maxx,))
SpeBosstMx = cur.fetchall()
print(SpeBosstMx)
cur.execute('''SELECT strftime('%m', MIN(Date)) FROM SPACEXTBL WHERE Landing_Outcome = 'Success (ground pad)';''')
fiva = cur.fetchall()
print(fiva)