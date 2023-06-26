# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 02:21:19 2023

@author: user
"""

import numpy as np 
import pickle
import streamlit  as st
#loaded the saved model
loaded_model=pickle.load(open("C:/Users/user/Downloads/trained_model(1).sav","rb"))

#creating a function for prediction
def bankruptcy_prediction(input_data):
    print(input_data)
    
    #changing the input_data to numpy array
    input_data_as_numpy_array=np.asarray(input_data)
    #reshape the array as we predicting for one instance
    input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
    prediction=loaded_model.predict(input_data_reshaped)
    print(prediction)
    if(prediction[0]==0):
       return "The company is non-bankrupt"
    else:
       return "The company is bankrupt"
    
def main():
    
    #giving a tittle 
    st.title("bankruptcy prediction web app")
    #getting the data from the user
    industrial_risk = st.selectbox("industrial_risk",['0.0','0.5','1.0'])
    management_risk = st.selectbox("management_risk",['0.0','0.5','1.0'])
    financial_flexibility = st.selectbox("financial_flexibility",['0.0','0.5','1.0'])
    credibility = st.selectbox("credibility",['0.0','0.5','1.0'])
    competitiveness = st.selectbox("competitiveness",['0.0','0.5','1.0'])
    operating_risk = st.selectbox("operating_risk",['0.0','0.5','1.0'])
    
    #code for prediction  
    bankruptcy=""
    
    #creating a button for prediction
    if st.button("bankruptcy result"):
        bankruptcy=bankruptcy_prediction([industrial_risk,management_risk,financial_flexibility,credibility,competitiveness,operating_risk])
        
        st.success(bankruptcy)
        
if __name__=='__main__':
    main()
       
        
   
