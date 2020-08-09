import pandas as pd

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

##########################################################################################
supply_data2016 = pd.DataFrame()
supply_data2016["2016_rbtc_colle"] = data["2016_rbtc_colle"]
supply_data2016["2016_donated_blood_units"] = data["2016_donated_blood_units"]
supply_data2016["2016_blood_other_sources"] = data["2016_blood_other_sources"]
supply_data2016["2016_no_of_units_requested_from_other_transfusing_hospi"] = data["2016_no_of_units_requested_from_other_transfusing_hospi"]
supply_data2016["2016__blood_units_received_from_moh_706blood_transfusio"] = data["2016__blood_units_received_from_moh_706blood_transfusio"]

# Get some across the rows
supply_data2016["supply"] = supply_data2016.sum(axis=1)


supply_2016 = pd.DataFrame()
supply_2016["orgunitlevel4"] = data["orgunitlevel4"]
supply_2016["supply"] = supply_data2016["supply"]


##########################################################################################
supply_data2017 = pd.DataFrame()
supply_data2017["2017_rbtc_colle"] = data["2017_rbtc_colle"]
supply_data2017["2017_donated_blood_units"] = data["2017_donated_blood_units"]
supply_data2017["2017_blood_other_sources"] = data["2017_blood_other_sources"]
supply_data2017["2017_no_of_units_requested_from_other_transfusing_hospi"] = data["2017_no_of_units_requested_from_other_transfusing_hospi"]
supply_data2017["2017__blood_units_received_from_moh_706blood_transfusio"] = data["2017__blood_units_received_from_moh_706blood_transfusio"]

# Get some across the rows
supply_data2017["supply"] = supply_data2017.sum(axis=1)


supply_2017 = pd.DataFrame()
supply_2017["orgunitlevel4"] = data["orgunitlevel4"]
supply_2017["supply"] = supply_data2017["supply"]

##########################################################################################
supply_data2018 = pd.DataFrame()
supply_data2018["2018_rbtc_colle"] = data["2018_rbtc_colle"]
supply_data2018["2018_donated_blood_units"] = data["2018_donated_blood_units"]
supply_data2018["2018_blood_other_sources"] = data["2018_blood_other_sources"]
supply_data2018["2018_no_of_units_requested_from_other_transfusing_hospi"] = data["2018_no_of_units_requested_from_other_transfusing_hospi"]
supply_data2018["2018__blood_units_received_from_moh_706blood_transfusio"] = data["2018__blood_units_received_from_moh_706blood_transfusio"]

# Get some across the rows
supply_data2018["supply"] = supply_data2018.sum(axis=1)


supply_2018 = pd.DataFrame()
supply_2018["orgunitlevel4"] = data["orgunitlevel4"]
supply_2018["supply"] = supply_data2018["supply"]


##########################################################################################
supply_data2019 = pd.DataFrame()
supply_data2019["2019_rbtc_colle"] = data["2019_rbtc_colle"]
supply_data2019["2019_donated_blood_units"] = data["2019_donated_blood_units"]
supply_data2019["2019_blood_other_sources"] = data["2019_blood_other_sources"]
supply_data2019["2019_no_of_units_requested_from_other_transfusing_hospi"] = data["2019_no_of_units_requested_from_other_transfusing_hospi"]
supply_data2019["2019__blood_units_received_from_moh_706blood_transfusio"] = data["2019__blood_units_received_from_moh_706blood_transfusio"]

# Get some across the rows
supply_data2019["supply"] = supply_data2019.sum(axis=1)


supply_2019 = pd.DataFrame()
supply_2019["orgunitlevel4"] = data["orgunitlevel4"]
supply_2019["supply"] = supply_data2019["supply"]

##########################################################################################

print(supply_2015.head())
print(supply_2016.head())
print(supply_2017.head())
print(supply_2018.head())
print(supply_2019.head())

supply_2015.to_csv("supply_2015.csv")
supply_2016.to_csv("supply_2016.csv")
supply_2017.to_csv("supply_2017.csv")
supply_2018.to_csv("supply_2018.csv")
supply_2019.to_csv("supply_2019.csv")

##########################################################################################

aggregate_supply = pd.DataFrame()
aggregate_supply["orgunitlevel4"]=data["orgunitlevel4"]
aggregate_supply["2015"]=supply_2015["supply"]
aggregate_supply["2016"]=supply_2016["supply"]
aggregate_supply["2017"]=supply_2017["supply"]
aggregate_supply["2018"]=supply_2018["supply"]
aggregate_supply["2019"]=supply_2019["supply"]

# Group identical Wards ("orgunitlevel4") and find the total sum for the Ward
aggregate_supply=aggregate_supply.groupby(['orgunitlevel4']).sum()


# Remove all rows with zeroes
aggregate_supply=aggregate_supply.loc[(aggregate_supply!=0).any(axis=1)]

print(aggregate_supply)
aggregate_supply.to_csv("supply_2015_2019.csv")
##########################################################################################





















#print(data.head())

#data=data.groupby(['orgunitlevel4']).sum()

#print(data.head(50))

#print(data.isnull().sum(axis = 1))




