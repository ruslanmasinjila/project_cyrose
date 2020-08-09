import pandas as pd


#data.columns = data.columns.str.strip().str.lower().str.replace(' ', '_').str.replace('(', '').str.replace(')', '')
#data.to_csv("clean_blood.csv")

##########################################################################################
data = pd.read_csv("clean_blood.csv")
supply_data2015 = pd.DataFrame()
supply_data2015["2015_rbtc_colle"] = data["2015_rbtc_colle"]
supply_data2015["2015_donated_blood_units"] = data["2015_donated_blood_units"]
supply_data2015["2015_blood_other_sources"] = data["2015_blood_other_sources"]
supply_data2015["2015_no_of_units_requested_from_other_transfusing_hospi"] = data["2015_no_of_units_requested_from_other_transfusing_hospi"]
supply_data2015["2015__blood_units_received_from_moh_706blood_transfusio"] = data["2015__blood_units_received_from_moh_706blood_transfusio"]

# Get some across the rows
supply_data2015["supply"] = supply_data2015.sum(axis=1)


supply_2015 = pd.DataFrame()
supply_2015["orgunitlevel4"] = data["orgunitlevel4"]
supply_2015["supply"] = supply_data2015["supply"]

# Group identical Wards ("orgunitlevel4") and find the total sum for the Ward
supply_2015=supply_2015.groupby(['orgunitlevel4']).sum()

print(supply_2015.head(15))

supply_2015=supply_2015.loc[(supply_2015!=0).any(axis=1)]

print(supply_2015.head(15))

##########################################################################################










#print(data.head())

#data=data.groupby(['orgunitlevel4']).sum()

#print(data.head(50))

#print(data.isnull().sum(axis = 1))




