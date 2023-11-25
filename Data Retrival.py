#IMPORTING REQUIRED lIBRARIES
import pandas as pd
import json
import os
os.environ["GIT_PYTHON_REFRESH"] = "quiet"
import mysql.connector
#IMPORTING AGGREGATED TRANSACTION DATA INTO DATAFRAME
path = r'D:\\project\\Phone_pe\\data\\aggregated\\transaction\\country\\india\\state\\'

file_st= os.listdir(path)

Data={"state":[],"year":[],"Quater":[],"Transaction_type":[],"Transaction_count":[],"Transaction_amount":[]}
for state in file_st:
    file_states=path+state+'\\'
    file_yr=os.listdir(file_states)
    for year in file_yr:
        file_year=file_states+year+'\\'
        file_j=os.listdir(file_year)
        for file in file_j:
            file_json=file_year+file
            f=open(file_json,"r")
            End=json.load(f)
            for i in End["data"]["transactionData"]:
                Data["Transaction_type"].append(i["name"])
                Data["Transaction_count"].append(i["paymentInstruments"][0]["count"])
                Data["Transaction_amount"].append(i["paymentInstruments"][0]["amount"])
                Data["state"].append(state)
                Data["year"].append(year)
                Data["Quater"].append(int(file.strip('.json')))
        df_agg_tran=pd.DataFrame(Data)
        df_agg_tran.shape
#IMPORTING AGGREGATED USER DATA INTO DATAFRAME
path1 = r'D:\\project\\Phone_pe\\data\\aggregated\\user\\country\\india\state\\'

agg_user=os.listdir(path1)

Data1={"state":[],"year":[],"Quater":[],"Brands":[],"count":[],"Percentage":[]}
for state in agg_user:
    agg_states=path1+state+"\\"
    agg_yr=os.listdir(agg_states)
    for year in agg_yr:
        agg_years=agg_states+year+"\\"
        agg_j=os.listdir(agg_years)
        for file in agg_j:
            agg_file=agg_years+file
            agg_json=open(agg_file,"r")
            st=json.load(agg_json)
            try:
                for i in st["data"]["usersByDevice"]:
                    Data1["Brands"].append(i["brand"])
                    Data1["count"].append(i["count"])
                    Data1["Percentage"].append(i["percentage"])
                    Data1["state"].append(state)
                    Data1["year"].append(year)
                    Data1["Quater"].append(int(file.strip('.json')))
            except:
                pass
df_agg_usr=pd.DataFrame(Data1)
# IMPORTING MAP TRANSACTION DATA INTO DATAFRAME
path2 = r'D:\\project\\Phone_pe\\data\\map\\transaction\\hover\\country\\india\\state\\'

map_tra= os.listdir(path2)
# print(file_st)

Data2={'state': [], 'year': [], 'Quarter': [],"District": [], "count": [], "amount": []}
for state in map_tra:
    tra_sta=path2+state+'\\'
    file_yr=os.listdir(tra_sta)
    # print(tra_sta)
    for year in file_yr:
        tra_yr=tra_sta+year+'\\'
        file_j=os.listdir(tra_yr)
        # print(file_j)
        for file in file_j:
            file_json=tra_yr+file
            f=open(file_json,"r")
            End=json.load(f)
            for entry in End["data"]["hoverDataList"]:
                district_name = entry["name"]
    
                for metric_data in entry["metric"]:
                    transaction_type = metric_data["type"]
                    transaction_count = metric_data["count"]
                    transaction_amount = metric_data["amount"]
                    
                    # Append data to Data2 dictionary
                    Data2["District"].append(district_name)
                    # Data2["Transaction_type"].append(transaction_type)
                    Data2["count"].append(transaction_count)
                    Data2["amount"].append(transaction_amount)
                    Data2["state"].append(state)
                    Data2["year"].append(year)
                    Data2["Quarter"].append(int(file.strip('.json')))
        df_map_tras=pd.DataFrame(Data2)
        df_map_tras.shape
        # print(df_map_tras)
#IMPORTING MAP USER DATA INTO DATAFRAME
path3 = r'D:\\project\\Phone_pe\\data\\map\\user\\hover\\country\\india\\state\\'

map_user=os.listdir(path3)

Data3={"State": [], "Year": [], "Quarter": [], "District": [],
            "RegisteredUser": [], "AppOpens": []}
for state in map_user:
    file_states=path3+state+'\\'
    file_yr=os.listdir(file_states)
    for year in file_yr:
        file_year=file_states+year+'\\'
        file_j=os.listdir(file_year)
        for file in file_j:
            file_json=file_year+file
            f=open(file_json,"r")
            End=json.load(f)
            for i in End["data"]["hoverData"].items():
                Data3["District"].append(i[0])
                Data3["RegisteredUser"].append(i[1]["registeredUsers"])
                Data3["AppOpens"].append(i[1]["appOpens"])
                # Datamap_user= os.listdir(path3)["State"].append(state)
                Data3["State"].append(state)
                Data3["Year"].append(year)
                Data3["Quarter"].append(int(file.strip('.json')))
        df_map_user=pd.DataFrame(Data3)
        df_map_user.shape
 
            
path4 = r'D:\\project\\Phone_pe\\data\\top\\transaction\\country\\india\\state\\'
top_trans=os.listdir(path4)
Data4={'State': [], 'Year': [], 'Quarter': [], 'Pincode': [], 'Transaction_count': [],
            'Transaction_amount': []}

for state in top_trans:
    file_states=path4+state+'\\'
    file_yr=os.listdir(file_states)
    for year in file_yr:
        file_year=file_states+year+'\\'
        file_j=os.listdir(file_year)
        for file in file_j:
            file_json=file_year+file
            f=open(file_json,"r")
            End=json.load(f)
            for i in End["data"]["pincodes"]:
                Data4["Pincode"].append(i['entityName'])
                Data4["Transaction_count"].append(i["metric"]["count"])
                Data4["Transaction_amount"].append(i["metric"]["amount"])
                Data4["State"].append(state)
                Data4["Year"].append(year)
                Data4["Quarter"].append(int(file.strip('.json')))
        df_top_trans=pd.DataFrame(Data4)
        df_top_trans.shape
#IMPORTING TOP USER DATA INTO DATAFRAME
path5 = r'D:\\project\\Phone_pe\\data\\top\\user\\country\\india\\state\\'
top_user=os.listdir(path5)
Data5={'State': [], 'Year': [], 'Quarter': [], 'Pincode': [],
            'RegisteredUsers': []}
for state in top_user:
    file_states=path5+state+'\\'
    file_yr=os.listdir(file_states)
    for year in file_yr:
        file_year=file_states+year+'\\'
        file_j=os.listdir(file_year)
        for file in file_j:
            file_json=file_year+file
            f=open(file_json,"r")
            End=json.load(f)
            for i in End["data"]["pincodes"]:
                Data5["Pincode"].append(i['name'])
                Data5["RegisteredUsers"].append(i["registeredUsers"])
                Data5["State"].append(state)
                Data5["Year"].append(year)
                Data5["Quarter"].append(int(file.strip('.json')))
        df_top_user=pd.DataFrame(Data5)
        df_top_user.shape
#CONNECTION WITH SQL
# mydb=mysql.connector.connect(
# host="127.0.0.1",
# user='root',
# password="confident23",
# )
# mycursor=mydb.cursor(buffered=True)#CREATING DATABASE
# mycursor.execute("CREATE DATABASE phonepe")
# mydb=mysql.connect(
#       host="localhost",
#       user="root",
#       password="confident23",
#       database="phonepe")
# mycursor=mydb.cursor(buffered=True)

# Establish connection to MySQL server
mydb = mysql.connector.connect(
    host="127.0.0.1",
    user="root",
    password="confident23"
)

# Create a cursor
mycursor = mydb.cursor(buffered=True)

# Create the 'phonepe' database
mycursor.execute("CREATE DATABASE IF NOT EXISTS phonepe")

# Connect to the 'phonepe' database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="confident23",  # Replace with your actual password
    database="phonepe"
)

# Create a cursor for the 'phonepe' database
mycursor = mydb.cursor(buffered=True)
#CREATING TABLE AND INSERTING VALUES FROM DATAFRAMES TO SQL TABLES
mycursor.execute("create table agg_trans (State varchar(100), Year int, Quarter int, Transaction_type varchar(100), Transaction_count int, Transaction_amount double)")

for i,row in df_agg_tran.iterrows():
    #here %S means string values 
    sql = "INSERT INTO agg_trans VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    # the connection is not auto committed by default, so we must commit to save our changes
    mydb.commit()
mycursor.execute("create table agg_user (State varchar(100), Year int, Quarter int, Brands varchar(100), Count int, Percentage double)")

for i,row in df_agg_usr.iterrows():
    sql = "INSERT INTO agg_user VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    mydb.commit()
mycursor.execute("create table map_trans (State varchar(100), Year int, Quarter int, District varchar(100), Count int, Amount double)")

for i,row in df_map_tras.iterrows():
    sql = "INSERT INTO map_trans VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    mydb.commit()
mycursor.execute("create table map_user (State varchar(100), Year int, Quarter int, District varchar(100), Registered_user int, App_opens int)")

for i,row in df_map_user.iterrows():
    sql = "INSERT INTO map_user VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    mydb.commit()
mycursor.execute("create table top_trans (State varchar(100), Year int, Quarter int, Pincode int, Transaction_count int, Transaction_amount double)")

for i,row in df_top_trans.iterrows():
    sql = "INSERT INTO top_trans VALUES (%s,%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    mydb.commit()
mycursor.execute("create table top_user (State varchar(100), Year int, Quarter int, Pincode int, Registered_users int)")

for i,row in df_top_user.iterrows(): 
    sql = "INSERT INTO top_user VALUES (%s,%s,%s,%s,%s)"
    mycursor.execute(sql, tuple(row))
    mydb.commit()