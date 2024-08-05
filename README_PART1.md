# 🔬  PART - 1 Preliminary and Exploratory data analysis of aqi in india

### 	➡️  DONE IN 1_exploratory_analysis_of_aqi_in_india.ipynb

# 🪟 where you can get this data?

The dataset is avaible on kaggle this is the link: https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india

* city_day csv
* city_hour csv
* station_day csv
* station_hour csv
* station csv

The links for geo json files of india are as follows:

* state geojson: https://github.com/Subhash9325/GeoJson-Data-of-Indian-States
* district geojson: https://www.kaggle.com/datasets/krutarthhd/india-geojson-file?select=district

********

this is the first part of the project in this we will perform 

* Preliminary and Exploratory analysis of station and station_day csv

* making the station_merged csv and using the data to visualze certain graph

OUTPUT GRAPHS GIVEN BELOW

### 📚 about the dataset

the dataset has 5 csv city_day, city_hour, station_day, station_hour, station csv out of these i have used only station_day and station csv as they have more data (more than 100000 rows) 

### 📕 station csv:-

this csv contains all the info on the stations

| #  | Column      | Non-Null Count | Dtype  |
|:---: | :------:      | -------------- | -----  |
| 0  | StationId   | 230 non-null   | object |
| 1  | StationName | 230 non-null   | object |
| 2  | City        | 230 non-null   | object |
| 3  | State       | 230 non-null   | object |
| 4  | Status      | 133 non-null   | object |

the Column are self-Exploratory

### 📗 station_day csv:-

this csv contains the aqi readings throughout the day as recorded by the station 

|#   |Column     | Non-Null Count   |Dtype   |
|--- | ------    |  --------------  | -----  |
| 0  | StationId |  108035 non-null | object |
| 1  | Date      |  108035 non-null | object |
| 2  | PM2.5     |  86410 non-null  | float64|
| 3  | PM10      |  65329 non-null  | float64|
| 4  | NO        |  90929 non-null  | float64|
| 5  | NO2       |  91488 non-null  | float64|
| 6  | NOx       |  92535 non-null  | float64|
| 7  | NH3       |  59930 non-null  | float64|
| 8  | CO        |  95037 non-null  | float64|
| 9  | SO2       |  82831 non-null  | float64|
| 10 | O3        |  82467 non-null  | float64|
| 11 | Benzene   |  76580 non-null  | float64|
| 12 | Toluene   |  69333 non-null  | float64|
| 13 | Xylene    |  22898 non-null  | float64|
| 14 | AQI       |  87025 non-null  | float64|
| 15 | AQI_Bucket|  87025 non-null  | object |


### 📙 station_merged csv:-

* this is our main csv, this is a combination of all Columns from
station_day (features and target) station csv (Date)

* this is the main csv that the part 2 and part 3 of the project 
will used to train their model and show output



| #  | Column     | Non-Null Count  | Dtype   |    meaning   |
|:-: | :------:     | :--------------:  | :-----:   | :---:  |
| 0  | StationId  | 108035 non-null | object  |    id of the station   |
| 1  | City       | 108035 non-null | object  |    city in which the station is located   |
| 2  | State      | 108035 non-null | object  |    state in which the station is located   |
| _  | Date       | 108035 non-null | object  |    date of the readings (now removed)   |
| 3  | PM2.5      | 86410 non-null  | float64 |    amount of said checmical in the air   |
| 4  | PM10       | 65329 non-null  | float64 |    amount of said checmical in the air   |
| 5  | NO         | 90929 non-null  | float64 |    amount of said checmical in the air   |
| 6  | NO2        | 91488 non-null  | float64 |    amount of said checmical in the air   |
| 7  | NOx        | 92535 non-null  | float64 |    amount of said checmical in the air   |
| 8  | NH3        | 59930 non-null  | float64 |    amount of said checmical in the air   |
| 9  | CO         | 95037 non-null  | float64 |    amount of said checmical in the air   |
| 10 | SO2        | 82831 non-null  | float64 |    amount of said checmical in the air   |
| 11 | O3         | 82467 non-null  | float64 |    amount of said checmical in the air   |
| 12 | Benzene    | 76580 non-null  | float64 |    amount of said checmical in the air   |
| 13 | Toluene    | 69333 non-null  | float64 |    amount of said checmical in the air   |
| 14 | Xylene     | 22898 non-null  | float64 |    amount of said checmical in the air   |
| 15 | AQI        | 87025 non-null  | float64 |    the air quality that day   |
| 16 | AQI_Bucket | 87025 non-null  | object  |    AQI catagory ranges from good to severe   |
| 17 | year       | 87025 non-null  | float64 |    year of the reading   |
| 18 | month      | 87025 non-null  | float64 |    month of the reading   |
| 18 | date       | 87025 non-null  | float64 |    day of the reading   |


* this is a combination of station and station_day csv with over 100000 rows

# 🖋️ The Fun Part:

### 🛠️ 1.Preliminary data analysis:
Edit the data to prepare it for further analysis, describe the key features of the data, and summarize the results.

* station and station_day csv were merged to make station_merged csv 

* dropped all columns where aqi reading was none
* numerical missing values were replaced with means of the respective columns 
* dropped the date column and added day, month, year columns instead


### ⛓️ 2. Exploratory data analysis with insights (the main goal of this ipynb) :

Investigate data sets and summarize their main characteristics, often employing data visualization methods

* major Exploratory data analysis has been done of all columns, states and citites on the basis of month, year and range from 2016-2020

* these 10 types of graphs are made:

### ✒️ 1. trend of aqi throughout the years 

![image](https://user-images.githubusercontent.com/91218998/228776720-35e71870-bae6-4ffa-9a0b-823715b1ff0e.png)

* aqi has steadily decreased throughout the years with a major drop from 2019 to 2020 due to corona

### ✒️ 2. aqi trend of states in india

![image](https://user-images.githubusercontent.com/91218998/228777567-6cf011b5-938d-4f58-bb28-90b9c4d18ede.png)

### ✒️ 3. aqi trend of cities in india

![image](https://user-images.githubusercontent.com/91218998/228777808-dd4ff1bf-3309-4776-8549-cc83f32967be.png)

### ✒️ 4. Yearly/ monthly state_Aqi_from_2015_to_2020 function

* this function shows the graph of (Yearly/ monthly) aqi of (all avaible) states from 2015-2020

* list of 21 states avaible that you make visualization of:
['Andhra Pradesh', 'Assam', 'Bihar', 'Chandigarh', 'Delhi', 'Gujarat', 'Haryana', 'Jharkhand', 'Karnataka', 'Kerala', 'Madhya Pradesh', 'Maharashtra', 'Meghalaya', 'Mizoram', 'Odisha', 'Punjab', 'Rajasthan', 'Tamil Nadu', 'Telangana', 'Uttar Pradesh', 'West Bengal']

#### monthly state aqi trend:

![image](https://user-images.githubusercontent.com/91218998/228789421-9a8cb728-74de-4927-a8b1-a708c246aa3b.png)

#### Yearly state aqi trend:

![image](https://user-images.githubusercontent.com/91218998/228789827-16229f4c-29e7-4c23-b88f-6b2077b6e769.png)


### ✒️ 5. Yearly/ monthly city_Aqi_from_2015_to_2020 function

* this function shows the graph of (Yearly/ monthly) aqi of a cities in india from 2015-2020

* list of 26 cities avaible that you make visualization of:
['Amaravati', 'Visakhapatnam', 'Guwahati', 'Patna', 'Chandigarh', 'Delhi', 'Ahmedabad', 'Gurugram', 'Jorapokhar', 'Bengaluru','Ernakulam', 'Kochi', 'Thiruvananthapuram', 'Bhopal', 'Mumbai' 'Shillong', 'Aizawl', 'Brajrajnagar', 'Talcher', 'Amritsar','Jaipur', 'Chennai', 'Coimbatore', 'Hyderabad', 'Lucknow' 'Kolkata']

#### 🖌️ monthly aqi trend of city:

![image](https://user-images.githubusercontent.com/91218998/228792278-bf38062f-7246-4d1a-91e5-595f5f8c0203.png)

#### 🖌️ Yearly aqi trend of city:
![image](https://user-images.githubusercontent.com/91218998/228790939-ac0e69dd-a573-4b26-b98b-7d04e60c725a.png)


### ✒️ 6. correlation of toxic gasses with aqi (top 3)

![image](https://user-images.githubusercontent.com/91218998/228792863-3769fee0-dbc8-4e33-9932-d3b64906382d.png)

* PM10, PM2.5, NO2 are the biggest contributors in aqi trend this can be proved by the graphs as well

### ✒️ 7. yearly/monthly state_toxic_gas_from_2015_2020 india function

* this function shows the trend of PM10, PM2.5, NO2 in a state from 2015-2020 (can show graph of all 21 avaible states)

#### 🖌️ monthly pollution gasses trend of state:

![image](https://user-images.githubusercontent.com/91218998/228795922-3edb4c36-f859-415d-81cc-1a75d7947df0.png)

#### 🖌️ Yearly pollution gasses trend of state:

![image](https://user-images.githubusercontent.com/91218998/228795705-f6673a0c-86c5-4788-8959-635dd5a2ae6e.png)

###### notice how the pollution and aqi trend in the state andra Pradesh is similar this proves the high correlation of these 3 gasses with AQI in a graphical way

### ✒️ 8. yearly/monthly city_toxic_gas_from_2015_2020 india function

* this function shows the trend of PM10, PM2.5, NO2 in a city from 2015-2020 (can show graph of all 26 avaible cities)


#### 🖌️ monthly pollution gasses trend of City:

![image](https://user-images.githubusercontent.com/91218998/228797789-a8701ccd-6ed4-4f41-a6e3-0fc44b3b7e1e.png)

#### 🖌️ Yearly pollution gasses trend of City:

![image](https://user-images.githubusercontent.com/91218998/228797713-055b9a6f-e3a1-493d-a7ab-aeb9155a166f.png)

### ✒️ 9. aqi of states on an india map

![image](https://user-images.githubusercontent.com/91218998/228799299-9d256766-8be8-4c04-b813-9d1f1978b004.png)

* this is an interactive map you can play with it in the ipynb

### ✒️ 10. aqi of states on an india map

![image](https://user-images.githubusercontent.com/91218998/228798992-5c875230-ddb6-40fc-8275-8ba19eaa1d96.png)

###### this graph is misleading as not much district data was avaible in the geojson making cities with higher aqi look lighter in color


# 📌 Conclusion

* Gujarat has the highest AQI in all state while Mizoram has the lowest. Delhi having the second highest aqi

* Ahmedabad has the highest AQI in all cities while Aizawl has lowest. Delhi having the second highest aqi

* PM10, PM2.5, NO2 are the highest contributors in growth of aqi this has been proved mathatically and by graphs throughout

* in southern india jan seems to be the most toxic month while april or jun seem to be the lowest in aqi


# 👨‍🦱credits and contact info:-

* made by Aryan Rathore
* LinkedIn : https://www.linkedin.com/in/aryan-rathore-b15459215/
* email: aryanrathore13572002@gmail.com, aryan.rathore2021@vitbhopal.ac.in


# ---------------------------------------

