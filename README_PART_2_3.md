# 🧰  PART - 2 data preprocessing and model analysis

### ➡️  DONE IN 2_model_analysis_of_aqi_in_india.ipynb

# 🪟 where you can get this data?

The dataset is avaible on kaggle this is the link: https://www.kaggle.com/datasets/rohanrao/air-quality-data-in-india

* city_day csv
* city_hour csv
* station_day csv
* station_hour csv
* station csv

********

this is the second part of the project in this we will perform 

* Preliminary and Exploratory analysis of station_merged csv (already done in part 1 but there are some changes done in this csv)

* making the making the xgb_model which will be used to predict aqi in part 3

### 📚 about the dataset

a lot of the preliminary data analysis has already been done in the previous part of this project in this part we will discuss the station_merged csv 

### 📕 station_merged csv / station_merged_data / station_merged_df:

this csv contains the chemical reading in the air with the station's location and date of reading

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

this is a combination of exercise and calories csv



### 2_model_analysis_of_aqi_in_india.ipynb :

* some of preliminary and Exploratory data analysis has been done in this ipynb

* this ipynb mainly concentrates on data preprocessing and model analysis 

* check the previous part for Preliminary and Exploratory analysis of station_merged csv


### 🛠️ 1.Preliminary data analysis:
Edit the data to prepare it for further analysis, describe the key features of the data, and summarize the results.

* dropped the "StationId", "City", "State", "year", "month", "day", "AQI_Bucket" columns as we dont need them

* null values have already been taken care of in the previous part

### ⛓️ 2.Exploratory data analysis:

Investigate data sets and summarize their main characteristics, often employing data visualization methods

* theses following plots were made

#### 1) distrtibution of AQI throughout the 100000 readings: 

![image](https://user-images.githubusercontent.com/91218998/228846324-69ba1c1c-cecd-43ab-9f17-80fa30c6b5fc.png)

#### 2) distribution plots of all feature columns throughout the same readings:

![image](https://user-images.githubusercontent.com/91218998/228846161-e133f092-2ac3-4450-9d95-27c1767f1643.png)

#### 3) Correlation of AQI with features:

![image](https://user-images.githubusercontent.com/91218998/228847891-653587b2-2806-4833-9c28-3fe89f9730d8.png)

### ⚒️ 3. Data pre-processing:

The dataset is preprocessed in order to check missing values, noisy data, and other inconsistencies before executing it to the algorithm.

* notice how all the columns are right skewed to solve this following steps were taken 

#### 1) PM10, PM2.5 were in hundreds but Benzene, Toluene were in tens making the data biased towards PM10, PM2.5 so to solve this the data was sclaed using standardscaler, these are the columns after scaling the features:

![image](https://user-images.githubusercontent.com/91218998/228848576-a40a60bc-157c-46aa-8db3-0dcc61b33c0e.png)

#### 2) to solve the right skewed issue the scaled data was then yeo transformed:

![image](https://user-images.githubusercontent.com/91218998/228849026-e3d42ed6-115f-40d7-8c05-1ecf6c4f4155.png)
![image](https://user-images.githubusercontent.com/91218998/228849099-c159b04e-9614-4d11-9dde-fede8a3f9928.png)
![image](https://user-images.githubusercontent.com/91218998/228849252-1e12fe5b-82ed-4efd-8a81-42e3c6fb37c7.png)
![image](https://user-images.githubusercontent.com/91218998/228849305-c565b99c-6bb0-4bae-ab84-415e74ceaddb.png)

### 🧰 5. Model development & evaluation:

Model comparison involves comparing the performance of different models on a given task to identify which model is most effective.

* data is fitted into diffrent models and there respective testing r2 scores are as follows:-

![image](https://user-images.githubusercontent.com/91218998/228850077-150651c6-a4c3-4624-8ffd-f82855956f4b.png)

* the graph of training, testing, mea mse cross_val_scores:

![image](https://user-images.githubusercontent.com/91218998/228850555-812206f7-9b78-4f5c-bf0a-3036c67acd84.png)

* The xgb_model was the best one of the model used with scores of:

![image](https://user-images.githubusercontent.com/91218998/228851135-cfcfac73-71a8-44d3-b299-099e8e2cbdb4.png)

* XGBRegressor is the fastest and the best model with a cross_val_score of 0.84 and testing score of 0.91
* the best mea_score i could get was 21.22 which is not bad as aqi ranges from 0 - 400 but it can still be worked on
* The SVR model was the worst one of them all with it taking somewhere around 45min to train and test and the cross_val_score abd testing score 0.70, 0.67 respectively (mlr model has lower score but it took way less time to train and test)

******

# PART 3 - GUI PROGRAM
#### ➡️  DONE IN 3_main_AQI_predictor.pyw

#### now that we have chosen XGBRregressor as our model this program how the 3_main_AQI_predictor.pyw works:

    1. initializes all the path, object variables and loads the xgb_model 

    2. maakes a window that greets the user asking for their 12 independent features

    3. if inccorect or empty values are given it shows an error msg 

    4. finnaly if correct values are given it shows the user the output


# ----------------------------------------

# 🪟 inputs and outputs of 3_main_AQI_predictor.pyw  

#### i would reccomond you watch the demo_video attached in the files as it would give you a clear image on what the project looks like but here are some Screenshots of the GUI

#### 1. asking for 12 independent features:


![image](https://user-images.githubusercontent.com/91218998/228854153-33734542-f12a-4d97-ac22-a78d290b133e.png)

#### 2. error measage in case someone enter words or empty values

![image](https://user-images.githubusercontent.com/91218998/228855145-accb7ff5-4355-4b89-b697-c1833fac2f13.png)


#### 3. speacial error measge if alphanumeric entries are given

![image](https://user-images.githubusercontent.com/91218998/228855589-7d73df15-6a67-418e-8ea2-411d044e0a14.png)

#### 4. output of the above input if all entries are correct (actual value - 59)

![image](https://user-images.githubusercontent.com/91218998/228854505-3deafbc1-9dbe-4c53-b3a8-e72b163c072b.png)


# ⛔ Limitations

* The Rmse score of the model is 1 unit higher

* the program still has an mea of 21 units which can make a big diffrance when applied in real life. in the output photo there was an error of -11 units

* the program does not have a proper website or app 

# 📌 Conclusion

* The best model in the research paper was (Ridge regression mea = 27.907, rmse = 36.791, r2 = 0.8089) on city_data csv
* my best model in this notebook was (xgb_model mea = 21.22, rmse = 37.011, r2 = 0.91) on station_data csv

* the city_data csv has only 30000 rows while station_data csv has 100000 which is way more data 
* my model has achived better mea and r2 scores on a bigger scale of data making it better than the ridge reggression model made in the research paper

* but my is not the best and can still be upgraded 
* xgb_model has worse rmse of 37.011 which is 1 units more than rigde regression model

# 🔜 future upgrades

* building a dedicated website or app so the program can be avaible
on both pc and mobile

* improving the model to have less error and mea / mse / Rmse score

# 👨‍🦱credits and contact info:-

* made by Aryan Rathore
* LinkedIn : https://www.linkedin.com/in/aryan-rathore-b15459215/
* email: aryanrathore13572002@gmail.com, aryan.rathore2021@vitbhopal.ac.in


# ---------------------------------------

