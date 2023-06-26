# -*- coding: utf-8 -*-
"""
Created on Thu Feb 23 01:58:07 2023

@author: user
"""

import numpy as np
import pickle
from sklearn.ensemble import RandomForestClassifier
#loaded the saved model
loaded_model=pickle.load(open("C:/Users/user/Downloads/trained_model(1).sav","rb"))

input_data=(0.5,0,0,0.5,0,1)
#changing the input_data to numpy array
input_data_as_numpy_array=np.asarray(input_data)
#reshape the array as we predicting for one instance
input_data_reshaped=input_data_as_numpy_array.reshape(1,-1)
prediction=loaded_model.predict(input_data_reshaped)
print(prediction)
if(prediction[0]==0):
    print("The company is non-bankrupt")
else:
    print("The company is bankrupt")
