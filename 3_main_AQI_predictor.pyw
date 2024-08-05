########################################################### CREDITS ##############################################################################################

'''
                                                  WELCOME TO THE main_AQI_predictor

                       THIS PROGRAM PREDICTS THE AIR QUALITY INDEX (AIR POLLUTION) OF A REGION BASED ON 12 FACTORS

                                                    MADE BY : ARYAN RATHORE 
                                            COMPUTER SCIENCE ENGINEER AT VIT BHOPAL

                                                        CONTACT INFO
                                                aryanrathore13572002@gmail.com
                                               aryan.rathore2021@vitbhopal.ac.in
                                          github :- https://github.com/aryanrathore1012
                                    LINKEDIN - https://www.linkedin.com/in/aryan-rathore-b15459215/
'''

########################################################### IMPORTS ##############################################################################################

from tkinter import *
from tkinter import messagebox as tmsg
import customtkinter
from PIL import ImageTk, Image
from tkinter import messagebox as tmsg
import numpy as np
import pandas as pd
import datetime as dt
from tkinter import ttk
import joblib

########################################################### FUNCTIONS ###################################################################0#########################

'''                                                             IMPORTANT NOTE                                                              
                                  BEFORE YOU RUN THE PROGRAM MAKE SURE YOU READ AND FOLLOW THE LINES BELOW  
                                                       OTHERWISE THE PROGRAM WONT RUN                  '''
                                                                                           
# 0

'''     
                                                            PART 3 - GUI PROGRAMM
        THIS IS THE THIRD PART OF AQI_analysis_of_indian_states_and_cities PROJECT WHICH MAKE A GUI PROGRAM THAT CALCULATES AND SHOWS AQI
'''                                                                                                                                             

# 1

'''          THERE IS 1 FUNCTION "EVERY FUNCTION HAS A DOCSTRING LIKE THIS SPECIFIES WHAT THAT FUNCTION DOES
                                                    AND HOW THE THE FUNCTION WORKS"                                                      '''
# 2

'''       MAKE SURE YOU READ THE "1_exploratory_analysis_of_aqi_in_india.ipynb" AND "2_model_analysis_of_aqi_in_india.ipynb" 
                 BEFORE USING THIS AS IT HAS THE INFO ON THE DATA AND WHY USED THE XGBREGRESSOR FOR MY PREDICTIONS                                         '''

# 3

'''   I HAVE TO SPECIFY A FILE PATH TO read the data from (xgb_model and all the images and icons) FILES IF 
    YOU ARE USING OR COPY PASTING MY CODE MAKE YOU CHANGE THE FILE PATHS I HAVE SPECIFIED WHICH FUNCTIONS NEED A 'FILE PATH CHANGE' 
                                                    SO MAKE SURE YOU CHANGE THEM FIRST '''

# 4

'''
                  ||||||| JUST CHANGE THE FILE PATHS FROM LINE 87 TO 89 AND YOU CAN RUN THE PROGRAM FOR YOURSELF |||||||
'''

class AQI_prediction:
    
    def __init__(self) -> None: # FILE PATH CAHNGE IN THIS FUNCTION
        
        '''

            this function initializes all variable, creates and displays the main window.
            
            steps:

            1. initialize all path variables
            2. load the xgb_model using joblib
            3. make the main window
            4. if values are incorrect (aplhabets and empty entries) shows the user error msg
            5. if values are correct caclulates the aqi and show the it to the user 
            6. show special error measage if the user enters an alphanumeric entry like "123ahs" or "123%$!123" or "12,02"            
    
        '''

        # ------------------------------------------------------------------------------------------------------------------
        # 1. initialize all path variables

        self.model_path = "F://aryans_code_notes//machine_learning//AQI_predictior//xgb_model"
        self.icon_path = "F://aryans_code_notes//machine_learning//AQI_predictior//aqi_icon.ico"
        self.pattern_path = "F://aryans_code_notes//machine_learning//AQI_predictior//pattern.jpg"

        # -------------------------------------------------------------------------------------------------------------------
        # 2. load the xgb_model using joblib

        self.xgb_model = joblib.load(self.model_path)

        # -------------------------------------------------------------------------------------------------------------------
        # 3. make the main window
            
        customtkinter.set_appearance_mode("dark")
        customtkinter.set_default_color_theme("green")

        main_window = customtkinter.CTk()
        main_window.geometry("1250x800")
        main_window.wm_iconbitmap(self.icon_path)
        main_window.title("main_AQI_predictor")

        pattern_image = customtkinter.CTkImage(light_image=Image.open(self.pattern_path), dark_image=Image.open(self.pattern_path),size=(1250, 800))
        bg_image = customtkinter.CTkLabel(master=main_window, image=pattern_image, text="").pack()

        main_frame = customtkinter.CTkFrame(master=bg_image, width=1100, height=700, corner_radius=20)
        main_frame.place(relx=0.5, rely=0.5, anchor=CENTER)

        PM25_var = StringVar()        
        PM10_var = StringVar()
        NO_var = StringVar()
        NO2_var = StringVar()
        NOx_var = StringVar()
        NH3_var = StringVar()
        CO_var = StringVar()
        SO2_var = StringVar()
        O3_var = StringVar()
        Benzene_var = StringVar()
        Toluene_var = StringVar()
        Xylene_var = StringVar()

        Variable_list = [PM25_var ,PM10_var ,NO_var ,NO2_var ,NOx_var ,NH3_var ,CO_var ,SO2_var ,O3_var ,Benzene_var ,Toluene_var ,Xylene_var]

        l2=customtkinter.CTkLabel(master=main_frame, text="Enter the amount of amount of pollutants",font=('Century Gothic',30))
        l2.place(x=260, y=45)

        
        customtkinter.CTkLabel(master=main_frame, text="PM 2.5",font=('Century Gothic',15)).place(x=150, y=160)
        customtkinter.CTkEntry(master=main_frame, width=220,height=30, textvariable=PM25_var).place(x=300, y=160)

        customtkinter.CTkLabel(master=main_frame, text="PM 10",font=('Century Gothic',15)).place(x=150, y=240)
        customtkinter.CTkEntry(master=main_frame, width=220,height=30, textvariable=PM10_var).place(x=300, y=240)

        customtkinter.CTkLabel(master=main_frame, text="NO",font=('Century Gothic',15)).place(x=150, y=320)
        customtkinter.CTkEntry(master=main_frame, width=220,height=30, textvariable=NO_var).place(x=300, y=320)

        customtkinter.CTkLabel(master=main_frame, text="NO2",font=('Century Gothic',15)).place(x=150, y=400)
        customtkinter.CTkEntry(master=main_frame, width=220,height=30, textvariable=NO2_var).place(x=300, y=400)

        customtkinter.CTkLabel(master=main_frame, text="NOx",font=('Century Gothic',15)).place(x=150, y=480)
        customtkinter.CTkEntry(master=main_frame, width=220,height=30, textvariable=NOx_var).place(x=300, y=480)

        customtkinter.CTkLabel(master=main_frame, text="NH3",font=('Century Gothic',15)).place(x=150, y=560)
        customtkinter.CTkEntry(master=main_frame, width=220,height=30, textvariable=NH3_var).place(x=300, y=560)

        # ----------------------------------------------------------------------------------------------------------

        customtkinter.CTkLabel(master=main_frame, text="CO",font=('Century Gothic',15)).place(x=650, y=160)
        customtkinter.CTkEntry(master=main_frame, width=220,height=30, textvariable=CO_var).place(x=750, y=160)

        customtkinter.CTkLabel(master=main_frame, text="SO2",font=('Century Gothic',15)).place(x=650, y=240)
        customtkinter.CTkEntry(master=main_frame, width=220,height=30, textvariable=SO2_var).place(x=750, y=240)

        customtkinter.CTkLabel(master=main_frame, text="O3",font=('Century Gothic',15)).place(x=650, y=320)
        customtkinter.CTkEntry(master=main_frame, width=220,height=30, textvariable=O3_var).place(x=750, y=320)

        customtkinter.CTkLabel(master=main_frame, text="Benzene",font=('Century Gothic',15)).place(x=650, y=400)
        customtkinter.CTkEntry(master=main_frame, width=220,height=30, textvariable=Benzene_var).place(x=750, y=400)

        customtkinter.CTkLabel(master=main_frame, text="Toluene",font=('Century Gothic',15)).place(x=650, y=480)
        customtkinter.CTkEntry(master=main_frame, width=220,height=30, textvariable=Toluene_var).place(x=750, y=480)

        customtkinter.CTkLabel(master=main_frame, text="Xylene",font=('Century Gothic',15)).place(x=650, y=560)
        customtkinter.CTkEntry(master=main_frame, width=220,height=30, textvariable=Xylene_var).place(x=750, y=560)

        def get_aqi():
            
            # -------------------------------------------------------------------------------------------------------------------
            # 4. if values are incorrect (aplhabets and empty entries) shows the user error msg

            for variable in Variable_list:
                
                if variable.get() == None or str(variable.get()).isalpha() == True:
                    tmsg.showerror("Entry Error","All values should be numeric and not empty")
                    break

            else:
                
                # -------------------------------------------------------------------------------------------------------------------
                # 5. if values are correct caclulates the aqi and show the it to the user 

                try:
                    aqi_status = ""
                    input_array = np.array([[float(PM25_var.get()) ,float(PM10_var.get()) ,float(NO_var.get()) ,float(NO2_var.get()) ,float(NOx_var.get()) ,float(NH3_var.get()) ,float(CO_var.get()) ,float(SO2_var.get()) ,float(O3_var.get()) ,float(Benzene_var.get()) ,float(Toluene_var.get()) ,float(Xylene_var.get())]])
                    prediction = self.xgb_model.predict(input_array)


                    # print(prediction[0])
                    if 0 < prediction[0] and prediction[0] <= 50:
                        aqi_status = "Good"
                    elif prediction[0] <= 100:
                        aqi_status = "Satisfactory"
                    elif prediction[0] <= 200:
                        aqi_status = "Moderately Polluted"
                    elif prediction[0] <= 300:
                        aqi_status = "poor"
                    elif prediction[0] <= 400:
                        aqi_status = "very poor"
                    elif prediction[0] <= 500:
                        aqi_status = "severe"
                    else:
                        aqi_status = "deadly"

                    tmsg.showinfo("Prediction successfull",f"AQI : {int(prediction[0])}, Status : {aqi_status}\n\n --- there may be an error in range of +- 0 units to 21 units")
                
                # -------------------------------------------------------------------------------------------------------------------
                # 6. show special error measage if the user enters an alphanumeric entry like "123ahs" or "123%$!123" or "12,02"

                except:
                    tmsg.showerror("number error", "some values in the form have letter or special charecters in them like comma(,) percentage(%) exapmple: '123,45' or '12.23aaa' please correct them first")

        
        customtkinter.CTkButton(master=main_frame,width=150,height=45,border_width=0,border_color="white",corner_radius=8,text="get AQI",command=get_aqi).place(x=215, y=630)
        customtkinter.CTkButton(master=main_frame,width=150,height=45,border_width=0,border_color="white",corner_radius=8,text="Quit",command=quit, fg_color=("#FF2400","#FF2400"), hover_color=("#C21807","#C21807")).place(x=700, y=630)
        
        main_window.mainloop()
    

start = AQI_prediction()